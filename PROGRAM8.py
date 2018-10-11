########################################################################
##
## CS 101
## Program 8
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : 
##
## ALGORITHM : 
##  1.	Create Park
##  2.	Ask user number of lots in the simulation
##      a.	If number < 2, warn user and return to step 2
##      b.	If number > 11, warn user and return to step 2
##      c.	If number is not an int, warn user and return to step 2
##  3.	Create lots
##      a.	Update lots_total and lots in park
##  4.	Ask user for the number of tourists waiting on the trams
##      a.	If number < 0, warn user and return to step 4
##      b.	If number > 20, warn user and return to step 4
##      c.	If number is not an int, warn user and return to step 4
##  5.	Create tourists
##  6.	Create tram
##  7.	For each tram stop, output the number of passengers that get off the tram and get onto the tram. 
##  8.	Once all tourists are to their desired location, end program
##
## ERROR HANDLING:
##
##
## OTHER COMMENTS:
##      Any special comments
##
#########################################################################

import random

#CLASSES

class Park(object):
    def __init__(self, lots = 2, tourist_num = 0):
        self.lots = lots
        self.tourist_num = tourist_num
    def __str__(self):
        #print("Park Status\nTram dropped off {} passengers and picked up {} passengers at Lot {}".format(
        pass
    def step(self):
        #FINISH THIS
        pass

class ParkingLot(Park):
    def __init__(self, lot_number):
        self.lot_number = lot_number
    def __str__(self):
        return "L{}({})".format(self.lot_number, self.tourist_num)
    def __repr__(self):
        return "L{}({})".format(self.lot_number, self.tourist_num)
    def register_tourist(self, tourist):
        #FINISH THIS
        pass

class Tram(object):
    def __init__(self, current_lot, lots):
        self.current_lot = ccurrent_lot
        self.lots = lots
    def __str__(self):
        #FINISH THIS
        pass
    def move(self):
        #FINISH THIS
        pass
    def direction(self):
        #FINISH THIS
        pass
    def tourists(self):
        #FINISH THIS
        pass

class Tourist(Park):
    def __init__(self, start_lot, dest_lot):
        Park.__init__(self, lots, tourist_num)
        self.start_lot = start_lot
        self.dest_lot = dest_lot
    
#FUNCTIONS
def num_of_lots():
    while True:
        try:
            number_of_lots = int(input("How many lots are in the simulation?"))
            if number_of_lots < 2:
                print("There must be more than 1 lot")
                continue
            elif number_of_lots > 11:
                print("There must be 11 or less lots")
                continue
            break
        except ValueError:
            print("You must enter a valid number of lots")
    return number_of_lots

def num_of_tourists():
    while True:
        try:
            number_of_tourists = int(input("How many tourists are waiting on the tram?"))
            if number_of_tourists < 1:
                print("There must be at least one person waiting on the tram.")
                continue
            if number_of_tourists > 20:
                print("There cannot be more than 20 people waiting on the tram.")
                continue
            break
        except ValueError:
            print("You must enter a valid number of people waiting on the tram.")
    return number_of_tourists
#PROGRAM
park_open = True        
while park_open == True:
    lots = num_of_lots()
    tourist_num = num_of_tourists()
    Park = Park(lots, tourist_num)
        
    park_open = False
    
        
