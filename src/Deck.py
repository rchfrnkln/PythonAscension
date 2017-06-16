'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
import random
from src.Hand import Hand

class Deck:
    
    def __init__(self, cards):
        self._deck = cards
        self._graveyard = Hand()
        self.shuffle()
        
    def draw_card(self):
        return self._deck.pop()
    
    def peek(self):
        return self._deck[0]
        
    def put_card_on_top(self, card):
        self._deck.append(card)
        
    def add_to_graveyard(self, card):
        self._graveyard.add_card(card)
        
    def shuffle(self):
        random.shuffle(self._deck)
        
    def get_size(self):
        return len(self._deck)