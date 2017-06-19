'''
Created on Jun 19, 2017

@author: user
'''
from Hand import Hand

class InPlay:
    
    def __init__(self):
        self._constructs = Hand()
        self._heroes = []
    
    def reset(self):
        for i in range(self._constructs.get_size()):
            card = self._constructs.get_card_at_index(i)
            card.untap()
        del self._heroes[:]
    
    def use_construct(self, index):
        card = self._constructs.get_card_at_index(index)
        card.tap()
    
    def add_construct(self, card):
        self._constructs.add_card(card)
    
    def remove_construct(self, index):
        return self._constructs.remove_card(index)
    
    def add_hero(self, card):
        self._heroes.append(card)
    
    def is_hero_type_in_play(self, card_type):
        for i in range(len(self._heroes)):
            if(self._heroes[i].get_card_type() == card_type):
                return True;
        return False

    def print(self):
        self._constructs.print()