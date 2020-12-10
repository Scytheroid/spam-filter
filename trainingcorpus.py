from utils import read_only, read_classification_from_file
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE

class TrainingCorpus:
    def __init__(self, path_to_mails):
        self.path_to_mails = path_to_mails
        
    def get_class(self, ename):
        rel_path = self.path_to_mails + '/'
        is_ham = read_classification_from_file(rel_path + TRUTHFILE)
        if (is_ham[ename] == NEGATIVE):
            return NEGATIVE
        else:
            return POSITIVE 
        
    def is_ham(self, ename):
        rel_path = self.path_to_mails + '/'
        is_ham = read_classification_from_file(rel_path + TRUTHFILE)
        if (is_ham[ename] == NEGATIVE):
            return True
        else:
            return False     
                 
    def is_spam(self, ename):
        rel_path = self.path_to_mails + '/'
        is_ham = read_classification_from_file(rel_path + TRUTHFILE)
        if (is_ham[ename] == POSITIVE):
            return True
        else:
            return False 
    
    def spams(self):
        yield read_only(self.path_to_mails, POSITIVE)
        
    def hams(self):
        yield read_only(self.path_to_mails, NEGATIVE)
               
    