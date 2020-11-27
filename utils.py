
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

if __name__ == '__main__':
    pass