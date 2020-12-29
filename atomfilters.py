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
        BaseFilter.__init__(self)
        # This is only used if filter not trained
        self.bayes_val = 0.86
        
    def return_body(self, mail):
        body = email.message_from_string(mail).get_payload()
        return body

    def train(self, t_corpus):
        for name, mail in t_corpus.emails():
            body = self.return_body(mail)
            for word in body.split():
                # html tags are simplyfied, no plain text includes <word>
                if word.startswith('<') and word.endswith('>'):
                    if t_corpus.is_ham(name):
                        self.in_hams += 1
                    elif t_corpus.is_ham(name):
                        self.in_spams += 1
        self.bayes()

    def test(self, mail):
        body = self.return_body(mail)
        for word in body.split():
            if word.startswith('<') and word.endswith('>'):
                return self.bayes_val
        return -1
        
class ReplyFilter(BaseFilter):
    '''FINDS MAILS THAT ARE REPLYS TO OUR MAIL.'''
    def __init__(self):
        BaseFilter.__init__(self)
        # This is only used if filter not trained
        self.bayes_val = 0

    def train(self, t_corpus):
        for fname, mail in t_corpus.emails():
            mesg = email.message_from_string(mail)
            if mesg.get('In-Reply-To'):
                if t_corpus.is_ham(fname):
                    self.in_hams += 1
                else:
                    self.in_spams += 1
        self.bayes()

    def test(self, mail):
        mesg = email.message_from_string(mail)
        if mesg.get('In-Reply-To'):
            return self.bayes_val
        else:
            return -1
            
class SusReplyFilter(BaseFilter):
    '''DETECTS MAILS PRETENDING TO BE A REPLY.'''
    def __init__(self):
        BaseFilter.__init__(self)
        # This is only used if filter not trained
        self.bayes_val = 0.92

    def train(self, t_corpus):
        for fname, mail in t_corpus.emails():
            mesg = email.message_from_string(mail)
            if mesg.get('Reply-To') and not mesg.get('In-Reply-To'):
                if t_corpus.is_ham(fname):
                    self.in_hams += 1
                else:
                    self.in_spams += 1
        self.bayes()

    def test(self, mail):
        mesg = email.message_from_string(mail)
        if mesg.get('Reply-To') and not mesg.get('In-Reply-To'):
            return self.bayes_val
        else:
            return -1

class XSpamStatusFilter(BaseFilter):
    def __init__(self):
        BaseFilter.__init__(self)
        self.bayes_val = 0
        
    def train(self, training_corpus):
        for fname, mail in training_corpus.emails():
            XSS_header = email.message_from_string(mail).get('X-Spam-Status')
            if XSS_header != None:
                if XSS_header.split(', ')[0] == 'No':
                    if training_corpus.is_ham(fname):
                        self.in_hams += 1
                    else:
                        self.in_spams += 1
        self.bayes()

    def test(self, mail):
        XSS_header = email.message_from_string(mail).get('X-Spam-Status')
        if XSS_header != None:
                if XSS_header.split(', ')[0] == 'No':
                    return self.bayes_val
        return -1
        
if __name__ == "__main__":
    
    a = SusReplyFilter()
    c = TrainingCorpus('./1')
    a.train(c)
    