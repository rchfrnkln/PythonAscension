'''
Created on Jun 19, 2017

@author: user
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class ArhaTemplar(Hero):
    
    NAME = "Arha Templar"
    COST = 4
    FACTION = Faction.ENLIGHTENED
    HONOR = 3
    MAX_POWER = 4
    
    def __init__(self):
        Hero.__init__(self, ArhaTemplar.NAME, ArhaTemplar.COST, ArhaTemplar.FACTION, ArhaTemplar.HONOR)
        
    def cast(self):
        GameManager.defeat_monster_with_cost(ArhaTemplar.MAX_POWER)
        return Hero.cast(self)