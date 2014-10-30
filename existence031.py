__author__ = 'michel'

from existence03 import Existence03
from interaction031 import Interaction031
from anticipation031 import Anticipation031

class Existence031(Existence03):
    INTERACTIONS=list()
    T1=8
    T2=15
    clock=0
    def __init__(self):
        Existence03.__init__(self)

    def step(self):
        
        anticipations = self.anticipate()
        experience = self.selectExperience(anticipations)
        #result = self.returnResult030(experience)
        result = self.returnResult031(experience)
        
        enactedInteraction = self.getInteraction(experience.getLabel() + result.getLabel())
        print "Enacted "+ enactedInteraction.__repr__()
        if enactedInteraction.getValence() >= 0:
            self.mood = 'PLEASED'
        else:
            self.mood = 'PAINED'
        
        self.learnCompositeInteraction(enactedInteraction)
        
        self.setEnactedInteraction(enactedInteraction)
        
        return self.mood

    def learnCompositeInteraction(self, enactedInteraction):
        preInteraction = self.getEnactedInteraction()
        postInteraction = enactedInteraction
        if preInteraction != None:
            interaction = self.addOrGetCompositeInteraction(preInteraction, postInteraction)
            interaction.incrementWeight()
    
    def createInteraction(self, label):
        return Interaction031(label)
    
    def anticipate(self):
        anticipations=self.getDefaultAnticipations()
        if self.getEnactedInteraction() != None:
            for activatedInteraction in self.getActivatedInteractions():
                proposition = Anticipation031(activatedInteraction.getPostInteraction().getExperience(),activatedInteraction.getWeight()*activatedInteraction.getPostInteraction().getValence())
                idx = [ a.getExperience().getLabel()==proposition.getExperience().getLabel() for a in anticipations]
                try:
                    index = idx.index(True)
                    anticipations[index].addProclivity(activatedInteraction.getWeight()*activatedInteraction.getPostInteraction().getValence())
                except:
                    anticipations.append(proposition)
        return anticipations

    def getDefaultAnticipations(self):
        anticipations = []
        for k, experience in self.EXPERIENCES.iteritems():
            anticipation = Anticipation031(experience, 0)
            anticipations.append(anticipation)
        return anticipations
    

    def selectExperience(self, anticipations):
        if (len(anticipations) > 0):
            anticipations.sort(key = lambda x: x.compareTo(), reverse=True)
            for anticipation in anticipations:
                print "propose "+anticipation.__repr__()
        selectedAnticipation = anticipations[0]
        return selectedAnticipation.getExperience()
         
    def getInteraction(self, label):
        try:
            ll=[a.getLabel() for a in self.INTERACTIONS]
            r = self.INTERACTIONS[ll.index(label)]
        except:
            ll=[]
            r = None
        return  r
    
    #Environment031
    
    def getClock(self):
        return self.clock
    
    def incClock(self):
        self.clock+=1
        
    def returnResult031(self,experience):

        self.incClock()
        if self.getClock() <= self.T1 or self.getClock() > self.T2:
            if experience == self.addOrGetExperience(self.LABEL_E1):
                result =  self.createOrGetResult(self.LABEL_R1)
            else:
                result = self.createOrGetResult(self.LABEL_R2)
        
        else :
            if experience == self.addOrGetExperience(self.LABEL_E1):
                result = self.createOrGetResult(self.LABEL_R2)
            else:
                result = self.createOrGetResult(self.LABEL_R1)
        
        return result
    ##
    
    def addOrGetPrimitiveInteraction(self, experience, result, valence=None):
        label = experience.getLabel() + result.getLabel()
        try:
            ll=[a.getLabel() for a in self.INTERACTIONS]
        except:
            ll=[]
        if not (label in ll):
            inter03 = Interaction031(label)
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
            i3 = Interaction031(label)
            self.INTERACTIONS.append(i3)
        else:
            i3 = self.INTERACTIONS[ll.index(label)]
        return i3
