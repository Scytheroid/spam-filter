import os
class BaseFilter:

    def train(self, dir_path):
        raise NotImplementedError("Parent filter can't be trained!")
    
    def test(self, dir_path):
        raise NotImplementedError("Parent filter can't be called!")

if __name__ == "__main__":
    pass