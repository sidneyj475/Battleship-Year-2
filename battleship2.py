import RPi.GPIO as GPIO
#import GPIOmock as GPIO
import threading
import time
import random
import os
from subprocess import call

LIGHTS_ROW1 = [7, 11, 13]
LIGHTS_ROW2 = [15, 29, 31]
LIGHTS_ROW3 = [33, 35, 37]
 

# Defining the Game Board
def print_board(board):
    for z in board:
        print(" ".join(z))

def print_board2(board2):
    for x in board2:
        print(" ".join(x))

 # Game Intro       
 
print("Let's Play Battleship! Your enemy is on water. They're coming at you and FAST! Do your best to destroy their fleet. You have 5 chances.")


# User defines how large board will be. The board size will be the same for both players (user and computer)
grid = int(input("Choose Your Grid Size: "))

grid2 = grid