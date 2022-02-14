# start of loop

# initialise loop so that is runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

    if count == 4:
        print("you have only 1 seat left!")
    else:   
        print ("you have {} seats "
        "left".format(MAX_TICKETS - count))


    # get details
    name = input("name: ")
    count += 1
    print()

    if count == MAX_TICKETS:
        print("You have sold all the available tickets!")