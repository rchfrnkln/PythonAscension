'''
Created on Jun 15, 2017

@author: KrzyMoose
''' 
import Utility
from Player import Player
from GameBoard import GameBoard

'''
Constants
'''
COMMAND_QUIT = "quit"
COMMAND_PASS_TURN = "pass"
COMMAND_BOARD = "board"
COMMAND_STATUS = "status"
COMMAND_STATUS = "cast"
COMMAND_DEFEAT = "defeat"

'''
Global Variables
'''
players = None
current_player = None
is_run = None
commands = None
game_board = None

'''
Public Functions
'''
def initialize():
    global is_run, current_player
    is_run = True
    current_player = 0
    build_players()
    build_command_map()
    build_game_board()

def run():
    global is_run, current_player, commands
    while(is_run):
        try:
            command = input(get_current_player().get_name() + "'s turn. Enter a command: ")
            if(commands.__contains__(command) == False):
                raise Exception("Invalid command.")
            commands[command]()
        except Exception as e:
            print("Error " + str(e))
    print("Exiting.")

'''
User Commands
'''
def quit_game():
    global is_run
    is_run = False

def pass_turn():
    get_current_player().end_turn()
    increment_current_player()
    
def print_board():
    global game_board
    game_board.print()

def print_status():
    global current_player, players
    for i in range(len(players)):
        if(i != current_player):
            players[i].print(False)
    get_current_player().print(True)

def cast_card():
    
    pass

def defeat_monster():
    pass

'''
Game Actions
'''
def add_power(power):
    get_current_player().add_power(power)

def add_runes(runes):
    get_current_player().add_runes(runes)

def draw_cards(num):
    for _ in range(num):
        get_current_player().draw_card()

'''
Helper Functions
'''
def build_command_map():
    global commands
    commands = dict()
    commands[COMMAND_QUIT] = quit_game
    commands[COMMAND_PASS_TURN] = pass_turn
    commands[COMMAND_BOARD] = print_board
    commands[COMMAND_STATUS] = print_status
    commands[COMMAND_CAST] = cast_card
    commands[COMMAND_DEFEAT] = defeat_monster

def build_game_board():
    global game_board
    game_board = GameBoard()

def build_players():
    global players
    players = []
    count = Utility.read_int("Enter the number of players: ")
    for i in range(count):
        name = input("Enter player %s's name: " % (i))
        players.append(Player(name))

def increment_current_player():
    global current_player, players
    current_player += 1
    if(current_player == len(players)):
        current_player = 0

def get_current_player():
    global current_player, players
    return players[current_player]