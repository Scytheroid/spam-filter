
import random, os
from basefilter import BaseFilter

class NaiveFilter(BaseFilter):
    def test(self, dir_path):
        f = open(dir_path + "\!prediction.txt","w+", encoding = "utf-8")
        for fname in os.listdir(dir_path):
            if not fname.startswith('!'):
                f.write(fname + " OK\n")
        f.close()

class ParanoidFilter(BaseFilter):
    def test(self, dir_path):
        f = open(dir_path + "\!prediction.txt","w+", encoding = "utf-8")
        for fname in os.listdir(dir_path):
            if not fname.startswith('!'):
                f.write(fname + " SPAM\n")
        f.close() 

class RandomFilter(BaseFilter):
    def test(self, dir_path):
        f = open(dir_path + "\!prediction.txt","w+", encoding = "utf-8")
        for fname in os.listdir(dir_path):
            if not fname.startswith('!'):
                f.write(fname + " " + random.choice(['HAM', 'SPAM']) + "\n")
        f.close()

if __name__ == "__main__":
    corpus_dir = 'C:\\Users\\ahoj7\\OneDrive\\Documents\\FEL\\rph\\spam_f\\1'
    c = RandomFilter()
    c.train(corpus_dir)
    c.test(corpus_dir)