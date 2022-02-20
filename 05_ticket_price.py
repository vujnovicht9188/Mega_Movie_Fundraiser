profit = 0

name = ""
while name != "xxx":

    name = imput("Name: ") #replace with function call

    # If name is exit code break out of loop
    if name == "xxx":
        break

    age = int(input("Age: "))

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5