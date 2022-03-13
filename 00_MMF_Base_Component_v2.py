# import statements 
import re
import pandas


# functions go here

# check that name is not blank
def not_blank(question, error): 
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response
        else:
            print(error)


# checks for integer more than 0
def int_check(question, error):
    valid = False

    while not valid:

        # ask user for number an check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else: 
                return response 

        # if an integer is not entered display an error
        except ValueError:
            print(error)

# checks number of tickets left and warns user
# if maximum is being approached 
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if tickets_sold < ticket_limit - 1:
        print("You have {} seats left".format(ticket_limit - tickets_sold))


    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!!! ***")

    return ""


# Gets ticket price based on age 
def get_ticket_price():

    # Get age (between 12 and 130)
    age = int_check("Age: ", "<error> please enter an age between 12 and 130")

    # check that age is valid...
    if age < 12:
            print ("Sorry, only people 12 or over can purchase a ticket.")
            return "invalid ticket price"
    elif age > 130:
            print ("Sorry, that age is very old. It looks like a mistake.")
            return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# ***** MAIN ROUTINE *****

# Set up dictionaries / lists needed to hold up data

# initialise loop so that it runs at leats once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# initailise lists ( to make data-frame in due course)
all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}


# ask user if they have used the program before & show instructions

# loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

    # check numbers of ticket limit has not been exceeded...
    check_tickets(ticket_count, MAX_TICKETS)

    # *** Get details for each ticket ***

    # get name (can't be blank)
    name = not_blank("Name: ", "Sorry, name cannot be blank")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # If age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price
    
    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # get snacks

    # get payment method (is: work out if surcharge is needed)

# End of tickets / snacks / payment loop

# Print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all avaliable tickets!")


