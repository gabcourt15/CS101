########################################################################
##
## CS 101
## Program 6
## Gabby Courtney
## gac6y5@mail.umkc.edu
##
## PROBLEM :
##
## ALGORITHM : 
##    1. Ask user for name of stock purchased
##      a. Convert to all upper case
##          i. If name entered is found, skip to step 2
##          ii. If name entered is not found, warn user and return to step 1
##          iii. If quit is entered, end program
##    2. Open corresponding stock csv file
##    3. Ask user for stock purchase date
##      a. If date is correctly formatted, skip to step 4
##      b. If date is incorrectly formatted, warn user and return to step 3
##    4. Ask user for date stock was sold
##      a. If date is correctly formatted, skip to step 5
##      b. If date is incorrectly formatted, warn user and return to step 4
##    5. Convert each line of csv file to list
##    6. Search through lists for matching start date
##      a. If found, skip to step 7
##      b. If not found, warn user and return to step 1
##    7. Ask user how many stocks were purchased on start date
##      a. If user enters a valid integer, skip to step 8
##      b. If user enters invalid input, warn user and return to step 7
##    8. Search through tuples for matching end date
##      a. If found, skip to step 9
##      b. If not found, warn user and return to step 1
##    9. Output formatted results
##    10. Close csv file
##    11. Return to step 1
##  
## ERROR HANDLING:
##
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#IMPORTING MODULES
import datetime
import csv

#FUNCTIONS

def name_of_stock(prompt, error_message):
    """Gets valid name of stock from user"""
    while True:
        try:
            stock_name = input(prompt).upper()
            if stock_name == "AAPL" or stock_name == "ACN" or stock_name == "BIDU" or stock_name == "CGI" or stock_name == "GOOGL" or stock_name == "INFN" or stock_name == "MSFT" or stock_name == "TSLA" or stock_name == "QUIT":
                return stock_name
            else:
                print(error_message)
        except ValueError:
            print(error_message)

                
def stock_purchase_date(prompt, error_message):
    """Gets valid stock purchase date from user"""
    while True:
        try:
            date = input(prompt)
            valid_date = datetime.datetime.strptime(date, "%m/%d/%Y") #CHANGES STRING TO DATE TIME FORMAT
            return valid_date
        except ValueError:
            print(error_message)


def stock_sold_date(prompt, error_message):
    """Gets valid stock sold date from user"""
    while True:
        try:
            date = input(prompt)
            valid_date = datetime.datetime.strptime(date, "%m/%d/%Y") #CHANGES STRING TO DATE TIME FORMAT
            return valid_date
        except ValueError:
            print(error_message)


def list_of_lists_of_lines(file_name):
    """Creates a list of lists in which the inner lists contain the date, opening price, closing price, and split ratio"""
    list_of_lines =[]
    for line in file_name:
        line_list = list(line.split(","))
        line_list[-1] = line_list[-1].strip()
        line_list.pop(2) #REMOVES HIGH VALUE
        line_list.pop(2) #REMOVES LOW VALUE
        line_list.pop(3) #REMOVES VOLUME
        line_list.pop(3) #REMOVES EX-DIVIDEND
        list_of_lines.append(line_list)
    return list_of_lines


def search_for_start_date(list_name, purchase_date):
    """searches list of lists to find matching purchase date"""
    for item in list_name:
        if item[0] == purchase_date.strftime("%m/%d/%Y"):
            return item
    return None


def search_for_end_date(list_name, sold_date):
    """searches list of lists to find matching sold date"""
    for item in list_name:
        if item[0] == sold_date.strftime("%m/%d/%Y"):
            return item
    return None


def number_of_stocks(prompt, error_message):
    """Gets valid number of stocks bought from user"""
    while True:
        try:
            number = int(input(prompt))
            if number < 1:
                print(error_message)
                continue
        except ValueError:
            print(error_message)
            continue
        return number


def seperate_date(list_to_be_seperated):
    """Makes list of just dates"""
    date_list = []
    for item in list_to_be_seperated:
        date_list.append(item[0]) #ADDS FIRST ELEMENT OF EACH LIST INSIDE THE LIST TO BE SEPERATED TO A DATE LIST
    return date_list


def seperate_open_value(list_to_be_seperated):
    """Makes list of just open values"""
    open_value_list = []
    for item in list_to_be_seperated:
        open_value_list.append(item[1]) #ADDS SECOND ELEMENT OF EACH LIST INSIDE THE LIST TO BE SEPERATED TO A OPEN VALUE LIST
    return open_value_list


def seperate_close_value(list_to_be_seperated):
    """Makes list of just close values"""
    close_value_list = []
    for item in list_to_be_seperated:
        close_value_list.append(item[2]) #ADDS THIRD ELEMENT OF EACH LIST INSIDE THE LIST TO BE SEPERATED TO A CLOSE VALUE LIST
    return close_value_list


def seperate_split_ratio(list_to_be_seperated):
    """Makes list of just split ratios"""
    split_ratio_list = []
    for item in list_to_be_seperated:
        split_ratio_list.append(item[3]) #ADDS FOURTH ELEMENT OF EACH LIST INSIDE THE LIST TO BE SEPERATED TO A SPLIT LIST
    return split_ratio_list
            

def stock_amount(split_list, num_of_stocks_bought):
    """Finds new number of stocks owned"""
    for item in split_list:
        if float(item) > 1:
            num_of_stocks_bought *= float(item) 
    return int(num_of_stocks_bought)
#MAIN PROGRAM

running_program = True
while running_program == True:
    stock = name_of_stock("Enter the name of the stock purchased.  Enter quit to exit. ==> ", "Could not find the stock.  Please enter another stock name.\n")
    if stock == "AAPL" or stock == "ACN" or stock == "BIDU" or stock == "CGI" or stock == "GOOGL" or stock == "INFN" or stock == "MSFT" or stock == "TSLA":
        stock_file = open(stock + ".csv")
        purchase_date = stock_purchase_date("Enter the date the stock was purchased. ==> ", "You entered an incorrect date, please re-enter in the following format. MM/DD/YYYY\n")
        sold_date = stock_sold_date("Enter the date the stock was sold. ==> ", "You entered an incorrect date, please re-enter in the following format. MM/DD/YYYY\n")
        stock_file.readline() #READ HEADER LINE
        list_of_lines = list_of_lists_of_lines(stock_file)
        valid_start_date = search_for_start_date(list_of_lines, purchase_date)
        if valid_start_date == None:
            print("Could not locate the start date you entered.\n")
            continue
        num_stocks_bought = number_of_stocks("How many stocks were purchased on start date? ==> ", "You must enter a valid number")
        valid_end_date = search_for_end_date(list_of_lines, sold_date)
        if valid_end_date == None:
            print("Could not locate the end date you entered.\n")
            continue
        date_list = seperate_date(list_of_lines)
        open_value_list = seperate_open_value(list_of_lines)
        close_value_list = seperate_close_value(list_of_lines)
        split_ratio_list = seperate_split_ratio(list_of_lines)
        start_index = date_list.index(purchase_date.strftime("%m/%d/%Y"))
        end_index = date_list.index(sold_date.strftime("%m/%d/%Y"))
        split_list = split_ratio_list[start_index:end_index] #CREATES SLICE LIST OF SPLITS BETWEEN THE START AND END DATES
        owned_stocks = stock_amount(split_list, num_stocks_bought)
        open_price = float(open_value_list[start_index])
        close_price = float(close_value_list[end_index])
        total_spent = open_price * num_stocks_bought
        total_earned = close_price * owned_stocks
        total_revenue = abs(total_spent - total_earned)
        print("")
        print("{:18.6s}{:13.4s}{:16.6s}{:9.5s}{:11.11s}".format("Action", "Date", "Shares", "Price", "Total Price"))
        print("===================================================================")
        print("{:12s}{:10s}{:15.1f}{:15.2f}{:15.2f}".format("Buy", purchase_date.strftime("%m/%d/%Y"), num_stocks_bought, open_price, total_spent))
        print("{:12s}{:10s}{:15.1f}{:15.2f}{:15.2f}".format("Sold", sold_date.strftime("%m/%d/%Y"), owned_stocks, close_price, total_earned))
        print("===================================================================")
        print("{:67.2f}".format(total_revenue))
        print("")
        stock_file.close()
    else:
        running_program = False

