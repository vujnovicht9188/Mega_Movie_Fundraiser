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




def int_check(question, error):

    valid = False

    while not valid:

        # askuser for number an check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else: 
                return response 

        # if an integer is not entered display an error
        except ValueError:
            print(error)


# main routine goes here


# start of loop

# initialise loop so that is runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0



while name != "xxx" and ticket_count < MAX_TICKETS:

    # get details

    # Get name (can't be blank)
    name = not_blank("Name: ", "<error> name cannot be blank")
    if name != 'xxx':  
    

        # check that age is 12 - 130
        age = int_check("Age: ", "Please enter a whole number between 12 and 130")

        # check if age is valid
        if age < 12:
            print ("Sorry, only people 12 or over can purchase a ticket.")
            continue
        elif age > 130:
            print ("Sorry, that age is very old. It looks like a mistake.")
            continue 
    else:
        break

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1

    # adds cost of ticket to total cost
    ticket_sales += ticket_price

    # checks if there is one seat left
    if ticket_count == 4:
        print("you have only ONE seat left!!")
    # tells user how many seats are left
    else:   
        print ("you have {} seats "
        "left".format(MAX_TICKETS - ticket_count))

    print()
    # end of ticket loop

# calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Profit from Tickets: ${:.2f}".format(ticket_profit))

# tell user if they have sold
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else :
    print("You have sold {} tickets. There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))