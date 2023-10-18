'''
<yourUWNetID>KInARow.py
Author: <your name here>
An agent for playing "K-in-a-Row with Forbidden Squares"
CSE 415, University of Washington

THIS IS A TEMPLATE WITH STUBS FOR THE REQUIRED FUNCTIONS.
YOU CAN ADD WHATEVER ADDITIONAL FUNCTIONS YOU NEED IN ORDER
TO PROVIDE A GOOD STRUCTURE FOR YOUR IMPLEMENTATION.

'''

import time

# Global variables to hold information about the opponent and game version:
INITIAL_STATE = None
OPPONENT_NICKNAME = 'Not yet known'
OPPONENT_PLAYS = 'O' # Update this after the call to prepare.

# Information about this agent:
MY_LONG_NAME = 'Templatus Skeletus'
MY_NICKNAME = 'Tea-ess'
I_PLAY = 'X' # Gets updated by call to prepare.

 
# GAME VERSION INFO
M = 0
N = 0
K = 0
TIME_LIMIT = 0
 
 
############################################################
# INTRODUCTION
def introduce():
    intro = '\nMy name is Templatus Skeletus.\n'+\
            '"An instructor" made me.\n'+\
            'Somebody please turn me into a real game-playing agent!\n' 
    return intro
 
def nickname():
    return 'Tea-ess'
 
############################################################

# Receive and acknowledge information about the game from
# the game master:
def prepare(initial_state, k, what_side_I_play, opponent_nickname):
    # Write code to save the relevant information in either
    # global variables.
    print("Change this to return 'OK' when ready to test the method.")
    return "Not-OK"
 
############################################################
 
def makeMove(currentState, currentRemark, timeLimit=10000):
    print("makeMove has been called")

    print("code to compute a good move should go here.")
    # Here's a placeholder:
    a_default_move = [0, 0] # This might be legal ONCE in a game,
    # if the square is not forbidden or already occupied.
    
    newState = currentState # This is not allowed, and even if
    # it were allowed, the newState should be a deep COPY of the old.
    
    newRemark = "I need to think of something appropriate.\n" +\
    "Well, I guess I can say that this move is probably illegal."

    print("Returning from makeMove")
    return [[a_default_move, newState], newRemark]
 
 
##########################################################################
 
# The main adversarial search function:
def minimax(state, depthRemaining, pruning=False, alpha=None, beta=None, zHashing=None):
    print("Calling minimax. We need to implement its body.")

    default_score = 0 # Value of the passed-in state. Needs to be computed.
    
    return [default_score, "my own optional stuff", "more of my stuff"]
    # Only the score is required here but other stuff can be returned
    # in the list, after the score.
 
##########################################################################
 
def staticEval(state):
    print('calling staticEval. Its value needs to be computed!')
    # Values should be higher when the states are better for X,
    # lower when better for O.
    return 0
 
##########################################################################
