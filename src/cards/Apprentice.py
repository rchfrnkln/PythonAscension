'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Card import Faction
from src.cards.Hero import Hero
from src import GameManager

class Apprentice(Hero):
    
    NAME = "Apprentice"
    COST = 0
    FACTION = Faction.NONE
    HONOR = 0
    RUNES_ADDED = 1
    
    def __init__(self):
        Hero.__init__(self, Apprentice.NAME, Apprentice.COST, Apprentice.FACTION, Apprentice.HONOR)
        
    def cast(self):
        GameManager.add_power(Apprentice.RUNES_ADDED)
        return Hero.cast(self)