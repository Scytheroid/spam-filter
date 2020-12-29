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

class WhitelistFilter(BaseFilter):
    def __init__(self):
        BaseFilter.__init__(self)
        self.whitelist = set()

    def train(self, training_corpus):
        for fname, mail in training_corpus.hams():
            from_header = email.message_from_string(mail).get('From').split(' ')
            self.whitelist.add(from_header[-1])

    def test(self, mail):
        from_header = email.message_from_string(mail).get('From').split(' ')
        suspicious_address = from_header[-1]
        if suspicious_address in self.whitelist:
            return 0    # Negative
        else:
            return -1    # Can't tell

class HtmlFilter(BaseFilter):
    def __init__(self):
        # default parameters, in case we didn't call the train function
        self.html_in_ham = 2
        self.html_in_spam = 8
        self.bayes = 0.86
        
    def return_body(self, mail, seperator):
        body = email.message_from_string(mail).get_payload()
        return body

    def train(self, t_corpus):
        self.html_in_ham = 0
        self.html_in_spam = 0
        for name, mail in t_corpus.emails():
            separator = ' '
            body = self.return_body(mail, separator)
            for word in body.split():
                if word.startswith('<') and word.endswith('>'):
                    if t_corpus.is_spam(name):
                        self.html_in_spam += 1
                    elif t_corpus.is_ham(name):
                        self.html_in_ham += 1
        self.bayes = self.html_in_spam / (self.html_in_spam + self.html_in_ham)

    def test(self, mail):
        separator = ' '
        body = self.return_body(mail, separator)
        for word in body.split():
            if word.startswith('<') and word.endswith('>'):
                return self.bayes
        return -1
        
if __name__ == "__main__":
    
    a = HtmlFilter()
    c = TrainingCorpus('./1')
    a.train(c)
    print(a.html_in_ham)
    print(a.html_in_spam)
    