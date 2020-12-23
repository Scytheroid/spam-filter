import os
class BaseFilter:

    def train(self, dir_path):
        pass
    
    def test(self, mail):
        raise NotImplementedError("Parent filter can't be called!")

if __name__ == "__main__":
    pass