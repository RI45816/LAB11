# File:    capitals.py
# Started: by Dr. Gibson
# Author:  Uzoma Uwanamodo
# Date:    11/16/2016
# Section: 05
# E-mail:  uu3@umbc.edu
# Description:
#   This file contains python code that reads in a list of
#   states and their capitals, stores it in a dictionary,
#   and then allows the user to list all options (states),
#   or to show the capital of a specified state.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 

QUIT     = "exit"
SHOW_ALL = "list"


# convertToDict() takes in the filename and converts to a dict
# Input:          a file object
# Output:         a dictionary containing the file contents
def convertToDict(fileContents):
    dict1 = {}

    # write the rest of the function (including the return)
    for line in fileContents:
        splitLine = line.strip().split(",")
        dict1[splitLine[0]] = splitLine[1]

    return dict1

def main():

    stateCapFile = open("stateCaps.txt")
    # a function call to convertToDict goes here
    statesCaps = {}
    statesCaps = convertToDict(stateCapFile)
    
    stateCapFile.close()
    
    STATES = statesCaps.keys()
    
    print("Welcome to the State Capital Lookup System")
    # message with all the prompts for the user
    msg = "\n\tPlease enter the state you want the capital of.\n" + \
        "\t(Use '" + SHOW_ALL + "' for choices, or '" + \
        QUIT + "' to quit): "

    choice = input(msg)

    # this should be a while loop that runs until the user chooses to "exit"
    # MAKE SURE TO USE THE CONSTANTS DEFINED AT THE TOP OF THE FILE!!!
    while choice != QUIT:
        # inside the loop: if the user enters "list", show all the states
        print("The capital of %s is %s" % (choice, statesCaps[choice]) if choice in statesCaps else "\n".join(STATES) if choice == SHOW_ALL else "Sorry, %s is not a state" % choice)
        choice = input(msg)


    print("Thank you for using the State Capital Lookup System!")
main()

    

