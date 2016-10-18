# This is a Tic Tac Toe game against an AI. Enjoy.

from time import sleep
import random
import os

print "\n"

print "Welcome to a game of Tic Tac Toe!"

playing = True
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
sleep(1)
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
      

def check_full_o():
    
    if b[choice] == " ":
        b[choice] = "O" 
        return True
    else:
        print "Sorry, space taken. Try again."
        return False
        
def win(b,p):

    if (b[1] == p and b[2] == p and b[3] == p) or \
        (b[4] == p and b[5] == p and b[6] == p) or \
	(b[7] == p and b[8] == p and b[9] == p) or \
	(b[1] == p and b[4] == p and b[7] == p) or \
	(b[2] == p and b[5] == p and b[8] == p) or \
	(b[3] == p and b[6] == p and b[9] == p) or \
	(b[3] == p and b[5] == p and b[7] == p) or \
	(b[1] == p and b[5] == p and b[9] == p):
        return True
    else:
        return False

def computer_turn(b,p):
    for v in range(1,10):
         if b[v] == " ":
            b[v] = p
            if win(b,"O") or win(b,"X"):
                print "I'm about to win",v
                return v
            else:
                b[v] = " "
        
    computer = random.randint(1,9)
    print "first random choice",computer
    while " " not in b[computer]:
        computer = random.randint(1,9)   
    return computer
	    
    

while playing:
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
    if win(b, "X"):
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
           
    if full:
        print "Both of you lost -_-"
        break

    while not check_full_o():
        choice = computer_turn(b,"O")
        print choice
        if win(b,"O"):
            break
    

	

    if win(b, "O"):
        os.system("clear")
        game_board()
        print "O wins! Congratulations! Sorry X."
        print "GAME OVER."
        break

 

