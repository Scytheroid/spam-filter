
import random, os
from basefilter import BaseFilter

class NaiveFilter(BaseFilter):
    def test(self, dir_path):
        with open(dir_path + r"/!prediction.txt","w+", encoding = "utf-8") as f:
          for fname in os.listdir(dir_path):
              if not fname.startswith('!'):
                  f.write(fname + " OK\n")

class ParanoidFilter(BaseFilter):
    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
            for fname in os.listdir(dir_path):
                if not fname.startswith('!'):
                    f.write(fname + " SPAM\n")

class RandomFilter(BaseFilter):
    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
            for fname in os.listdir(dir_path):
                if not fname.startswith('!'):
                    f.write(fname + " " + random.choice(['HAM', 'SPAM']) + "\n")
           
