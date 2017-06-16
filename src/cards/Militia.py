'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class Militia(Hero):
    
    NAME = "Militia"
    COST = 0
    FACTION = Faction.NONE
    HONOR = 0
    POWER_ADDED = 1
    
    def __init__(self):
        Hero.__init__(self, Militia.NAME, Militia.COST, Militia.FACTION, Militia.HONOR)
        
    def cast(self):
        GameManager.add_power(Militia.POWER_ADDED)
        return Hero.cast(self)