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


# checks for valid string
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # get full name of snack and put in
            # in titile case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen options is not valid, set is_valid to no
        else:
            is_valid = "no"
    
    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

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

def get_snack():

    # regular expression to find if item starts with a number
    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["m&ms", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "h2o", "d"],
        ["orange juice", "oj", "tenthplace", "e"]
        
    ]

    # holds snack order for a single user
    snack_order = []

    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []

        # ask user for a desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx" or desired_snack == "n":
            return snack_order


        # if item has a number, seperate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "too many"

        # add snack AND amount to list...
        snack_row.append(amount)
        snack_row.append(snack_choice)

        amount_snack = "{} {}".format(amount, snack_choice)

        if snack_choice == "invalid choice":
            print("invalid choice")

        elif snack_choice == "too many":
            print()

        else:
            print("Snack Choice:", amount_snack)


        # check that snack if not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice" and snack_choice != "too many":            
                    snack_order.append(snack_row)

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

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

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# lists to store summary data...
summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                   "Orange Juice", "Snack Profit", "Ticket Price", 
                   "Total Profit"]

summary_data = []

# store surcharge multiplier
surcharge_mult_list = []

yes_no = [
    ["yes","y"],
    ["no", "n"]

]

# list of valid responses for payment method
pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# data frame dictionary
movie_data_dict = {
    'Name': all_names, 
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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
    snack_order = get_snack()

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    # print(snack_lists)
    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    
    # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("please choose a payment method (cash / credit) ")
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0
    

    surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snacks / payment loop


# create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'Sub Total'
# fill it price for snacks and ticket

movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks'] 


movie_frame['Surcharge'] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame['Total'] = movie_frame['Sub Total'] + \
    movie_frame['Surcharge']

# Print details...

movie_frame = movie_frame.reindex(columns=['Popcorn', 'M&Ms', 'Pita Chips', 'Water', 'Orange Juice', 'Ticket', 'Snacks', 'Sub Total','Surcharge','Total'])


# Set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2

# Get ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit

# format dollar amounts and add to list...
dollar_amounts = [snack_profit, ticket_profit, total_profit]
for item in dollar_amounts:
    item = "{:.2f}".format(item)
    summary_data.append(item)

# create summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index('Item')

# set up columns to be printed
pandas.set_option('display.max_columns', None)

# *** Pre Printing / Export ***
# Format currency values so they have $'s

# Ticket Details formatting (uses currncy function)
add_dollars = ['Ticket', 'Snacks', 'Surcharge', 'Total', 'Sub Total']
for item in add_dollars:
    movie_frame[item] = movie_frame[item].apply(currency)

# Write each frame in seperate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")


print()
print("*** Ticket Snack Information ***") 
print("Note: for all full details, please see the excel file called T/S Info")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total', 'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)
print()


# Calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all avaliable tickets!")
else:
    print("You have sold {} tickets. \n" "There are {} places still available".format(ticket_count, MAX_TICKETS - ticket_count))

print()