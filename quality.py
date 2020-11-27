POSITIVE = "SPAM"
NEGATIVE = "OK"

TRUTHFILE = '!truth.txt'
PREDFILE = '!prediction.txt'

from utils import read_classification_from_file, write_classification_to_file
from confmat import BinaryConfusionMatrix

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


    
