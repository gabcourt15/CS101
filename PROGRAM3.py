########################################################################
##
## CS 101
## Program 3
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : Students need an ample way to study for slices that could be presented to them on the CS101 Exam 1.
##
## ALGORITHM : 
##      1.	Ask user for input
##          a.	How many rounds do you want to play?
##              i.	If user enters input < 1 or input > 20, explain error and return to step 1a
##              ii.	If user enters a number between 1 and 20, including 1 and 20, continue to step 1b
##          b.	How easy of a string? 
##              i.	If user enters input > 3 or < 1, explain error and return to step 1b
##              ii.	If user enters input between 1 and 3, including 1 and 3, continue to step 2
##      2.	Begin round
##      3.	Generate random word slice
##          a.	If difficulty level set at 1, word = 5 chars
##          b.	If difficulty level set at 2, word = 7 chars
##          c.	If difficulty level set at 3, word = 10 chars
##      4.	Generate random start and end slice values
##          a.	If difficulty level = 1, start slice value can be from 0 to 2 and end value can be from 2 to 4
##          b.	If difficulty level = 2, start slice value can be from 0 to 3 and end value can be from 3 to 6
##          c.	If difficulty level = 3, start slice value can be from 0 to 4 and end value can be from 5 to 9
##              i.	Start slice negative = 25%
##              ii.	End slice negative= 25%
##              iii.	Reverse slice = 25%
##              iv.	Interval is 2 or -2 = 25%
##      5.	Ask the user what the slice of the generated word is
##          a.	If user enters correct response, tell them and add one to correct answers total
##          b.	If user enters incorrect response, tell them
##      6.	If another round is needed, return to step 2
##      7.	End rounds
##      8.	Output number of correct responses out of total responses and percentage of correctness.
##      9.	Ask the user if they would like to play again (consider different versions and code to include them)
##          a.	If yes, start again at step 1
##          b.	If no, end program
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#IMPORTING MODULES
import random
import string

#INITIALIZING LOOP
play_again = True

#BEGINNING USER INPUT
while play_again == True:
    hints_loop = True
    play_again_loop = True
    print("Welcome to the game of slice")
    while True:
        try:
            number_of_rounds = int(input("\nHow many rounds do you want to play? ==>"))
            total_rounds = number_of_rounds
            if number_of_rounds < 1:
                print("You must play one or more rounds")
                continue
            if number_of_rounds > 20:
                print("You must play less than twenty rounds")
                continue
            break
        except ValueError:
            print("You must enter a positive integer of rounds to play")
    while True:
        try:
            difficulty_level = int(input("\nHow easy of a string? 1. Easy, 2. Medium, 3. Hard ==>"))
            if difficulty_level < 1:
                print("You must enter 1, 2, or 3")
                continue
            if difficulty_level > 3:
                print("You must enter 1, 2, or 3")
                continue
            break
        except ValueError:
            print("You must enter 1, 2, or 3")
    while hints_loop == True:
        hints = input("\nDo you want hint indexes? ==>").upper()
        if hints == "Y" or hints == "YES":
            hints = True
            hints_loop = False
        elif hints == "N" or hints == "NO":
            hints = False
            hints_loop = False
        else:
            print("You must enter Y/YES/N/NO.")

#BEGINNING PLAY
    total_correct = 0
    while number_of_rounds > 0:
        if difficulty_level == 1:
            random_string = ""
            for x in range(0,5):
                random_string = random.choice(string.ascii_letters) + random_string
            half_length = int(len(random_string)/2)
            start_slice = random.randrange(0, half_length + 1)
            end_slice = random.randrange(half_length + 1 ,6)
            answer = random_string[start_slice:end_slice]
            if hints == True:
                print("\n                     01234")
                user_guess = input("What is the slice of " + random_string + "[" +str(start_slice) + ":" + str(end_slice) +"]? ==>")
            if hints == False:
                user_guess = input("\nWhat is the slice of " + random_string + "[" +str(start_slice) + ":" + str(end_slice) +"]? ==>")
            if user_guess == answer:
                print("Correct, the answer was " + answer)
                total_correct += 1
            else:
                print("Incorrect, the answer was " + answer)
            number_of_rounds -= 1
        elif difficulty_level == 2:
            random_string = ""
            for x in range(0,7):
                random_string = random.choice(string.ascii_letters) + random_string
            half_length = int(len(random_string)/2)
            start_slice = random.randrange(0, half_length + 1)
            end_slice = random.randrange(half_length + 1 ,8)
            answer = random_string[start_slice:end_slice]
            if hints == True:
                print("\n                     0123456")
                user_guess = input("What is the slice of " + random_string + "[" +str(start_slice) + ":" + str(end_slice) +"]? ==>")
            if hints == False:
               user_guess = input("\nWhat is the slice of " + random_string + "[" +str(start_slice) + ":" + str(end_slice) +"]? ==>") 
            if user_guess == answer:
                print("Correct, the answer was " + answer)
                total_correct += 1
            else:
                print("Inncorrect, the answer was " + answer)
            number_of_rounds -= 1
        else:
            random_string= ""
            for x in range(0,10):
                random_string = random.choice(string.ascii_letters) + random_string
            start_slice = random.randint(0,4)
            end_slice = random.randint(5,9)
            start_slice_negative = random.randint(1,4)
            end_slice_negative = random.randint(1,4)
            reverse_slice = random.randint(1,4)
            interval_of_2 = random.randint(1,5)
            if start_slice_negative != 1 and end_slice_negative != 1:
                start_slice = random.randint(0,4)
                end_slice = random.randint(5,9)
                answer = random_string[start_slice:end_slice]
                increment = 1
            if start_slice_negative == 1 and end_slice_negative == 1:
                start_slice = random.randint(-10, -6)
                end_slice = random.randint(-5, -1)
                increment = 1
            if start_slice_negative != 1 and end_slice_negative == 1:
                start_slice = random.randint(0,4)
                end_slice = random.randint(-5, -1)
                increment = 1
            if start_slice_negative == 1 and end_slice_negative != 1:
                start_slice = random.randint(-10, -6)
                end_slice = random.randint(5,9)
                increment = 1
            if reverse_slice == 1:
                increment = -1
            if interval_of_2 == 1 and reverse_slice == 1:
                increment = -2
            if interval_of_2 == 1 and reverse_slice != 1:
                increment = 1
                #TELLING USER THEIR CORRECTNESS AND ANSWER
            if increment > 0:
                answer = random_string[start_slice:end_slice:increment]
                if hints == True:
                    print("\n                     0123456789\n                    -0987654321")
                    user_guess = input("What is the slice of " + random_string + "[" + str(start_slice) + ":" + str(end_slice) + ":" + str(increment) + "]? ==>")
                if hints == False:
                    user_guess = input("\nWhat is the slice of " + random_string + "[" + str(start_slice) + ":" + str(end_slice) + ":" + str(increment) + "]? ==>")
                if user_guess == answer:
                    print("Correct, the answer was " + answer)
                    total_correct += 1
                else:
                    print("Incorrect, the answer was " + answer)
            if increment < 0:
                answer = random_string[end_slice:start_slice:increment]
                if hints == True:
                    print("\n                     0123456789\n                    -0987654321")
                    user_guess = input("What is the slice of " + random_string + "[" + str(end_slice) + ":" + str(start_slice) + ":" + str(increment) + "]? ==>")
                if hints == False:
                    user_guess = input("\nWhat is the slice of " + random_string + "[" + str(end_slice) + ":" + str(start_slice) + ":" + str(increment) + "]? ==>")
                if user_guess == answer:
                    print("Correct, the answer was " + answer)
                    total_correct += 1
                else:
                    print("Incorrect, the answer was " + answer)
            number_of_rounds -= 1

    #OUTPUT AT END OF ROUNDs
    percentage = (total_correct / total_rounds) * 100
    print("\nYou got " + str(total_correct) + " out of " + str(total_rounds) + " which is " + str("{:4.2f}".format(percentage)) + "%.")

    #PLAY AGAIN?
    while play_again_loop == True:
        play_again = input("\nWould you like to play again?").upper()
        if play_again == "Y" or play_again == "YES":
            play_again = True
            play_again_loop = False
        elif play_again == "N" or play_again == "NO":
            play_again = False
            play_again_loop = False
        else:
            print("You must enter Y/YES/N/NO.")
