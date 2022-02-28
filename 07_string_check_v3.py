

# function goes here
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