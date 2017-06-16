'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Card import Card, CardType, Faction

class Monster(Card):
    
    def __init__(self, name, cost, honor):
        Card.__init__(name, cost, CardType.MONSTER, Faction.NONE, honor)
        
    def defeat(self):
        print(Card.get_name(self) + " defeated.")
        return Card.get_honor(self)