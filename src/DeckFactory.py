'''
Created on Jun 15, 2017

@author: KrzyMoose
'''
from src.cards.Apprentice import Apprentice
from src.cards.Militia import Militia
from src.cards.HeavyInfantry import HeavyInfantry
from src.cards.Mystic import Mystic
from src.cards.ArhaInitiate import ArhaInitiate
from Deck import Deck
from src.cards.ArbiterOfThePrecipice import ArbiterOfThePrecipice
from src.cards.AsceticOfTheLidlessEye import AsceticOfTheLidlessEye

STARTING_APPRENTICE = 8
STARTING_MILITIA = 2
STARTING_MYSTIC = 30
STARTING_HEAVY = 29

STARTING_ARBITER = 2
STARTING_ARHA_INITIATE = 3
STARTING_ASCETIC = 2

def build_player_deck():
    cards = []
    for _ in range(STARTING_APPRENTICE):
        cards.append(Apprentice())
    for _ in range(STARTING_MILITIA):
        cards.append(Militia())
    return Deck(cards)

def build_center_deck():
    cards = []
    for _ in range(STARTING_ARHA_INITIATE):
        cards.append(ArhaInitiate())
    for _ in range(STARTING_ARBITER):
        cards.append(ArbiterOfThePrecipice())
    for _ in range(STARTING_ASCETIC):
        cards.append(AsceticOfTheLidlessEye())
    return Deck(cards)

def build_mystic_deck():
    cards = []
    for _ in range(STARTING_HEAVY):
        cards.append(Mystic())
    return Deck(cards)

def build_heavy_deck():
    cards = []
    for _ in range(STARTING_MYSTIC):
        cards.append(HeavyInfantry())
    return Deck(cards)