'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
import random
from Hand import Hand

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
        self._deck.insert(0, card)
        
    def add_to_graveyard(self, card):
        self._graveyard.add_card(card)
        
    def shuffle(self):
        random.shuffle(self._deck)
        
    def shuffle_graveyard_into_deck(self):
        while(self._graveyard.get_size() != 0):
            self._deck.append(self._graveyard.remove_card(0))
        self.shuffle()
        
    def get_size(self):
        return len(self._deck)