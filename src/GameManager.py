'''
Created on Jun 15, 2017

@author: KrzyMoose
''' 
from src import Utility
from src.Player import Player
from src.GameBoard import GameBoard

'''
Constants
'''
COMMAND_QUIT = "quit"
COMMAND_PASS_TURN = "pass"
COMMAND_BOARD = "board"
COMMAND_STATUS = "status"

'''
Global Variables
'''
players = None
current_player = None
isRun = None
commands = None
game_board = None

'''
Public Functions
'''
def initialize():
    global isRun, current_player
    isRun = True
    current_player = 0
    build_players()
    build_command_map()
    build_game_board()

def run():
    global isRun, current_player, commands
    while(isRun):
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
    global isRun
    isRun = False

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