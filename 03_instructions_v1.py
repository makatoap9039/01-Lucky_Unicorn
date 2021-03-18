
#functions
def yes_no(question):

 def instructions():
    print("****How to Play****")
    print("the rules of the game go here")
    print()
    return ""


    valid = False
    while not valid:
        response = input(question).lower()

        if response == "y" or response == "yes":
            return "yes"

        elif  response == "n" or response == "no":
            return "no"

        else:
            print("Please enter yes or no")


# Main Routine
instructions = yes_no("have you played this game before?")

print("You chose {}".format(instructions))
print()
having_fun = yes_no("are you having fun?")
print("you said {} to having fun".format(having_fun))
