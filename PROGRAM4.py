########################################################################
##
## CS 101
## Program 4
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : Transpose and untranspose lines from a file to another file.
##
## ALGORITHM : 
##     1.   Display transposition options
##          a.	(1)Encipher File
##          b.	(2)Decipher File
##          c.	(3)Quit
##              i.	If user enters input other than 1, 2, or 3 warn user and return to step 1a
##              ii.	If user enters 1, skip to step 2
##              iii.	If user enters 2, skip to step 3
##      2.  If Encipher File is chosen, ask for in file name
##          a.	If file name not found, warn user and return to step 2
##          b.	If file name is found, ask user to enter the name of the out file
##          c.	Transpose the in file and write to out file, tell user the deed has been done and  return to menu in step 1
##      3.  If Decipher File is chosen, ask for in file name
##          a.	If file name not found, warn user and return to step 3
##          b.	If file name is found, ask user to enter the name of the out file
##          c.	Untranspose the in  file and write to the out file, tell the user the deed has been done and return to menu in step 1
##      4.  If Quit is chosen, end the program.
## 
##
## ERROR HANDLING:
##      When inputting name of file, .txt must be added to the end.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


#FUNCTIONS
def options_menu(prompt, min, max,error_message):
    """Gets choice from user"""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < min or user_input > max:
                print(error_message)
                continue
        except ValueError:
            print(error_message)
            continue
        return user_input

def in_file(prompt, error_message):
    """Gets file to be read from user"""
    while True:
        try:
            file_name = input(prompt)
            file = open(file_name)
            return file
        except FileNotFoundError:
            print(error_message)
        except IOError:
            print(error_message)
            
def out_file(prompt):
    """Gets file to be written to from user"""
    file_name = input(prompt)
    write = open(file_name, "w")
    return write

def transpose():
    """Encodes the string and retuens the transposed value"""
    for line in encipher:
        strip_line = line.strip() #Gets rid of extra spaces and returns
        new_line = strip_line[::2] + strip_line[1::2] #slices the word and concatinates them to create the new line
        write_to.write(new_line +"\n")

def untranspose():
    """Takes a transposed message and returns it back to the original"""
    for line in decipher:
        line = line.strip() #Gets rid of extra spaces and returns
        line_length = len(line)
        if line_length % 2 != 0: # If length of word is odd, add one to include one more character in the first half of the word
            line_length += 1
        middle = line_length / 2 # Finds the cutting point for first half and second half
        first_half = line[:int(middle)] # sets first half to the slice of the beginning of the line
        second_half = line[int(middle):] # sets second half to the slice of the end of the line
        deciphered = ""
        for char in first_half:  #for loop with a break nested in another for loop to created deciphered with the first letter of the first half followed by the first letter of the second half then the second letter of the first half followed by the second letter of the second half and so on
            deciphered += char
            for char in second_half:
                deciphered += char
                second_half = second_half[1:]
                break
        write_to.write(deciphered +"\n")
    
#BODY
file_transposition = True #while user doesn't select 3 file transposition is True
while file_transposition == True:
    choice = options_menu("Transposition Options: \n1. Encipher File\n2. Decipher File\n3. Quit\nWhat would you like to do? ==>", 1, 3, "You must enter 1, 2,or 3\n")
    if choice == 1:
        encipher = in_file("\nWhat is the name of the file you'd like to encipher? ==>", "Could not find the file specified, please try another file name.")
        write_to = out_file("\nWhat is the name of the file you'd like to write to? ==>")
        transpose()
        encipher.close()
        write_to.close()
        print("\nYour file has been transposed\n")
    if choice == 2:
        decipher = in_file("\nWhat is the name of the file you'd like to decipher? ==>", "Could not find the file specified, please try another file name.")
        write_to = out_file("\nWhat is the name of the file you'd like to write to? ==>")
        untranspose()
        decipher.close()
        write_to.close()
        print("\nYou file has been untransposed\n")
    if choice == 3:
        file_transposition = False

    
