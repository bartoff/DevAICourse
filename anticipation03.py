__author__ = 'michel'

from interaction03 import Interaction03

class Anticipation03():
    interaction=None
    def __init__(self, interaction):
        self.interaction = interaction
        
    def getInteraction(self):
        return self.interaction
    
    def compareTo(self):
        return self.interaction.getValence()