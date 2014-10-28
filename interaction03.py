__author__ = 'michel'

from interaction01 import Interaction01
from experiment import Experiment
from result import Result


class Interaction03(Interaction01):
    valence = 0.0
    preInteraction=None
    postInteraction=None
    
    def __init__(self, label):
        Interaction01.__init__(self, label)

    def getValence(self):
        return self.valence

    def setValence(self, valence):
        self.valence = valence
        
    def getPreInteraction(self):
        return self.preInteraction
        
    def setPreInteraction(self,preInteraction):
        self.preInteraction = preInteraction
        
    def getPostInteraction(self):
        return self.postInteraction
        
    def setPostInteraction(self,postInteraction):
        self.postInteraction = postInteraction

    def isPrimitive(self):
        return self.preInteraction==None
    
    def __repr__(self):
        return self.getLabel() + ',' + self.getValence()