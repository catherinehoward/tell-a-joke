def printJoke(myNumber):
    told = 'false'
    while told == 'false':
        if  number == 1:
            print("Why did the chicken cross the road? ")
            input()
            print("To get to the other side")
            told = 'true'
        elif number == 2:
            print("What do you call a guy lying on your doorstep?")
            input()
            print("Matt")
            told = 'true'
        elif number == 3:
            print("What do you call a gorilla with bananas in its ears?")
            input()
            print("Anything you like he can't hear you.")
            told = 'true'
        elif number == 4:
            print("What do you call a fish with no eyes?")
            input()
            print("A fsh")
            told = 'true'
        elif number == 5:
            print("Why don’t polar bears eat penguins?")
            input()
            print("Because they can’t get the wrappers off.")
            told = 'true'
        else:
            print("Please enter a number between 1 and 5 and try again")
#   End of function

print("I'm going to tell you a joke")
#Ask the user for a number
number = int(input("Pick a number between 1 and 5 "))
printJoke(number)

