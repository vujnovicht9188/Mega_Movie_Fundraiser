# functions

from tkinter.tix import MAX


def not_blank(question, error): 
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response
        else:
            print(error)


# start of loop

# initialise loop so that is runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    # get details
    name = not_blank("name: ", "<error> name cannot be blank")
    if name != 'xxx':  
        count += 1
        if count == 4:
            print("you have only 1 seat left!")
        else:   
            print ("you have {} seats "
            "left".format(MAX_TICKETS - count))

        print()

if count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else :
    print("You have sold {} tickets. \n"
    "There are {} places still available"
    .format(count, MAX_TICKETS - count))