'''Farmer_Fox.py
by Janet Jenson
UWNetID: jjens17
Student number: 2076543

Assignment 2, in CSE 415, Autumn 2023.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

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
    
    def can_move(self,things):
        farmer_side = []
        for thing in self.d:
            if self.d[thing]==self.d['farmer']:
                farmer_side.append(thing)
            if thing in things and thing not in farmer_side:
                return False # can't move thing if not on same side as farmer
        farmer_side.remove(thing for thing in things)
        if 'chicken' in farmer_side and 'fox' in farmer_side:
            return False # can't leave fox and chicken alone
        if 'chicken' in farmer_side and 'grain' in farmer_side:
            return False # can't leave chicken and grain alone
        return True

            


#pass  # replace this.
