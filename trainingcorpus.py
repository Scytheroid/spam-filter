from corpus import Corpus
from utils import read_only, read_classification_from_file
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE

class TrainingCorpus(Corpus):
    '''HELPS US WITH TRAINING FILTERS.'''
    def __init__(self, path_to_mails):
        Corpus.__init__(self, path_to_mails)
        
    def is_tag(self, ename, whichtag):
        rel_path = self.path_to_mails + '/'
        is_ham = read_classification_from_file(rel_path + TRUTHFILE)
        if (is_ham[ename] == whichtag):
            return True
        else:
            return False        
            
    def get_class(self, ename):
        if (self.is_tag(ename, NEGATIVE) == True):
            return NEGATIVE
        else:
            return POSITIVE 
        
    def is_ham(self, ename):
        return self.is_tag(ename, NEGATIVE)
                 
    def is_spam(self, ename):
        return self.is_tag(ename, POSITIVE) 
    
    def hams(self):
        hams_only = read_only(self.path_to_mails, NEGATIVE)
        for ham in hams_only:
            yield ham           # Returns filename and mail contents
           
    def spams(self):
        spams_only = read_only(self.path_to_mails, POSITIVE)
        for spam in spams_only:
            yield spam          # Returns filename and mail contents
        