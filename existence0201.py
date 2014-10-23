__author__ = 'george'

from existence02 import Existence02
from experiment import Experiment
from result import Result
from interaction02 import Interaction02


class Existence0201(Existence02):
    def __init__(self):
        Existence02.__init__(self)
        self.selfSatisfactionCounter = 0

    def step(self):
        experience = self.previousExperience

        if (self.mood == 'PAINED') or (self.mood == 'BORED'):
            experience = self.getOtherExperience(experience)

        result = self.returnResult010(experience)
        enactedInteraction = self.addOrGetPrimitiveInteraction(experience, result)

        if 0 < self.valencePerception(enactedInteraction.getValence()) < 0.3:
            self.mood = 'BORED'
            self.selfSatisfactionCounter = 0

        elif 0.3 < self.valencePerception(enactedInteraction.getValence()):
            self.mood = 'PLEASED'
            self.selfSatisfactionCounter += 1

        else:
            self.mood = 'PAINED'
            self.selfSatisfactionCounter = 0

        self.previousExperience = experience

        return experience.getLabel() + result.getLabel() + " " + self.mood

    def valencePerception(self, valence):
        return float(valence) / float(self.selfSatisfactionCounter + 1)
