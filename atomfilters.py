from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter, WordFilter
from collections import Counter
from corpus import Corpus
from trainingcorpus import TrainingCorpus
import email.message

class BlacklistFilter(BaseFilter):
    '''DETECTS MAIL ADRESSES THAT USUALLY SEND SPAMS.'''
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
    '''DETECTS MAIL ADRESSES THAT USUALLY SEND HAMS.'''
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
    '''DETECTS WHETER BODY CONTAINS HTML TAGS.'''
    def __init__(self):
        # default parameters, in case we didn't call the train function
        self.html_in_ham = 2
        self.html_in_spam = 8
        self.bayes = 0.86
        
    def return_body(self, mail):
        body = email.message_from_string(mail).get_payload()
        return body

    def train(self, t_corpus):
        self.html_in_ham = 0
        self.html_in_spam = 0
        for name, mail in t_corpus.emails():
            body = self.return_body(mail)
            for word in body.split():
                # html tags are simplyfied, no plain text includes <word>
                if word.startswith('<') and word.endswith('>'):
                    if t_corpus.is_spam(name):
                        self.html_in_spam += 1
                    elif t_corpus.is_ham(name):
                        self.html_in_ham += 1
        if self.html_in_ham + self.html_in_spam > 0:
            self.is_trained = True
            self.bayes = self.html_in_spam / (self.html_in_spam + self.html_in_ham)

    def test(self, mail):
        body = self.return_body(mail)
        for word in body.split():
            if word.startswith('<') and word.endswith('>'):
                return self.bayes
        return -1
        
class ReplyFilter(BaseFilter):
    '''FINDS MAILS THAT ARE REPLYS TO OUR MAIL.'''
    def __init__(self):
        # default parameters, in case we didn't call the train function
        self.reply_in_ham = 0
        self.reply_in_spam = 0
        self.bayes = 0.0
        
    def return_header(self, mail, seperator):
        parts = []
        for part in mail.split('\n\n'):
            parts.append(part)
        return parts[0]

    def train(self, t_corpus):
        for name, mail in t_corpus.emails():
            separator = ' '
            header = self.return_header(mail, separator)
            if header.find("In-Reply-To") != -1:
                if t_corpus.is_spam(name):
                    self.reply_in_spam += 1
                elif t_corpus.is_ham(name):
                    self.reply_in_ham += 1
        self.bayes = self.reply_in_spam / (self.reply_in_spam + self.reply_in_ham)

    def test(self, mail):
        separator = ' '
        header = self.return_header(mail, separator)
        if header.find("In-Reply-To") != -1:
            return self.bayes
        else:
            return -1
            
class SusReplyFilter(BaseFilter):
    '''DETECTS MAILS PRETENDING TO BE A REPLY.'''
    def __init__(self):
        # default parameters, in case we didn't call the train function
        self.sus_reply_in_ham = 0
        self.sus_reply_in_spam = 0
        self.sus_bayes = 0.92
        
    def return_header(self, mail, seperator):
        parts = []
        for part in mail.split('\n\n'):
            parts.append(part)
        return parts[0]

    def train(self, t_corpus):
        for name, mail in t_corpus.emails():
            separator = ' '
            header = self.return_header(mail, separator)
                # sorts out mails that genuinely are replys
            if header.find("In-Reply-To") != -1:
                pass
                # finds mails pretending to be a reply
            elif header.find("Reply-To") != -1:
                if t_corpus.is_spam(name):
                    self.sus_reply_in_spam += 1
                elif t_corpus.is_ham(name):
                    self.sus_reply_in_ham += 1
        self.sus_bayes = self.sus_reply_in_spam / \
            (self.sus_reply_in_spam + self.sus_reply_in_ham)

    def test(self, mail):
        separator = ' '
        header = self.return_header(mail, separator)
        if header.find("In-Reply-To") != -1:
            return -1
        elif header.find("Reply-To") != -1:
            return self.sus_bayes
        else:
            return -1
        
if __name__ == "__main__":
    
    a = SusReplyFilter()
    c = TrainingCorpus('./1')
    a.train(c)
    