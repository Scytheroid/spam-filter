import os
import inspect

from constants import POSITIVE, NEGATIVE, POSITIVITY_THRESHOLD
from corpus import Corpus
import ownfilters
import utils

class MyFilter:
    def __init__(self):
        # self.filter_importance = 2
        # initializing importance of our filters in case they don't let us
        # train them
        self.filters = []
        self.init_filters()

    def init_filters(self):
        for name, obj in inspect.getmembers(ownfilters):
            if inspect.isclass(obj):
                if obj.__module__ == "ownfilters":
                    print("Initializing " + name)
                    filt = obj.__init__(obj)
                    self.filters.append(filt)
    
    def train(self, dir_path):
        corpus = Corpus(dir_path)

        for filt in self.filters:
            print("Training " + filt.__name__)
            filt.train(corpus)

    def test(self, dir_path):
        corpus = Corpus(dir_path)
        clasif = dict()
        
        for name, mail in corpus.emails():
            score = 0

            for filt in self.filters:
                print("Testing " + name + " with " + filt.__name__)
                result = filt.test(mail)
                print("Result is: " + result)
                score += result
            score /= len(self.filters)

            if score > POSITIVITY_THRESHOLD:
                clasif[name] = POSITIVE
            else:
                clasif[name] = NEGATIVE        
        utils.write_classification_to_file(clasif, dir_path + "/!prediction.txt")
                    
            
if __name__ == '__main__':
    filt = MyFilter()
    corpus_dir = '2/'
    filt.train(corpus_dir)
            