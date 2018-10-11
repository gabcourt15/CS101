########################################################################
##
## CS 101
## Program 5
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : We need a program to apply a filter so we can upload pictures to instagram.
##
## ALGORITHM : 
##      1.	Display options
##          a.	(1) Convert an image to grayscale
##          b.	(2) Convert an image to vintage
##          c.	(3)Quit
##              i.	If user enters input other than 1, 2, or 3 warn user and return to step 1a
##              ii.	If user enters 1, skip to step 2
##              iii.	If user enters 2, skip to step 3
##              iv.     If user enters 3, skip to step 4
##      2.	Ask for in file name
##          a.	If file name not found, warn user and return to step 2
##          b.	If file name is found, ask user to enter the name of the out file
##          c.	Convert the in file and write to out file by reading over the file contents of in file and weighting each color value
##          d.	Tell user the deed has been done and return to menu in step 1
##      3.	Ask for in file name
##          a.	If file name not found, warn user and return to step 3
##          b.	If file name is found, ask user to enter the name of the out file
##          c.	Convert the in file and write to the out file by reading over the file contents of the in file and darken the blue color value
##          d.	Tell user the deed has been done and return to menu in step 1
##      4.	End the program.
##
## 
##
## ERROR HANDLING:
##
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#FUNCTIONS
def options_menu(prompt, min, max, error_message):
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
    """Asks user for valid file name"""
    while True:
        try:
            file_name = input(prompt)
            file = open(file_name)
            line1 = file.readline().strip()
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            if line1 != "P3": #Checks to see if first line contains P3
                print("The files first line must be P3")
                continue
            elif line3 != "255": #Checks to see if color depth is 255
                print("The files color depth must be 255")
                continue
            return file_name
        except FileNotFoundError:
            print(error_message)
        except IOError:
            print(error_message)

def out_file(prompt, error_message):
    """Gets file to be written to from user"""
    while True:
        try:
            file_name = input(prompt)
            write = open(file_name, "w")
            return write
        except OSError:
            print(error_message)

def reading_header():
    """Reads header to write to new file"""
    line1 = read_file.readline().strip()
    write_file.write(line1 + "\n")
    line2 = read_file.readline().strip()
    write_file.write(line2 + "\n")
    line3 = read_file.readline().strip()
    write_file.write(line3 + "\n")

def gray_scale():
    """Converts file to grayscale"""
    file = read_file.readlines()
    line_num = 4 #initializes line number
    for line in file:
        line = int(line.strip())
        if line_num % 3 == 0: #Every third line is blue
            blue = line * 0.114
            new_value += blue #tabulates the average value
            write_file.write(str(new_value) + "\n") #replaces each RGB value with the new average value
            write_file.write(str(new_value) + "\n")
            write_file.write(str(new_value) + "\n")
        elif line_num %3 != 0: #If the line isnt blue
            if (line_num + 1) % 3 == 0: #The line is green
                green = line * 0.587
                new_value += green #tabulates the average value
            if (line_num + 2) % 3 ==0: #The line is red
                red = line * 0.299 
                new_value = red #tabulates the average value
        line_num += 1 # adds one to the line number before continuing the loop for the next line
    
def vintage():
    """Converts file to vintage"""
    line_num = 4 #initializes line number
    file = read_file.readlines()
    for line in file:
        line = line.strip()
        line = int(line)
        if line_num % 3 == 0: #every third line is blue
            new_line = line * .5 #changes value of blue lines
        elif line_num % 3 != 0: #every other line
            new_line = line #value is unchanged
        write_file.write(str(new_line) + "\n")
        line_num += 1#adds one to updates line number before continuing loop to the next line

#MAIN PROGRAM
convert_file = True
while convert_file == True:
    choice = optns_menu("What would you like to do?\n1. Convert image to GrayScale\n2. Convert image to Vintage\n3. Quit ==>", 1, 3, "You must enter 1, 2, or 3\n")
    if choice == 1: #grayscale
        read_file = in_file("Enter a valid file name to convert. ==>", "The file you specified does not exist, please enter a valid file name.")
        read_file = open(read_file)
        write_file = out_file("What is the name of the file you want to save to? ==>", "The file you specified is invalid")
        reading_header()
        gray_scale()
        read_file.close()
        write_file.close()
    elif choice == 2: #vintage
        read_file = in_file("Enter a valid file name to convert. ==>", "The file you specified does not exist, please enter a valid file name.")
        read_file = open(read_file)
        write_file = out_file("What is the name of the file you want to save to? ==>", "The file you specified is invalid")
        reading_header()
        vintage()
        read_file.close()
        write_file.close()        
    else: #quit 
        convert_file = False
    
