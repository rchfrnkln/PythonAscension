'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
from src import GameManager

class ArhaInitiate(Hero):
    
    NAME = "Arha Initiate"
    COST = 1
    FACTION = Faction.ENLIGHTENED
    HONOR = 1
    CARDS_DRAWN = 1
    
    def __init__(self):
        Hero.__init__(self, ArhaInitiate.NAME, ArhaInitiate.COST, ArhaInitiate.FACTION, ArhaInitiate.HONOR)
        
    def cast(self):
        GameManager.draw_cards(ArhaInitiate.CARDS_DRAWN)
        return Hero.cast(self)