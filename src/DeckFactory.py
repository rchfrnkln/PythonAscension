'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Apprentice import Apprentice
from src.cards.Militia import Militia
from src.cards.HeavyInfantry import HeavyInfantry
from src.cards.Mystic import Mystic
from src.cards.ArhaInitiate import ArhaInitiate

STARTING_APPRENTICE = 7
STARTING_MILITIA = 3
STARTING_MYSTIC = 30
STARTING_HEAVY = 29

def build_player_deck():
    cards = []
    for _ in range(STARTING_APPRENTICE):
        cards.append(Apprentice())
    for _ in range(STARTING_MILITIA):
        cards.apprent(Militia())
    return cards

def build_center_deck():
    cards = []
    for _ in range(60):
        cards.append(ArhaInitiate())
    return cards

def build_mystic_deck():
    cards = []
    for _ in range(STARTING_HEAVY):
        cards.append(HeavyInfantry())
    return cards

def build_heavy_deck():
    cards = []
    for _ in range(STARTING_MYSTIC):
        cards.append(Mystic)
    return cards