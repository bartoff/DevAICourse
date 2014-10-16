__author__ = 'george'

from interaction import Interaction
from experiment import Experiment
from result import Result


class Interaction01(Interaction):
    def __init__(self, label):
        self.experience = None
        self.result = None
        self.label = label

    def getLabel(self):
        return self.label

    def getExperience(self):
        return self.experience

    def getResult(self):
        return self.result

    def setExperience(self, experience):
        self.experience = experience
        return

    def setResult(self, result):
        self.result = result
        return

    def __repr__(self):
        return self.experience.getLabel() + self.result.getLabel()