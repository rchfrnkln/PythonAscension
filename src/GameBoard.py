'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
import DeckFactory
from src.cards.Cultist import Cultist
from Hand import Hand

class GameBoard:

    MYSTIC_INDEX = 6
    HEAVY_INDEX = 7
    CULTIST_INDEX = 8
    
    def __init__(self):
        self._mystics = DeckFactory.build_mystic_deck()
        self._heavies = DeckFactory.build_heavy_deck()
        self._deck = DeckFactory.build_center_deck()
        self._board = Hand()
        self._cultist = Cultist()
        for _ in range(6):
            self.draw_card()
        
    def draw_card(self):
        card = self._deck.draw_card()
        self._board.add_card(card)
    
    def get_card(self, index):
        self.assert_is_valid_index(index)
        
        if(index == self.MYSTIC_INDEX):
            return self._mystics.peek()
        if(index == self.HEAVY_INDEX):
            return self._heavies.peek()
        if(index == self.CULTIST_INDEX):
            return self._cultist
        return self._board.get_card_at_index(index)
        
    def acquire_card(self, index):
        self.assert_is_valid_index(index)
        
        if(index == self.MYSTIC_INDEX):
            return self.acquire_mystic()
        if(index == self.HEAVY_INDEX):
            return self.acquire_heavy()
        if(index == self.CULTIST_INDEX):
            self._cultist.acquire()
        
        card = self._board.remove_card(index)
        try:
            card.acquire()
            self.draw_card()
            return card
        except Exception as e:
            self._board.add_card_at_index(card, index)
            raise e
            
    def acquire_heavy(self):
        card = self._heavies.draw_card()
        return card
    
    def acquire_mystic(self):
        card = self._mystics.draw_card()
        return card
        
    def defeat_card(self, index):
        self.assert_is_valid_index(index)
        
        if(index == self.CULTIST_INDEX):
            return self._cultist.defeat()
        
        card = self._board.remove_card(index)
        try:
            honor = card.defeat()
            self.draw_card()
            return honor
        except Exception as e:
            self._board.add_card_at_index(card, index)
            raise e
    
    def print(self):
        for i in range(self._board.get_size()):
            print(str(i) + ". " + self._board.get_card_at_index(i).get_name())
        print(str(GameBoard.MYSTIC_INDEX) + ". " + self._mystics.peek().get_name())
        print(str(GameBoard.HEAVY_INDEX) + ". " + self._heavies.peek().get_name())
        print(str(GameBoard.CULTIST_INDEX) + ". " + self._cultist.get_name())
    
    def assert_is_valid_index(self, index):
        if(self.is_valid_index(index) == False):
            raise Exception("Invalid index.")
    
    def is_valid_index(self, index):
        if(index < 0):
            return False
        if(index > 8):
            return False
        return True