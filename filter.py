import os
import inspect

from constants import POSITIVE, NEGATIVE, POSITIVITY_THRESHOLD
from corpus import Corpus
from trainingcorpus import TrainingCorpus
import atomfilters, wordfilters
import utils

class MyFilter:
    '''COMBINES ALL OUR FILTERS TO GET THE BEST RESULTS POSSIBLE.'''
    def __init__(self):
        self.strong_filters = []
        self.normal_filters = []
        self.word_filters = []
        self.init_filters()

    def init_filters(self):
        # Initialize strong filters (>99% decisive)
        # print("Initializing BlacklistFilter")
        self.strong_filters.append(atomfilters.BlacklistFilter())
        # print("Initializing WhiteListFilter")
        self.strong_filters.append(atomfilters.WhitelistFilter())
        self.strong_filters.append(atomfilters.ReplyFilter())
        self.strong_filters.append(atomfilters.XSpamStatusFilter())

        # Initialize normal filters
        # self.normal_filters.append(atomfilters.HtmlFilter())

        # Initialize word filters
        for name, obj in inspect.getmembers(wordfilters):
            if inspect.isclass(obj):
                if obj.__module__ == "wordfilters":
                    # print("Initializing " + name)
                    filt = obj()
                    self.word_filters.append(filt)
    
    def train(self, dir_path):
        corpus = TrainingCorpus(dir_path)
        for filt in self.strong_filters + self.normal_filters + self.word_filters:
            # print("Training " + filt.__class__.__name__)
            filt.train(corpus)

    def test(self, dir_path):
        no_tests_done = 0
        rather_positive = 0
        corpus = Corpus(dir_path)
        clasif = dict()
        
        for name, mail in corpus.emails():
            # Test strong filters
            result = self.test_strong_filters(name, mail)
            if result != -1:    # Strong filters were decisive
                clasif[name] = result
                continue       # Skip to the next iteration

            score = 0
            tests_done = 0

            # Test normal filters
            result = self.test_word_filters(name, mail)
            score += result[0]
            tests_done += result[1]         

            # Test word filters
            result = self.test_word_filters(name, mail)
            score += result[0]
            tests_done += result[1]

            if tests_done == 0:
                no_tests_done += 1
                print("No tests were done for " + name)
                clasif[name] = NEGATIVE 
            elif score / tests_done > POSITIVITY_THRESHOLD:
                clasif[name] = POSITIVE
            else:
                if score / tests_done > 0.50:
                    rather_positive += 1
                clasif[name] = NEGATIVE

        utils.write_classification_to_file(clasif, dir_path + "/!prediction.txt")
        print("No tests done: {}".format(no_tests_done))
        print("Are rather positive but not tagged: {}".format(rather_positive))

    def test_strong_filters(self, name, mail):
        for filt in self.strong_filters:
            # print("Testing " + name + " with " + filt.__class__.__name__)
            result = filt.test(mail)

            if result != -1:    # Test is decisive
                if result > POSITIVITY_THRESHOLD:
                    return POSITIVE
                elif result < POSITIVITY_THRESHOLD:
                    return NEGATIVE
        # No tests were decisive
        return -1

    def test_normal_filters(self, name, mail):
        score = 0
        tests_done = 0
        for filt in self.normal_filters:
            # print("Testing " + name + " with " + filt.__class__.__name__)
            result = filt.test(mail)
            # print("Score of {name} calculated by {test} is {score:3.2f}".format(name=name, test=filt.__class__.__name__, score=result))
            if result != -1:
                score += result
                tests_done += 1
        return (score, tests_done)

    def test_word_filters(self, name, mail):
        score = 0
        tests_done = 0
        for filt in self.word_filters:
                # print("Testing " + name + " with " + filt.__class__.__name__)
                result = filt.test(mail)
                # print("Score of {name} calculated by {test} is {score:3.2f}".format(name=name, test=filt.__class__.__name__, score=result))
                if result != -1:
                    score += result
                    tests_done += 1
        return (score, tests_done)
                    
            
if __name__ == '__main__':
    import quality
    train_dir = '1/'
    test_dir = '2/'

    # filt = atomfilters.XSpamStatusFilter()
    # score = quality.test_atom_filter(filt, train_dir, test_dir)
    # print("Score of {name} is {score:3.2f}".format(name=filt.__class__.__name__, score=score))

    filt = MyFilter()
    filt.train(train_dir)
    filt.test(test_dir)
    # utils.show_mismatched(test_dir)
    score = quality.compute_quality_for_corpus(test_dir)
    print("Score of {name} is {score:3.2f}".format(name=filt.__class__.__name__, score=score))
