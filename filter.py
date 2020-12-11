import os
from constants import POSITIVE, NEGATIVE

class MyFilter:

    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
            for fname in os.listdir(dir_path):
                if not fname.startswith('!'):
                    #analyzing the file
                    result = POSITIVE
                    f.write(fname + " " + result +"\n") # result
                    
    def train(self, dir_path):
        pass
        
if __name__ == '__main__':
    corpus_dir = 'C:\\Users\\ahoj7\\OneDrive\\Documents\\FEL\\rph\\spam_projekt\\1'
    c = MyFilter()
    c.train(corpus_dir)
    c.test(corpus_dir)
            