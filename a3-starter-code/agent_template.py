'''
ahong02KInARow.py
Author: Aaron Hong
An agent for playing "K-in-a-Row with Forbidden Squares"
CSE 415, University of Washington

THIS IS A TEMPLATE WITH STUBS FOR THE REQUIRED FUNCTIONS.
YOU CAN ADD WHATEVER ADDITIONAL FUNCTIONS YOU NEED IN ORDER
TO PROVIDE A GOOD STRUCTURE FOR YOUR IMPLEMENTATION.

'''

import time, copy, math

# Global variables to hold information about the opponent and game version:
INITIAL_STATE = None
OPPONENT_NICKNAME = 'Not yet known'
OPPONENT_PLAYS = 'O' # Update this after the call to prepare.

# Information about this agent:
MY_LONG_NAME = 'Luminous Godwin, Bane of Bots, Curator of Viruses, King of Lies'
MY_NICKNAME = 'Xx_Godwin_xX'
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
    return MY_NICKNAME
 
############################################################

# Receive and acknowledge information about the game from
# the game master:
def prepare(initial_state, k, what_side_I_play, opponent_nickname):
    # Write code to save the relevant information in either
    # global variables.

    INITIAL_STATE = initial_state
    K = k
    I_PLAY = what_side_I_play
    OPPONENT_NICKNAME = opponent_nickname


    print("Change this to return 'OK' when ready to test the method.")
    return "OK"
 
############################################################
 
def makeMove(currentState, currentRemark, timeLimit=10000):
    #print("makeMove has been called")

    #print("code to compute a good move should go here.")
    # Here's a placeholder:
    a_default_move = [0, 0] # This might be legal ONCE in a game,
    # if the square is not forbidden or already occupied.
    
    newState = currentState # This is not allowed, and even if
    # it were allowed, the newState should be a deep COPY of the old.

    #new_move_state = minimax(currentState, 2)[1]
    move_data = minimax(currentState, 2)
    print(move_data[0])
    
    newRemark = "I need to think of something appropriate.\n" +\
    "Well, I guess I can say that this move is probably illegal."

    return [move_data[1], newRemark]
 
 
##########################################################################
 
# The main adversarial search function:
def minimax(state, depthRemaining, pruning=False, alpha=None, beta=None, zHashing=None):
    #print("Calling minimax. We need to implement its body.")

    best_move_state = [[0,0], state]
    if depthRemaining == 0:
        return [staticEval(state), best_move_state]
    if state[1] == 'X': provisional = -100000
    else: provisional = 100000

    for s in successors(state):
        new_score = minimax(s[1], depthRemaining - 1)
        if (state[1] == 'X' and new_score[0] > provisional) or (state[1] == 'O' and new_score[0] < provisional):
            provisional = new_score[0]
            best_move_state = s
    #default_score = 0 # Value of the passed-in state. Needs to be computed.
    
    return [provisional, best_move_state, "my own optional stuff", "more of my stuff"]
    # Only the score is required here but other stuff can be returned
    # in the list, after the score.

def other(player):
    if player == 'X':
        return 'O'
    if player == 'O':
        return 'X'

def successors(state):
    move_states = []
    player = state[1]
    for row in range(len(state[0])):
        for column in range(len(state[0][row])):
            if state[0][row][column] == ' ':
                new_state = copy.deepcopy(state)
                new_state[0][row][column] = player
                new_state[1] = other(player)
                move_states.append([[row, column], new_state])
    return move_states
                
 
##########################################################################
 
def staticEval(state):
    #print('calling staticEval. Its value needs to be computed!')
    # Values should be higher when the states are better for X,
    # lower when better for O.
    score = 0

    score += check_all_win_cons(state[0])
    
    return score
    
def win_possible(spaces, player):
    count = 0
    if(len(spaces) < K):
        return False
    for space in spaces:
        if space == player or space == ' ':
            count += 1
        else:
            count = 0
        if count >= K:
            return True
    return False

def in_a_row_score(spaces, player):
    score = 0
    in_a_row = 0
    for space in spaces:
        if space == player:
            in_a_row += 1
            score += math.pow(4, in_a_row)
        else:
            in_a_row = 0
    return score


def win_possible_score(spaces):
    score = 0
    if win_possible(spaces, 'X'):
        score += 1
        score += in_a_row_score(spaces, 'X')
    if win_possible(spaces, 'O'):
        score -= 1
        score -= in_a_row_score(spaces, 'O')
    return score

def check_all_win_cons(board):
    score = 0
    score += check_rows(board)
    score += check_columns(board)
    score += check_upwards_diagonals(board)
    score += check_downwards_diagonals(board)
    return score

def check_rows(board):
    score = 0
    for row in board:
        score += win_possible_score(row)
    return score

def check_columns(board):
    score = 0
    for i in range(len(board[:])):
        column = []
        for row in board:
            column.append(row[i])
        score += win_possible_score(column)
    return score

def check_upwards_diagonals(board):
    score = 0
    for row_start in range(len(board)):
        diagonal = []
        column_index = 0
        row_index = row_start
        while within_board_bounds(board, row_index, column_index):
            diagonal.append(board[row_index][column_index])
            column_index += 1
            row_index -= 1
        score += win_possible_score(diagonal)
    for column_start in range(1, len(board[:])):
        diagonal = []
        column_index = column_start
        row_index = len(board) - 1
        while within_board_bounds(board, row_index, column_index):
            diagonal.append(board[row_index][column_index])
            row_index -= 1
            column_index += 1
        score += win_possible_score(diagonal)
    return score

def check_downwards_diagonals(board):
    score = 0
    for row_start in range(len(board)):
        diagonal = []
        column_index = len(board[:]) - 1
        row_index = row_start
        while within_board_bounds(board, row_index, column_index):
            diagonal.append(board[row_index][column_index])
            column_index -= 1
            row_index -= 1
        score += win_possible_score(diagonal)
    for column_start in range(len(board[:]) - 2, -1, -1):
        diagonal = []
        column_index = column_start
        row_index = len(board) - 1
        while within_board_bounds(board, row_index, column_index):
            diagonal.append(board[row_index][column_index])
            row_index -= 1
            column_index -= 1
        score += win_possible_score(diagonal)
    return score

def within_board_bounds(board, row, column):
    return row >= 0 and column >= 0 and row < len(board) and column < len(board[:])
        

FIVE_INITIAL_STATE = \
              [[['-',' ',' ',' ',' ',' ','-'],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ','X',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ['-',' ',' ',' ',' ',' ','-']], "X"]

test_board =   [['-',' ',' ',' ','X',' ','-'],
                [' ',' ',' ','X',' ',' ',' '],
                [' ',' ','X',' ',' ',' ',' '],
                [' ','X',' ',' ',' ',' ',' '],
                ['X',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' '],
                ['-',' ',' ',' ',' ',' ','-']]

TTT_INITIAL_STATE = [[[' ',' ',' '],
                      [' ','X',' '],
                      [' ',' ',' ']], "X"]

# print(in_a_row_score(['X', 'X', ' ', ' '], 'X'))
# print(win_possible(['X','X','X', ' ','O','O'], 'X'))
print(staticEval(TTT_INITIAL_STATE))
print(staticEval(FIVE_INITIAL_STATE))
        

 
##########################################################################
