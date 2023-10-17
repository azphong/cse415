"""FranceWithDXHeuristic.py
This file augments EightPuzzle.py with heuristic information.
The particular heuristic is a Manhattan heuristic.

"""

from EightPuzzle import *

TARGET = ([[0,1,2],[3,4,5],[6,7,8]])

def h(currentState):
    h = 0
    for i in range(3):
      for j in range(3):
         if currentState.b[i][j] != 0:
            value = currentState.b[i][j]    
            target_i = value // 3 #row
            target_j = value % 3 #column

            # Calculate the Manhattan distance for the tile
            distance = abs(i - target_i) + abs(j - target_j)
            h += distance
    return h