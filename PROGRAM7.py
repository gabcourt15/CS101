########################################################################
##
## CS 101
## Program 7
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM : We need a way to generate the average and standard deviation of the feeling towards a word in movie reviews.
##
## ALGORITHM : 
##  1.	Display options
##      a.	(1) Get sentiment for all words in a file
##      b.	(2) Quit
##          i.	If user enters input other than 1 or 2 warn user and return to step 1
##          ii.	If user enters 1, skip to step 2
##          iii.	If user enters 2, skip to step 3
##  2.	If 1 is chosen, ask for word list file name
##      a.	If file name not found, warn user and return to step 2
##      b.	If file name is found,
##          i.	Open moviereviews.txt
##          ii.	Open word list file
##          iii.	Search through lines of moviereviews.txt for words in word list
##              a.	Create a dictionary for each word with the word being the key, and the scores being the values
##              b.	Calculate the average score and standard deviation of each word and store in new dictionary which has the word as the key and average score and standard deviation as values
##          iv.	Close moviereviews.txt
##          v.	Close word list file
##          vi.	Display sort options menu
##              a.	(1) Sort by average ascending
##                  i.	Print out results by averages low to high
##              b.	(2) Sort by average descending
##                  i.	Print out results by averages high to low
##              c.	(3) Sort by standard deviation ascending
##                  i.	Print out results by standard deviations low to high
##              d.	(4) Sort by standard deviation descending
##                  i.	Print out results by standard deviations high to low
##          vii.	Return to step one
##  3.	Quit program
## 
##
## ERROR HANDLING:
##
##
## OTHER COMMENTS:
##      Any special comments
##
#########################################################################FUNCTIONS
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
            return file_name
        except FileNotFoundError:
            print(error_message)
        except IOError:
            print(error_message)


def in_file_dict(in_file):
    """gets words from in file and places them into dictionary as keys"""
    word_list_dict = dict()
    for line in in_file:
        line = line.strip() #GET RID OF EXTRA SPACES
        word_list_dict[line] = list() #CREATE KEY FOR EACH LINE WITH EMPTY LIST AS VALUE
    return word_list_dict

def search_for_word(reviews, word_dict):
    """searches for words in reviews, adds review value as keys to word dictionary"""
    reviews = reviews.readlines() #READS LINES IN REVIEW FILE
    for line in reviews:
        for word in word_dict:
            if word.upper() in str(line[1:]).upper():
                word_dict[word].append(int(line[0])) #ADDS VALUE TO LIST ASSOCIATED WITH WORD IN DICTIONARY
    return word_dict

def occurrance(reviews, word_dict):
    """calculates the number of appearances for each word"""
    occurrance_dict = {}
    for value in word_dict:
        occurrance_dict[value] = len(word_dict[value])
    return occurrance_dict
        
def average(word_dict, occurrance_dict):
    """calculates the average review value for each word"""
    average_dict = {}
    for word in word_dict:
        total = 0
        for item in word_dict[word]:
            total += item #ADDS ALL THE VALUES TOGETHER
        average = total / occurrance_dict[word] #DIVIDE TOTAL BY OCCURANCE OF WORD
        average_dict[word] = average #ADDS WORD TO AVERAGE DICT WITH VALUE OF AVERAGE
    return average_dict

def std_dev(word_dict, average_dict):
    """calculates the standard deviation for each word"""
    std_dev_dict = {}
    for word in word_dict:
        numerator = 0
        denominator = 0
        for item in word_dict[word]:
            item = int(item)
            item -= average_dict[word] 
            item = item ** 2
            numerator += item
            denominator += 1
        std_dev = numerator / denominator
        std_dev_dict[word] = std_dev #ADDS WORD TO STD DEV DICT WITH VALUE OF STD DEV
    return std_dev_dict
            
    

running_program = True
while running_program == True:
    choice1 = options_menu("Python Sentiment Analysis\n1.Get sentiment for all words in file\n2. Quit\n==> ", 1, 2, "You must choose 1 or 2")
    if choice1 == 1:
        in_file = in_file("\nEnter the name of the file with words to score ==> ", "Could not find the file you specified")
        reviews = open("movieReviews.txt")
        in_file = open(in_file)
        word_dict = in_file_dict(in_file)
        word_dict= search_for_word(reviews, word_dict)
        occurrance_dict = occurrance(reviews, word_dict)
        average_dict = average(word_dict, occurrance_dict)
        std_dev_dict = std_dev(word_dict, average_dict)
        choice_2 = options_menu("\nHow would you like to sort the results?\n1.Sort by average ascending\n2.Sort by average descending\n3.Sort by standard deviation ascending\n4.Sort by standard deviation descending\n ==>", 1, 4, "You must select 1, 2, 3, or 4")
        print("Word" + " " * 13 + "Occurrence" + " " * 3 + "Avg Score" + " " * 5 + "Std Dev")
        print("=" * 51)
        for word in word_dict:
            print("{:<17s}{:>10.0f}{:>12.4f}{:>12.4f}".format(word, occurrance_dict[word], average_dict[word], std_dev_dict[word]))
            
        
    else:
        running_program = False
