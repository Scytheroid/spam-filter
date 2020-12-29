import os

class BaseFilter:
    '''GIVES THE BASIS TO ALL FILTERS.'''
    def __init__(self):
        self.bayes_val = -1
        self.in_hams = 0
        self.in_spams = 0

    def train(self, training_corpus):
        pass
    
    def test(self, mail):
        raise NotImplementedError("Parent filter can't be called!")

    def bayes(self):
        if self.in_hams + self.in_spams > 0:
            self.bayes_val = self.in_spams / (self.in_spams + self.in_hams)
        

class WordFilter(BaseFilter):
    '''DETECTS HOW GIVEN WORD INFLUENCES FILTERS PROBABILITY OF BEING A SPAM.'''
    
    # called from atomfilters.py
    def __init__(self, word):
        BaseFilter.__init__(self)
        self.word = word.lower()

    # tests how many times a word has appeared in hams and in spams, then 
    # computes by Bayes the probabilityof mail containing the word being a spam
    def train(self, t_corpus):                
        for name, email in t_corpus.emails():
            email.lower()
            if self.word in email:
                if t_corpus.is_ham(name):
                    self.in_hams += 1
                else:
                    self.in_spams += 1
        self.bayes()

    def test(self, mail):
        mail.lower()
        # Do not give any info if there is no such word
        # or there were no such words during training
        if self.word in mail:
            return self.bayes_val
        else:
            return -1

if __name__ == "__main__":
    pass
