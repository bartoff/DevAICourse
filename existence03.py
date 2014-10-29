__author__ = 'michel'

from existence02 import Existence02
from experiment import Experiment
from result import Result
from interaction03 import Interaction03
from anticipation03 import Anticipation03


class Existence03(Existence02):
    INTERACTIONS=list()
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
        experience = self.selectInteraction(anticipations).getExperience()
        result = self.returnResult030(experience)
        enactedInteraction = self.getInteraction(experience.getLabel() + result.getLabel())
        print "Enacted "+ enactedInteraction.__repr__()
        if enactedInteraction.getValence() >= 0:
            self.mood = 'PLEASED'
        else:
            self.mood = 'PAINED'
        
        self.learnCompositeInteraction(enactedInteraction)
        
        self.setEnactedInteraction(enactedInteraction)
        
        return self.mood

    def learnCompositeInteraction(self, interaction):
        preInteraction = self.getEnactedInteraction()
        postInteraction = interaction
        if preInteraction != None:
            self.addOrGetCompositeInteraction(preInteraction, postInteraction)

    def addOrGetCompositeInteraction(self, preInteraction, postInteraction):
        valence = preInteraction.getValence() + postInteraction.getValence()
        interaction = self.addOrGetInteraction(preInteraction.getLabel() + postInteraction.getLabel()) 
        interaction.setPreInteraction(preInteraction)
        interaction.setPostInteraction(postInteraction)
        interaction.setValence(valence)
        print "learn " + interaction.getLabel()
        return interaction
    
    def createInteraction(self, label):
        return Interaction03(label)
    
    def anticipate(self):
        anticipations=[]
        if self.getEnactedInteraction() != None:
            for activatedInteraction in self.getActivatedInteractions():
                proposedInteraction = activatedInteraction.getPostInteraction()
                anticipations.append(Anticipation03(proposedInteraction))
                print "afforded " + proposedInteraction.__repr__()
        return anticipations

    def selectInteraction(self, anticipations):
        if (len(anticipations) > 0):
            anticipations.sort(key = lambda x: x.compareTo())
            affordedInteraction = anticipations[0].getInteraction()
            if affordedInteraction.getValence() >= 0:
                intendedInteraction = affordedInteraction
            else:
                intendedInteraction = self.getOtherInteraction(affordedInteraction)
        
        else :
            intendedInteraction = self.getOtherInteraction(None)
        return intendedInteraction
           
    def getActivatedInteractions(self) :
        activatedInteractions = []
        if self.getEnactedInteraction() != None:
            for activatedInteraction in self.INTERACTIONS:
                if activatedInteraction.getPreInteraction() == self.getEnactedInteraction():
                    activatedInteractions.append(activatedInteraction)
        return activatedInteractions
    
    def getInteraction(self, label):
        try:
            ll=[a.getLabel() for a in self.INTERACTIONS]
        except:
            ll=[]
        return  self.INTERACTIONS[ll.index(label)]

    def getOtherInteraction(self, interaction):
        otherInteraction = self.INTERACTIONS[0]
        if interaction != None:
            for e in self.INTERACTIONS:
                if e.getExperience() != None and e.getExperience() != interaction.getExperience():
                    otherInteraction =  e
                    break
        return otherInteraction
    
    def setEnactedInteraction(self, enactedInteraction):
        self.enactedInteraction = enactedInteraction
    
    def getEnactedInteraction(self):
        return self.enactedInteraction
    
    def returnResult030(self, experience):
        result = None
        if self.getPreviousExperience() == experience:
            result =  self.createOrGetResult(self.LABEL_R1)
        else:
            result =  self.createOrGetResult(self.LABEL_R2)
        self.setPreviousExperience(experience)
        return result
    
    ##
    
    def addOrGetPrimitiveInteraction(self, experience, result, valence=None):
        label = experience.getLabel() + result.getLabel()
        try:
            ll=[a.getLabel() for a in self.INTERACTIONS]
        except:
            ll=[]
        if not (label in ll):
            inter03 = Interaction03(label)
            inter03.setExperience(experience)
            inter03.setResult(result)
            inter03.setValence(valence)
            self.INTERACTIONS.append(inter03)
            
        return inter03
    
    def addOrGetInteraction(self, label):
        i3=None
        try:
            ll=[a.getLabel() for a in self.INTERACTIONS]
        except:
            ll=[]
        if not (label in ll):
            i3 = Interaction03(label)
            self.INTERACTIONS.append(i3)
        else:
            i3 = self.INTERACTIONS[ll.index(label)]
        return i3
    
    def getPreviousExperience(self):
        return self.previousExperience
    
    def setPreviousExperience(self, previousExperience):
        self.previousExperience = previousExperience