TRUTHFILE = '!truth.txt'
PREDFILE = '!prediction.txt'

from constants import POSITIVE, NEGATIVE
from utils import read_classification_from_file, write_classification_to_file
from confmat import BinaryConfusionMatrix
from simplefilters import NaiveFilter

def quality_score(tp, tn, fp, fn):
    numerator = tp + tn
    denominator = tp + tn + 10*fp + fn
    if denominator == 0:
        return 0
    return numerator/denominator

def compute_quality_for_corpus(corpus_dir):
    truth_clasf = read_classification_from_file(corpus_dir + '/' + TRUTHFILE)
    pred_clasf = read_classification_from_file(corpus_dir + '/' + PREDFILE)

    conf_matrix = BinaryConfusionMatrix(POSITIVE, NEGATIVE)
    conf_matrix.compute_from_dicts(truth_clasf, pred_clasf)

    matrix_dict = conf_matrix.as_dict()
    
    score = quality_score(matrix_dict['tp'], \
                          matrix_dict['tn'], \
                          matrix_dict['fp'], \
                          matrix_dict['fn'])
    
    return score
    
#will be testing our filter's quality, once we create one    
def filter_quality(path):
    c = NaiveFilter()
    # path must contain directory /1 for training and /2 for testing
    c.train(path + r'/1')  
    c.test(path + r'/2')
    f_quality = compute_quality_for_corpus(path + r'/2')
    os.remove(path + r'/2/' + PREDFILE)
    return f_quality
 
    


    
