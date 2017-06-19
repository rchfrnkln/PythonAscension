'''
Created on Jun 19, 2017

@author: user
'''

from src.cards.Construct import Construct
from src.cards.Card import Faction
import GameManager

class Muramasa(Construct):
    
    NAME = "Muramasa"
    COST = 7
    FACTION = Faction.NONE
    HONOR = 4
    POWER_ADDED = 3
    
    def __init__(self):
        Construct.__init__(self, Muramasa.NAME, Muramasa.COST, Muramasa.FACTION, Muramasa.HONOR)
    
    def tap(self):
        Construct.tap(self)
        GameManager.add_power(Muramasa.POWER_ADDED)