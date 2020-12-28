from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter, WordFilter
from collections import Counter
from corpus import Corpus
from trainingcorpus import TrainingCorpus
import email.message

class BlacklistFilter(BaseFilter):
    def __init__(self):
        BaseFilter.__init__(self)
        self.blacklist = set()

    def train(self, training_corpus):
        for fname, mail in training_corpus.spams():
            from_header = email.message_from_string(mail).get('From').split(' ')
            self.blacklist.add(from_header[-1])
    
    def test(self, mail):
        from_header = email.message_from_string(mail).get('From').split(' ')
        suspicious_address = from_header[-1]
        if suspicious_address in self.blacklist:
            return 1    # Positive
        else:
            return -1    # Can't tell

        
if __name__ == "__main__":
    
    a = WonFilter()
    c = TrainingCorpus('./1')
    a.train(c)
    print(a.word_in_hams)
    print(a.word_in_spams)
    