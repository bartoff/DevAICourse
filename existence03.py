__author__ = 'michel'

from existence02 import Existence02
from experiment import Experiment
from result import Result
from interaction03 import Interaction03


class Existence03(Existence02):
    def __init__(self):
        e1 = self.addOrGetExperience(self.LABEL_E1)
        e2 = self.addOrGetExperience(self.LABEL_E2)
        r1 = self.createOrGetResult(self.LABEL_R1)
        r2 = self.createOrGetResult(self.LABEL_R2)
        self.addOrGetPrimitiveInteraction(e1, r1, -1)
        self.addOrGetPrimitiveInteraction(e1, r2, 1)
        self.addOrGetPrimitiveInteraction(e2, r1, -1)
        self.addOrGetPrimitiveInteraction(e2, r2, 1)
        self.enactedInteraction=None

    def step(self):
        anticipations = self.anticipate()
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

    def anticipate(self):
        anticipations=[]
        if self.getEnactedInteraction() != None:
            for activatedInteraction in self.getActivatedInteractions():
                proposedInteraction = activatedInteraction.getPostInteraction()
                anticipations.push(proposedInteraction);
                print "afforded " + proposedInteraction.toString();
                
    def getActivatedInteractions(self) :
        activatedInteractions = []
        if self.getEnactedInteraction() != None:
            for activatedInteraction in self.INTERACTIONS:
                if activatedInteraction.getPreInteraction() == self.getEnactedInteraction():
                    activatedInteractions.push(activatedInteraction)
        return activatedInteractions
    
    def setEnactedInteraction(self, enactedInteraction):
        self.enactedInteraction = enactedInteraction;
    
    def getEnactedInteraction(self):
        return self.enactedInteraction
    
