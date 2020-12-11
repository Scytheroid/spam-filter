import os
from constants import POSITIVE, NEGATIVE

class MyFilter:
    def __init__(self):
        self.filter_importance = 2
        # initializing importance of our filters in case they don't let us
        # train them

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
    c = MyFilter()
    c.train(corpus_dir)
    c.test(corpus_dir)
            