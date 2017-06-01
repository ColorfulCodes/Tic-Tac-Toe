# -*- coding: utf-8 -*-

# This is a two player game of tic tac toe. Enjoy.

from time import sleep
import os

print "\n"

print "Welcome to a game of Tic Tac Toe!"

running = True
board = [""," "," "," "," "," "," "," "," "," "]
b = board

print """
Instructions: Choose any number 1-9 that has
not yet been used by the other player.
Player 1 will be 'X' and Player 2 will be 'O'.
In order to win the game, your letter"
(X or O) must be three times in a row either
horizontally, vertically or diagonaly.
\n
The numbers below represent the spaces you want your letters to be.
"""

def example_board():

    board = " 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9"
    print board

example_board()
sleep(5)
print "May the best player win!"


def game_board():
    print " "+b[1]+" | "+b[2]+" | "+b[3]+" \n-----------\n "+b[4]+" | "+ b[5] +" | "+b[6]+"\n-----------\n "+b[7]+" | "+b[8]+" | "+b[9]+" "

def check_full_x():
    
    if b[choice] == " ":
        b[choice] = "X" 
        return True
    else:
        print "Sorry, space full. Try again."
        return False
        sleep(1)

def check_full_o():
    
    if b[choice] == " ":
        b[choice] = "O" 
        return True
    else:
        print "Sorry, space taken. Try again."
        return False
        sleep(1)
    

while running:
    os.system("clear")
    print "Remember, Player 1 is X & Player 2 is O."
    example_board()
    print "Use the numbers above as your example."
    game_board()
    print "Player 1."
    choice = int(raw_input("What is your choice? Any number 1-9. "))
    while not check_full_x():
        choice = int(raw_input("Please choose an empty space for X. "))

    
#X's play
    if (b[1] == "X" and b[2] == "X" and b[3] == "X") or \
            (b[4] == "X" and b[5] == "X" and b[6] == "X") or \
	    (b[7] == "X" and b[8] == "X" and b[9] == "X") or \
	    (b[1] == "X" and b[4] == "X" and b[7] == "X") or \
	    (b[2] == "X" and b[5] == "X" and b[8] == "X") or \
	    (b[3] == "X" and b[6] == "X" and b[9] == "X") or \
	    (b[3] == "X" and b[5] == "X" and b[7] == "X") or \
	    (b[1] == "X" and b[5] == "X" and b[9] == "X"):
	    os.system("clear")
	    game_board()
	    print "X won the game! Too bad O."
            print "GAME OVER"
	    break

    os.system("clear")
    print "Remember, Player 1 is X & Player 2 is O."
    example_board()
    print "Use the numbers above as your example."
    game_board()

# If there is a tie
   
    full = True
    if " " in b:
        full = False
           
    if full == True:
        print "Both of you lost -_-"
        break

# O's Turn
    print "Player 2's turn."
    choice = int(raw_input("What is your choice? Any number 1-9. "))
    while not check_full_o():
        choice = int(raw_input("Please choose an empty space for O. "))
	

    if (b[1] == "O" and b[2] == "O" and b[3] == "O") or \
        (b[4] == "O" and b[5] == "O" and b[6] == "O") or \
        (b[7] == "O" and b[8] == "O" and b[9] == "O") or \
        (b[1] == "O" and b[4] == "O" and b[7] == "O") or \
        (b[2] == "O" and b[5] == "O" and b[8] == "O") or \
        (b[3] == "O" and b[6] == "O" and b[9] == "O") or \
        (b[1] == "O" and b[5] == "O" and b[9] == "O") or \
        (b[3] == "O" and b[5] == "O" and b[7] == "O"):
        os.system("clear")
        game_board()
        print "O wins! Congratulations! Sorry X."
        print "GAME OVER."
        break

