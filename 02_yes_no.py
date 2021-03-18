#functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"

        elif  response == "n" or response == "no":
            return "no"

        else:
            print("Please enter yes or no")


show_instructions = ""
while show_instructions.lower()  != "xxx":

    # ask users if they have played before
    show_instructions = yes_no("have you played this before?")
    # if they say yes, output program continues
    if show_instructions == "yes":
        print("program continues")

    else:
        print("display instructions an then continue code")

    print()


