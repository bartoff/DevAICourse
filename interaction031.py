__author__ = 'michel'

from interaction03 import Interaction03
from experiment import Experiment

class Interaction031(Interaction03):
    weight = 0
    def __init__(self, label):
        Interaction03.__init__(self,label)
        
    def getWeight(self):
        return self.weight

    def incrementWeight(self):
        self.weight +=1
        
    def __repr__(self):
        return "{0}, valence {1}, weight {2}".format(self.getLabel(),self.getValence(),self.getWeight())