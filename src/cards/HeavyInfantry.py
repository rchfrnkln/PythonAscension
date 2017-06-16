'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class HeavyInfantry(Hero):
    
    NAME = "Heavy Infantry"
    COST = 2
    FACTION = Faction.NONE
    HONOR = 1
    POWER_ADDED = 2
    
    def __init__(self):
        Hero.__init__(self, HeavyInfantry.NAME, HeavyInfantry.COST, HeavyInfantry.FACTION, HeavyInfantry.HONOR)
        
    def cast(self):
        GameManager.add_power(HeavyInfantry.POWER_ADDED)
        return Hero.cast(self)