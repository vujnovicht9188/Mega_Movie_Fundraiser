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
Name = ""
count = 1
MAX_TICKETS = 5

while name != "xxx" and count <= MAX_TICKETS:

    # get details
    name = not_blank("name: ", "<error> name cannot be blank")
    count += 1