import random, os
from constants import POSITIVE, NEGATIVE
from basefilter import BaseFilter

class NaiveFilter():
    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
          for fname in os.listdir(dir_path):
              if not fname.startswith('!'):
                  f.write(fname + " OK\n")

class ParanoidFilter():
    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
            for fname in os.listdir(dir_path):
                if not fname.startswith('!'):
                    f.write(fname + " SPAM\n")

class RandomFilter():
    def test(self, dir_path):
        with open(dir_path + "/!prediction.txt","w+", encoding = "utf-8") as f:
            for fname in os.listdir(dir_path):
                if not fname.startswith('!'):
                    f.write(fname + " " + random.choice([POSITIVE, NEGATIVE]) + "\n")
           
