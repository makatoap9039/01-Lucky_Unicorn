show_instructions = ""

while show_instructions.lower() != "xxx":

    # ask users if they have played before
    show_instructions = input("have you played this before?").lower()
    # if they say yes, output program continues

    if show_instructions == "xxx":
        break

    elif show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions an then continue code")

    # if they say no, output display instructions
    else:
        print("please answer yes or no")

print("we are done")
