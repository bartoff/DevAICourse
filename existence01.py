__author__ = 'george'

from existence import Existence
from experiment import Experiment
from result import Result
from interaction01 import Interaction01


class Existence01(Existence):
    LABEL_E1 = "e1"
    LABEL_E2 = "e2"
    LABEL_R1 = "r1"
    LABEL_R2 = "r2"
    MOODS = set(['SELF_SATISFIED', 'FRUSTRATED', 'BORED', 'PAINED', 'PLEASED'])
    mood = None
    BOREDOME_LEVEL = 4
    selfSatisfactionCounter = 0
    previousExperience = None

    EXPERIENCES = dict()
    INTERACTIONS = dict()
    RESULTS = dict()

    def __init__(self):
        e1 = self.addOrGetExperience(self.LABEL_E1)
        self.addOrGetExperience(self.LABEL_E2)
        self.previousExperience = e1


    def step(self):
        experience = self.previousExperience
        if self.mood == 'BORED':
            experience = self.getOtherExperience(experience)
            self.selfSatisfactionCounter = 0

        anticipatedResult = self.predict(experience)

        result = self.returnResult010(experience)

        self.addOrGetPrimitiveInteraction(experience, result)

        if result == anticipatedResult:
            self.mood = 'SELF_SATISFIED'
            self.selfSatisfactionCounter += 1
        else:
            self.mood = 'FRUSTRATED'
            self.selfSatisfactionCounter = 0

        if self.selfSatisfactionCounter >= self.BOREDOME_LEVEL:
            self.mood = 'BORED'

        self.previousExperience = experience

        return experience.getLabel() + result.getLabel() + " " + self.mood


    def predict(self, experience):
        pInter = None
        pResult = None

        for key, inter in self.INTERACTIONS.items():
            if inter.getExperience() == experience:
                pInter = inter

        if pInter is not None:
            pResult = pInter.getResult()

        return pResult

    def addOrGetPrimitiveInteraction(self, experience, result):
        inter = self.addOrGetInteraction(experience.getLabel() + result.getLabel())
        inter.setExperience(experience)
        inter.setResult(result)
        return inter

    def addOrGetInteraction(self, label):
        if not (label in self.INTERACTIONS):
            self.INTERACTIONS[label] = Interaction01(label)
        return self.INTERACTIONS[label]

    def createOrGetResult(self, label):
        if not (label in self.RESULTS):
            self.RESULTS[label] = Result(label)
        return self.RESULTS[label]

    def addOrGetExperience(self, label):
        if not (label in self.EXPERIENCES):
            self.EXPERIENCES[label] = Experiment(label)
        return self.EXPERIENCES[label]

    def getOtherExperience(self, experience):
        for key, exp in self.EXPERIENCES.items():
            if exp != experience:
                return exp
        return experience

    def returnResult010(self, experience):
        if experience == self.addOrGetExperience(self.LABEL_E1):
            return self.createOrGetResult(self.LABEL_R1)
        else:
            return self.createOrGetResult(self.LABEL_R2)