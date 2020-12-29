
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE, POSITIVITY_THRESHOLD

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

def show_mismatched(corpus_dir):
    rel_path = corpus_dir + '/'
    truth_dict = read_classification_from_file(rel_path + TRUTHFILE)
    pred_dict = read_classification_from_file(rel_path + PREDFILE)
    for name, classif in truth_dict.items():
        if classif != pred_dict[name]:
            print("Mismatch found in file {}!".format(name))
            print("Should be {} but {} is predicted.\n".format(classif, pred_dict[name]))
            with open(rel_path + name, mode='r', encoding='utf-8') as email:
                print(email.read())
            print("\n")
        input()

if __name__ == '__main__':
    corpus_dir = '1'
    read_only(corpus_dir, NEGATIVE)