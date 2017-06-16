'''
Created on Jun 16, 2017

@author: KrzyMoose
'''
from src.cards.Hero import Hero
from src.cards.Card import Faction
import GameManager

class AsceticOfTheLidlessEye(Hero):
    
    NAME = "Ascetic of the Lidless Eyee"
    COST = 5
    FACTION = Faction.ENLIGHTENED
    HONOR = 2
    CARDS_DRAWN = 2
    
    def __init__(self):
        Hero.__init__(self, AsceticOfTheLidlessEye.NAME, AsceticOfTheLidlessEye.COST, AsceticOfTheLidlessEye.FACTION, AsceticOfTheLidlessEye.HONOR)
        
    def cast(self):
        GameManager.draw_cards(AsceticOfTheLidlessEye.CARDS_DRAWN)
        return Hero.cast(self)