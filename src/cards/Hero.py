'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Card import Card, CardType

class Hero(Card):
    
    def __init__(self, name, cost, faction, honor):
        Card.__init__(self, name, cost, CardType.HERO, faction, honor)
        
    def cast(self):
        print(Card.get_name(self) + " cast.")
        return False
    
    def acquire(self):
        return