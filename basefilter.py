import os
class BaseFilter:

    def train(self, dir_path):
        pass
        #os.remove(dir_path + '/!truth.txt')
    
    def test(self, dir_path):
        raise NotImplemented_Error("Každý filtr se trénuje jinak")

if __name__ == "__main__":
    pass