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
            
class HtmlFilter(BaseFilter):
    def __init__(self):
        self.html_in_ham = 2
        self.html_in_spam = 8
        self.mail_is_spam = 1
        self.mail_is_ham = 1

    def train(self, t_corpus):
        self.html_in_ham = 0
        self.html_in_spam = 0
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
            for word in words:
                if word.startswith('<') and word.endswith('>'):
                    if t_corpus.is_spam(name):
                        self.html_in_spam += 1
                    elif t_corpus.is_ham(name):
                        self.html_in_ham += 1

    def test(self, mail):
        found = 0
        words = []
        for word in mail.split():
            words.append(word.lower())
        for word in words:
            if word.startswith('<') and word.endswith('>'):
                '''Naive Bayes spam filtering method'''
                return (self.html_in_spam * self.mail_is_spam) / \
                (self.html_in_spam * self.mail_is_spam + self.html_in_ham \
                * self.mail_is_ham)
        return -1
        
if __name__ == "__main__":
    
    a = HtmlFilter()
    c = TrainingCorpus('./1')
    b = '<TABLE width=3D500> \
  <TBODY> \
  <TR>'
    a.train(c)
    print(a.test(b))
    