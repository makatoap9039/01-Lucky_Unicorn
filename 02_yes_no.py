show_instructions = ""
while show_instructions.lower()  != "xxx":

    # ask users if they have played before
    show_instructions = input("have you played this before?").lower()
    # if they say yes, output program continues
    if show_instructions == "yes":
        print("program continues")

    elif show_instructions == "no":
        print("display instructions an then continue code")

    # if they say y out put program continues
    elif show_instructions == "y":
        print ("program continues")

    # if they say no, output display instructions
    else:
        print("please answer yes or no")

