'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
import DeckFactory
from Hand import Hand

class Player:
    
    def __init__(self, name):
        self._name = name
        self._current_power = 0
        self._current_runes = 0
        self._honor = 0
        self._deck = DeckFactory.build_player_deck()
        self._hand = Hand()
        self.end_turn()
    
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
    
    def get_honor(self):
        return self._honor
    
    def get_runes(self):
        return self._current_runes
    
    def get_power(self):
        return self._current_power
    
    def end_turn(self):
        self._current_power = 0;
        self._current_runes = 0;
        while(self._hand.get_size() != 0):
            self._deck.add_to_graveyard(self._hand.remove_card(0))
        while(self._hand.get_size() != 5):
            if(self._deck.get_size() == 0):
                self._deck.shuffle_graveyard_into_deck()
            self._hand.add_card(self._deck.draw_card())
    
    def print(self, is_print_full):
        print("Player " + self.get_name() + " - " + str(self.get_honor()) + " honor")
        print(str(self._hand.get_size()) + " cards in hand")
        if(is_print_full):
            print(str(self.get_power()) + " runes; " + str(self.get_runes()) + " power")