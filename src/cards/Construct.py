'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Card import Card, CardType

class Construct(Card):
    
    def __init__(self, name, cost, faction, honor):
        Card.__init__(self, name, cost, CardType.CONSTRUCT, faction, honor)
        self._tapped = False
        
    def cast(self):
        return True
    
    def acquire(self):
        return
    
    def tap(self):
        if(self._tapped == True):
            raise Exception(self.get_name() + " already used.")
        self._tapped = True
        return True
    
    def untap(self):
        self._tapped = False