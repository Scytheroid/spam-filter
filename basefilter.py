import os

class BaseFilter:
    '''GIVES THE BASIS TO ALL FILTERS.'''
    def __init__(self):
        self.is_trained = False

    def train(self, training_corpus):
        pass
    
    def test(self, mail):
        raise NotImplementedError("Parent filter can't be called!")
        

class WordFilter(BaseFilter):
    '''DETECTS HOW GIVEN WORD INFLUENCES FILTERS PROBABILITY OF BEING A SPAM.'''
    
    # called from atomfilters.py
    def __init__(self, word):
        BaseFilter.__init__(self)
        self.word_in_spams = 0
        self.word_in_hams = 0
        self.word_total = 0
        self.word = word.lower()
        self.bayes_val = -1

    # tests how many times a word has appeared in hams and in spams, then 
    # computes by Bayes the probabilityof mail containing the word being a spam
    def train(self, t_corpus):                
        for name, email in t_corpus.emails():
            email.lower()
            if self.word in email:
                self.word_total += 1
                if t_corpus.is_spam(name):
                    self.word_in_spams += 1
                else:
                    self.word_in_hams += 1
        if self.word_total > 0:
            self.bayes_val = self.bayes()
            self.is_trained = True

    def test(self, mail):
        mail.lower()
        # Do not give any info if there is no such word or there were no such words
        if self.word in mail:
            return self.bayes_val
        else:
            return -1

    def bayes(self):
        return self.word_in_spams / (self.word_in_spams + self.word_in_hams)

if __name__ == "__main__":
    pass
