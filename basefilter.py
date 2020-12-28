import os
from collections import Counter

class BaseFilter:

    def train(self, training_corpus):
        pass
    
    def test(self, mail):
        raise NotImplementedError("Parent filter can't be called!")
        
    # tests how many times a word has appeared in hams and in spams, then 
    # computes by Bayes the probabilityof mail containing the word being a spam
    # called from ownfilters.py
class WordFilter(BaseFilter):
    def __init__(self, word):
        self.word_in_spams = 0
        self.word_in_hams = 0
        self.word_total = 0
        self.word = word
        self.mail_is_spam = 1
        self.mail_is_ham = 1

    def train(self, t_corpus):
        if self.mail_is_spam == 1:
            for name, email in t_corpus.emails():
                if t_corpus.is_spam(name):
                    self.mail_is_spam += 1
                else:
                    self.mail_is_ham += 1                   
        for name, email in t_corpus.emails():
            words = []
            for word in email.split():
                words.append(word.lower())
            counter = Counter(words)
            total_in_mail = counter[self.word]
            if t_corpus.is_spam(name):
                self.word_in_spams += total_in_mail
            elif t_corpus.is_ham(name):
                self.word_in_hams += total_in_mail
            else:
                print("isn't a name of email")

    def test(self, mail):
        mail.lower()
        if mail.find(self.word) != -1:
            self.word_total = self.word_in_hams + self.word_in_spams
            return self.bayes()
        else:
            return -1

    def bayes(self):
        '''Naive Bayes spam filtering method'''
        return (self.word_in_spams * self.mail_is_spam) / \
        (self.word_in_spams * self.mail_is_spam + self.word_in_hams * self.mail_is_ham)

if __name__ == "__main__":
    pass
