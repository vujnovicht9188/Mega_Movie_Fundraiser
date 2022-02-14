# functions

# checks that ticket name is not blank
def not_blank(question, error): 
    valid = False

    while not valid:
        response = input(question)

        if response !="":
            return response
        else:
            print(error)

# ask user for name and age       
name = not_blank("Name: ", "<error> Please put in your name.")

age = not_blank("Age: ", "<error> Please input age." )
