from basefilter import WordFilter
from trainingcorpus import TrainingCorpus
import inspect
import wordfilters

c = TrainingCorpus('./1')
for name, obj in inspect.getmembers(wordfilters):
    if inspect.isclass(obj):
        if obj.__module__ == "wordfilters":
            a = obj()
            a.train(c) 
            print(name, a.bayes_val)