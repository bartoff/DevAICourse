__author__ = 'george'

from existence01 import Existence01
from experiment import Experiment
from result import Result
from interaction02 import Interaction02


class Existence02(Existence01):
    def __init__(self):
        e1 = self.addOrGetExperience(self.LABEL_E1)
        e2 = self.addOrGetExperience(self.LABEL_E2)
        r1 = self.createOrGetResult(self.LABEL_R1)
        r2 = self.createOrGetResult(self.LABEL_R2)
        self.addOrGetPrimitiveInteraction(e1, r1, -1)
        self.addOrGetPrimitiveInteraction(e1, r2, 1)
        self.addOrGetPrimitiveInteraction(e2, r1, -1)
        self.addOrGetPrimitiveInteraction(e2, r2, 1)
        self.previousExperience = e1

    def step(self):
        experience = self.previousExperience
        if self.mood == 'PAINED':
            experience = self.getOtherExperience(experience)

        result = self.returnResult010(experience)

        enactedInteraction = self.addOrGetPrimitiveInteraction(experience, result)

        if enactedInteraction.getValence() > 0:
            self.mood = 'PLEASED'
        else:
            self.mood = 'PAINED'

        self.previousExperience = experience

        return experience.getLabel() + result.getLabel() + " " + self.mood


    def addOrGetPrimitiveInteraction(self, experience, result, valence=None):
        label = experience.getLabel() + result.getLabel()
        if not (label in self.INTERACTIONS):
            inter02 = Interaction02(label)
            inter02.setExperience(experience)
            inter02.setResult(result)
            inter02.setValence(valence)
            self.INTERACTIONS[label] = inter02
        return self.INTERACTIONS[label]

    def addOrGetInteraction(self, label):
        return None


