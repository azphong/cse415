'''Farmer_Fox.py
by Aaron Hong
UWNetID: ahong02
Student number: 1902131

Assignment 2, in CSE 415, Autumn 2023.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

SOLUTION_VERSION = "1.0"
PROBLEM_NAME = "Farmer, Fox, Chicken, Grain"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['A. Hong']
PROBLEM_CREATION_DATE = "16-OCT-2023"

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

LEFT=0
RIGHT=1

class State():

    def __init__(self, d=None):
        if d==None:
            d = {'farmer':LEFT,
                 'fox':LEFT,
                 'chicken':LEFT,
                 'grain':LEFT}
        self.d=d

    def __eq__(self,s2):
        for thing in self.d:
            if self.d[thing] != s2.d[thing]: return False
        return True
    
    def __str__(self):
        txt = ""
        for thing in self.d:
            txt += thing + " is on the "
            if self.d[thing] == LEFT:
                txt += "left\n"
            else:
                txt += "right\n"
        return txt
    
    def __hash__(self):
        return (self.__str__()).__hash__()
    
    def copy(self):
        new_state = State({})
        for thing in self.d:
            new_state.d[thing] = self.d[thing]
        return new_state
    
    def can_move(self,moving_things):
        farmer_side = self.d['farmer']
        for thing in moving_things:
            if self.d[thing] != farmer_side:
                return False # can't move thing if not on same side as farmer
        temp_state = self.copy()
        for thing in moving_things:
            temp_state.d[thing] = 1-temp_state.d[thing]
        if temp_state.d['chicken'] != temp_state.d['farmer']:
            if temp_state.d['chicken'] == temp_state.d['fox']:
                return False # can't leave chicken and fox alone
            if temp_state.d['chicken'] == temp_state.d['grain']:
                return False # can't leave chicken and grain alone
        return True
    
    def move(self,moving_things):
        new_state = self.copy()
        for thing in moving_things:
            new_state.d[thing] = 1-new_state.d[thing]
        return new_state
    
def goal_test(s):
    for thing in s.d:
        if s.d[thing] == LEFT:
            return False
    return True

def goal_message(s):
    return "Congratulations on moving everything across the river!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)
    
    def apply(self, s):
        return self.state_transf(s)
    
CREATE_INITIAL_STATE = lambda : State()

OPERATORS = [Operator("Send the farmer across alone",
                    lambda s: s.can_move(['farmer']),
                    lambda s: s.move(['farmer'])),
            Operator("Send the chicken with the farmer",
                    lambda s: s.can_move(['farmer', 'chicken']),
                    lambda s: s.move(['farmer', 'chicken'])),
            Operator("Send the grain with the farmer",
                    lambda s: s.can_move(['farmer', 'grain']),
                    lambda s: s.move(['farmer', 'grain'])),
            Operator("Send the fox with the farmer",
                    lambda s: s.can_move(['farmer', 'fox']),
                    lambda s: s.move(['farmer', 'fox']))]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)



        


#pass  # replace this.
