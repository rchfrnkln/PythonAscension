'''
Created on Jun 16, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class ArbiterOfThePrecipice(Hero):
    
    NAME = "Arbiter of the Precipice"
    COST = 4
    FACTION = Faction.VOID
    HONOR = 1
    CARDS_DRAWN = 2
    CARDS_BANISHED = 1
    
    def __init__(self):
        Hero.__init__(self, ArbiterOfThePrecipice.NAME, ArbiterOfThePrecipice.COST, ArbiterOfThePrecipice.FACTION, ArbiterOfThePrecipice.HONOR)
        
    def cast(self):
        GameManager.draw_cards(ArbiterOfThePrecipice.CARDS_DRAWN)
        GameManager.banish_cards_from_hand(ArbiterOfThePrecipice.CARDS_BANISHED)
        return Hero.cast(self)