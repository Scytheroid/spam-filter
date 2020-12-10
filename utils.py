
from constants import POSITIVE, NEGATIVE, TRUTHFILE, PREDFILE

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
    is_ham = read_classification_from_file(rel_path + TRUTHFILE)
    for fname in is_ham.keys():
        if (is_ham[fname] == which_tag):
            with open(rel_path + fname, mode='r', encoding='utf-8') as email:
                    yield fname, email.read()          

if __name__ == '__main__':
    corpus_dir = '1'
    read_only(corpus_dir, NEGATIVE)