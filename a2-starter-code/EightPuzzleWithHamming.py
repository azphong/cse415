"""FranceWithDXHeuristic.py
This file augments EightPuzzle.py with heuristic information.
The particular heuristic is a hamming heuristic.

"""

from EightPuzzle import *

TARGET = ([[0,1,2],[3,4,5],[6,7,8]])

def h(currentState):
    h = 0
    for i in range(3):
      for j in range(3):
         if currentState.b[i][j] != 0 and currentState.b[i][j] != TARGET[i][j]:
            h += 1
    return h