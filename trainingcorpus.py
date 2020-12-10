
from utils import read_only, read_classification_from_file
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE

class TrainingCorpus:
    def __init__(self, path_to_mails):
        self.path_to_mails = path_to_mails
        
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
    
    def spams(self):
        yield read_only(self.path_to_mails, POSITIVE)
        
    def hams(self):
        yield read_only(self.path_to_mails, NEGATIVE)
           
               
    