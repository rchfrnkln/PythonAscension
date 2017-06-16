'''
Created on Jun 15, 2017

@author: KrzyMoose
'''

class Hand:
    
    def __init__(self):
        self._cards = []
        
    def add_card(self, card):
        self._cards.append(card)
        
    def add_card_at_index(self, card, index):
        self._cards.insert(index, card)
    
    def get_card_at_index(self, index):
        if(index >= len(self._cards)):
            raise Exception("Invalid index")
        return self._cards[index]
        
    def remove_card(self, index):
        if(index >= len(self._cards)):
            raise Exception("Invalid index")
        card = self._cards[index]
        self._cards.remove(card)
        return card
    
    def get_size(self):
        return len(self._cards)
    
    def print(self):
        for i in range(len(self._cards)):
            print(str(i) + ". " + self._cards[i].get_name())