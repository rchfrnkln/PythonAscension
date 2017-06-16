'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Monster import Monster

class Cultist(Monster):
    
    NAME = "Cultist"
    COST = 2
    HONOR = 1
    
    def __init__(self):
        Monster.__init__(self, Cultist.NAME, Cultist.COST, Cultist.HONOR)
        
    def defeat(self):
        return Monster.defeat(self)