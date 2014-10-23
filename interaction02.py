__author__ = 'george'

from interaction01 import Interaction01
from experiment import Experiment
from result import Result


class Interaction02(Interaction01):
    valence = 0.0

    def __init__(self, label, valence=0.0):
        Interaction01.__init__(self, label)
        self.valence = valence

    def getValence(self):
        return self.valence

    def setValence(self, valence):
        self.valence = valence

    def __repr__(self):
        return self.getLabel() + ',' + self.getValence()