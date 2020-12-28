
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE, POSITIVITY_THRESHOLD
from basefilter import BaseFilter
from corpus import Corpus
from trainingcorpus import TrainingCorpus
import confmat
import quality

def read_classification_from_file(path):
    classification = dict()
    with open(path, encoding='utf-8', mode='r') as reference:
        for line in reference:
            name, eval = line.split()
            classification[name] = eval
    return classification

def write_classification_to_file(clasif, path):
    with open(path, mode="w", encoding="utf-8") as file:
        for mail, result in clasif.items():
            file.write(mail + ' ' + result + '\n')
            
def read_only(corpus_dir, which_tag):
    rel_path = corpus_dir + '/'
    classif_dict = read_classification_from_file(rel_path + TRUTHFILE)
    for name, classif in classif_dict.items():
        if classif == which_tag:
            with open(rel_path + name, mode='r', encoding='utf-8') as email:
                    yield name, email.read()   

def test_atom_filter(initialized_filter, train_dir, test_dir):
    train_corp = TrainingCorpus(train_dir)
    test_corp = Corpus(test_dir)
    
    filter = initialized_filter
    filter.train(train_corp)
    prediction = dict()

    for name, mail in test_corp.emails():
        result = filter.test(mail)
        if result == -1:
            continue
        elif result > POSITIVITY_THRESHOLD:
            prediction[name] = POSITIVE
        else:
            result[name] = NEGATIVE

    truth = read_classification_from_file(test_dir + '/' + TRUTHFILE)
    conf_matrix = confmat.BinaryConfusionMatrix(POSITIVE, NEGATIVE)
    conf_matrix.compute_from_dicts(truth, prediction)

    matrix_dict = conf_matrix.as_dict()
    
    score = quality.quality_score(matrix_dict['tp'], \
                          matrix_dict['tn'], \
                          matrix_dict['fp'], \
                          matrix_dict['fn'])
    
    return score


if __name__ == '__main__':
    corpus_dir = '1'
    read_only(corpus_dir, NEGATIVE)