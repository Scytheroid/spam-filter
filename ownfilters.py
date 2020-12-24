from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter
from collections import Counter

class AdvertisementWordFilter(WordFilter):
    def __init__(self):
        self.word_in_spams = 0
        self.word_in_hams = 0
        self.word_total = 0

    def train(self, corpus):
        raise NotImplementedError

    def test(self, mail):
        mail.lower()
        if mail.find("advertisement") != -1:
            return self.bayes()
        else:
            return -1

    def bayes(self):
        return self.word_in_spams / (self.word_in_spams + self.word_in_hams)

    

class HasWordFilter(BaseFilter):

    # parses corpus of the email into words, turns all upper letters
    # into lower letters
    def __init__(self, email):
        words = []
        for word in email.split():
            words.append(word.lower())
        self.words = words
        self.counter = Counter(self.words)
        self.total = sum(self.counter.values())
    
    # returns how many times there is a spam word
    def occurs(self, spam_word):
        return self.counter[spam_word]
        
    def spam_words(self):
        # words that are usually in spams from 
        # www.inc.com/geoffrey-james/how-to-avoid-a-spam-filter-5-rules.html
        sp_words = ['advertisement', 'business', 'cash', 'cheap', 'commodity', \
        'congratulations', 'credit', 'deal', 'debt', 'degree', 'disclaimer', \
        'discount', 'free', 'gimmick', 'guarantee', 'income', 'ink', \
        'investment', 'joke', 'load', 'marketing', 'merchant', 'money', \
        'obligation', 'offer', 'opt', 'opportunity', 'outstanding', 'payoff', \
        'price', 'profit', 'promo', 'promotion', 'rate', 'refund', 'rich', \
        'sales', 'save', 'shop', 'spam', 'spree', 'stock', 'subscribe', \
        'trading', 'wealth', 'win', 'winner', 'winning', 'won']
        sp_words_total = 0
        for spam_word in sp_words:
            sp_words_total += self.counter[spam_word]
        return sp_words_total
        
    def test(self):
        pass
        
if __name__ == "__main__":
    email = 'ahoj jojoPOIJSDnkc  hns MONey RICH RICH s ha ahs mOney hsl'
    l = HasWordFilter(email)
    wordiis = []
    print(l.spam_words())
    
    