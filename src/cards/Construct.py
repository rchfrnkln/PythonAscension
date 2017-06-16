'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Card import Card, CardType

class Construct(Card):
    
    def __init__(self, name, cost, faction, honor):
        Card.__init__(self, name, cost, CardType.CONSTRUCT, faction, honor)
        
    def cast(self):
        return True
    
    def acquire(self):
        return