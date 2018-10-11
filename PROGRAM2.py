########################################################################
##
## CS 101
## Program 2
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : The airline we are using to fly isn't very organized and luggage is often not on time.
##
## ALGORITHM :
##      1.Import modules
##      2.Ask user how many times to run lost luggage
##          a.If user inputs number <= 0, warn user, explain error and return to step 2
##          b.If user inputs number > 0, go to step 3
##      3.Once user gives valid input, convert to int
##      4.Ask user if they want detailed output
##          a.Convert their input to all upper/lower case
##          b.Consider different versions of answer and code to include them
##      5.Begin starting hop
##      6.Generate random whole number
##      7.Determine what location the suitcase ends up at based on number from step 6
##          current location of suitcase is LVS if number generated is 1, 2, 3 or 4
##          current location of suitcase is SEA if number generated is 5, 6, or 7
##          current location of suitcase is HNL if number generated is 8, 9, or 10
##      8.If suitcase ends up in HNL, start step 9
##      9.If suitcase ends up in MCI, LVS, or SEA regenerate random numbers until suitcase ends up at HNL
##      10.Once, suitcase ends up in HNL, Begin next trial (if another is needed) by starting over at step 5
##      11.End trials
##      12.Output details (if user said yes previously)
##      13.Output percentage and fraction that suitcase arrived on time
##      14.Ask user if they want to run the program again
##          a.If yes, start again at step 2
##          b.If no, end program
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import random
play_again = True
count_3 = 0
while play_again == True:
#INPUT
    while count_3 == 0: #getting input for number of trials
        number_of_luggage_runs = input("How many times would you like to run lost luggage? ")
        number_of_luggage_runs = int(number_of_luggage_runs)
        if number_of_luggage_runs > 0:
            count_3 += 1
        elif number_of_luggage_runs <= 0:
            print("You must enter a number greater than 0")
    total_runs = number_of_luggage_runs

    count = 0
    while count == 0: #getting input for detailed output
        detailed_output = input("Would you like detailed output? ").upper()
        if detailed_output in ("Y", "YES", "N", "NO"):
            count += 1
        elif detailed_output != "Y" or detailed_output != "YES" or detailed_output != "N" or detailed_output != "NO":
            print("Please enter valid input")
    current_location = 0
    hops = 0
    count_hops = 0
    start = 0
    max_hops = 0
    #BEGIN TRACKING LUGGAGE
    while number_of_luggage_runs > 0: #starting hop
        starting_hop = random.randint(1,11)
        if detailed_output == "Y" or detailed_output == "YES":
            print("MCI ->", end="")
        while starting_hop:
            if starting_hop in range(1,5): #determining if suitcase goes to LVS first
                hops += 1
                current_location = 3 #sets LVS to location 3
                if detailed_output == "Y" or detailed_output == "YES":
                    print("LVS ->", end="")
                break
            elif starting_hop in range(5,8): #determining if suitcase goes to SEA first
                hops += 1
                current_location = 2 #sets SEA to location 2
                if detailed_output == "Y" or detailed_output == "YES":
                   print("SEA ->",end="")
                break
            else:
                #determining if suitcase goes to HNL first
                hops += 1
                current_location = 4 #sets HNL to location 4
                break
        #SWITCHES FROM STARTING HOP TO CURRENT LOCATION
        while number_of_luggage_runs > 0: #determines every hop after the first
            if current_location == 1: #determines the last hop was to MCI
                from_MCI = random.randint(1,11)
                if from_MCI in range(1,5): #sends suitcase to LVS
                    hops += 1
                    current_location = 3 #location 3 is LVS
                    if detailed_output == "Y" or detailed_output == "YES":
                       print("LVS ->", end="")
                elif from_MCI in range(5,8): #sends suitcase to SEA
                    hops += 1
                    current_location = 2 #location 2 is SEA
                    if detailed_output == "Y" or detailed_output == "YES":
                       print("SEA ->", end="")
                else: #determines the last hop was to HNL
                    hops += 1
                    current_location = 4 #sends suitcase to HNL
            elif current_location == 2:#determines the last hop was to SEA
                from_SEA = random.randint(1,11)
                if from_SEA in range(1,2): #sends suitcase to MCI
                    hops += 1
                    current_location = 1 #location 1 is MCI
                    if detailed_output == "Y" or detailed_output == "YES":
                       print("MCI ->", end="")
                elif from_SEA in range(2,8): #sends suitcase to LVS
                    hops += 1
                    current_location = 3 #location 3 is LVS
                    if detailed_output == "Y" or detailed_output == "YES":
                        print("LVS ->", end="")
                else: #determines the last hop was to HNL
                    hops += 1
                    current_location = 4 #sends suitcase to HNL
            elif current_location == 3: #determines the last hop was to LVS
                from_LVS = random.randint(1,11)
                if from_LVS in range(1,4):#sends suitcase to MCI
                    hops += 1
                    current_location = 1 #location 1 is MCI
                    if detailed_output == "Y" or detailed_output == "YES":
                        print("MCI ->", end="")
                elif from_LVS in range(4,9): #sends suitcase to SEA
                    hops += 1
                    current_location = 2 #location 2 is SEA
                    if detailed_output == "Y" or detailed_output == "YES":
                        print("SEA ->", end="")
                else: #determines the last hop was to HNL
                    hops += 1
                    current_location = 4 #sends suitcase to HNL
            elif current_location == 4: #determines the last hop was to HNL
                if detailed_output == "Y" or detailed_output == "YES":
                    print("HNL")
                number_of_luggage_runs -= 1 #subtracts one to change variable to test if loop should reiterate
                if hops <= 2: #determines is said trial was considered on-time
                    count_hops += 1
                max_hops = hops
                if start < max_hops: 
                    start = max_hops #stores max_hops to compare to all other trials to determine if it really was the max hop
                hops = 0
                break
#OUTPUT    
    print("The baggage was on time", (count_hops / total_runs)*100 , "% of the time", "(", count_hops, "/", total_runs,")") #reports results to user
    print("The max hops that occured was", start) #reports results to user
    count_2 = 0
    while count_2 == 0:
        play_again = input("Would you like to run again? ").upper() #determines if program needs to be run again
        if play_again in ("Y", "YES"):
            count_2 += 1
            count_3 = 0
            play_again = True
        elif play_again in ("N", "NO"):
            count_2 += 1
            play_again = False
        elif detailed_output != "Y" or detailed_output != "YES" or detailed_output != "N" or detailed_output != "NO":
            print("Please enter valid input")
