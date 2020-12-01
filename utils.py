
POSITIVE = "SPAM"
NEGATIVE = "OK"
TRUTHFILE = '!truth.txt'
PREDFILE = '!prediction.txt'

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
            
def read_only(corpus_dir, pos_or_neg_tag):
    is_ham = read_classification_from_file(corpus_dir + '/' + TRUTHFILE)
    for fname in is_ham.keys():
        if (is_ham[fname] == pos_or_neg_tag):
            path_to_file = corpus_dir + '/' + fname
            with open(path_to_file, mode='r', encoding='utf-8') as email:
                    print(fname, email.read())            

if __name__ == '__main__':
    corpus_dir = 'C:\\Users\\ahoj7\\OneDrive\\Documents\\FEL\\rph\\spam_projekt\\1'
    read_only(corpus_dir, NEGATIVE)
    pass