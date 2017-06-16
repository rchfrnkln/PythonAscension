'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class Mystic(Hero):
    
    NAME = "Mystic"
    COST = 3
    FACTION = Faction.NONE
    HONOR = 1
    RUNES_ADDED = 2
    
    def __init__(self):
        Hero.__init__(self, Mystic.NAME, Mystic.COST, Mystic.FACTION, Mystic.HONOR)
        
    def cast(self):
        GameManager.add_runes(Mystic.RUNES_ADDED)
        return Hero.cast(self)