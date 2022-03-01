# function goes here
from operator import is_


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


valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes","y"],
    ["no", "n"]

]

# holds snack order for a single user
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# if they say yes ask what snacks they want
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for a desired snack and put it in lowercase
        desired_snack = input("Snack").lower()

        if desired_snack == "xxx":
            break


    # check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)

    # add snack to list...

    # check that snack if not the exit code before adding
    if snack_choice != "xxx" and snack_choice != "invalid choice":
        snack_order.append(snack_choice)

# show snack orders
print ()
if len(snack_order) == 0:
    print(" Snacks Ordered: None")

else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)



    for var_list in valid_snacks:

        # if the snack is in one of the lists, return the full name 
        if desired_snack in var_list:

            # Get full name of snack and put it 
            # in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break
    
        # if the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "no"
        
    # if the snack is not OK - ask question again.'
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("Invalid choice")