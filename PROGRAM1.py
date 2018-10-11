########################################################################
##
## CS 101
## Program 1
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : Given user input, calculate how long a drone can fly.
##
## ALGORITHM : 
##      1. Ask user for input
##      2. Convert milliamp to amp
##      3. Find amps used
##      4. Find how long the drone will fly
##      5. Convert that to minutes
##      6. Isolate float multiply by 60
##      7. create print out
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#Getting input and turning it into an int
mAh = int(input("Enter the mAh")) #asking user how many mAh and converting to int
motors = int(input("How many motors does the drone have?")) #asking user how many motors and converting to an int
amps_per_motor = int(input("How many Amps drawn per motor?")) #asking user how many amps drawn and converting to an int

#Calculations
Ah = mAh / 1000 #convert milliamp hours to amp hours
amps_used = motors * amps_per_motor #find amount of amps used
hours = Ah / amps_used #how long drone will fly in hours
minutes = hours * 60 #convert hours to minutes
minutes_int = int(minutes) #get float portion by itself
seconds = (minutes - int(minutes)) * 60 #find seconds
seconds_int = int(seconds) #converting to an int

#Output
print("Your drone will use", amps_used, "amps")
print("Your flight time will be", minutes,"minutes")
print("Which is", minutes_int, "minutes and", seconds_int, "seconds")
