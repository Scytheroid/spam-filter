from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter
from collections import Counter

class HasWordFilter(BaseFilter):
    def test(self, email, the_word):
        emails = email.split()
        occurance = Counter(emails)
        print(occurance)
        for word in email:
            word.lower()
            occurance[word] += 1
        if occurance[the_word]:
            return 1
        return 0
        
if __name__ == "__main__":
    l = HasWordFilter()
    email = 'ahoj jojofnkc  hns s ha ahs money hsl'
    print(l.test(email, 'money'))


    