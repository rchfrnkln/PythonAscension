'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from enum import Enum

class CardType(Enum):
    HERO = 0
    MONSTER = 1
    CONSTRUCT = 2
    
class Faction(Enum):
    NONE = 0
    ENLIGHTENED = 1
    VOID = 2
    MECHANA = 3
    LIFEBOUND = 4
    
class Card:
    
    def __init__(self, name, cost, card_type, faction, honor):
        self._name = name
        self._cost = cost
        self._card_type = card_type
        self._faction = faction
        self._honor = honor
    
    def get_name(self):
        return self._name
    
    def get_cost(self):
        return self._cost
    
    def get_card_type(self):
        return self._card_type
    
    def get_faction(self):
        return self._faction

    def get_honor(self):
        return self._honor
    
    # Fat interface
    def cast(self):
        raise Exception("Can't cast.")
    
    # Fat interface
    def defeat(self):
        raise Exception("Can't defeat.")