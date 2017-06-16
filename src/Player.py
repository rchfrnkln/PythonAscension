'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
import DeckFactory
from Hand import Hand

class Player:
    
    def __init__(self, name):
        self._name = name
        self._current_power = 0;
        self._current_runes = 0;
        self._deck = DeckFactory.build_player_deck()
        self._hand = Hand()
    
    def add_power(self, power):
        self._current_power += power
        print(self.get_name() + " now has " + str(self._current_power) + " power.")
        
    def add_runes(self, runes):
        self._current_runes += runes
        print(self.get_name() + " now has " + str(self._current_runes) + " runes.")
        
    def draw_card(self):
        card = self._deck.draw_card()
        self._hand.add_card(card)
        print(self.get_name() + " now has " + str(self._hand.get_size()) + " cards in hand.")
    
    def get_name(self):
        return self._name
    
    def end_turn(self):
        self._current_power = 0;
        self._current_runes = 0;
        
    def __str__(self):
        return "Player %s" % (self._name)