###################################################
##              Made by Vojtěch Gistr            ##
##                                               ##
##           Code is available on GitHub:        ##
##      https://github.com/VojtaG/thunderMath    ##
##                                               ##
###################################################
import sys
import math
import time
import os

# creating global variables
global clear
global do

clear = lambda: os.system('cls')
do = True

def main():
    clear()
    print("This program finds the distance to a lightning strike in miles and kilometers.")
    print()

    # trying to get a real number, if it's not, program will write an error
    try:
        light = eval(input("Please enter the time in seconds since the lightning strike until you hear thunder "))
    except:
        clear()
        print('Hey! The input has to be a positive number!')
        time.sleep(5)
        return

    # checking if user is not lying
    if light > 50:
        clear()
        print('Bruh, stop lying to me dumbass..')
        time.sleep(5)
        return

    if light == 0:
        clear()
        print('Enjoy your funeral <3')
        time.sleep(5)
        return

    if light < 0:
        clear()
        print('Hey! The input has to be a positive number, not negative!')
        time.sleep(5)
        return

    # Math operations
    km = light * 343 / 1000
    miles = km * 0.621371
    print("The lightning strike was", round(miles, 2), "miles away /", round(km, 2), "kilometers away.")

    time.sleep(2)
    asking = True
    i = 0
    print()
    
    # creating while loop - asking if user want to continue at this program
    while asking:
        print("Do you wanna continue?")
        print()
        answer = input('Type "yes" or "no" ')

        if answer == "yes":
            asking = False
            return
        elif answer == "no":
            clear()
            asking = False
            do = False
            print('Thanks for using this program! I hope this at least a little bit encourages your laziness in math and logical thinking.\nProgram will be closed in 10secs')
            print()
            print('Program were made by Vojtěch Gistr, code is available on my GitHub -> https://github.com/VojtaG')
            time.sleep(10)
            return sys.exit()
        else:
            # checking if user didn't answer 5 times or higher, then program ends
            if i > 5:
                clear()
                print('Error, too many incorrect answers were entered.. Closing program')
                print()
                print('Program were made by Vojtěch Gistr, code is available on my GitHub -> https://github.com/VojtaG')
                time.sleep(10)
                return sys.exit()
            else:
                clear()
                print('The answer was incorrect.. Try it again')
                i += 1
                print()

## running while loop, almost infinite
while do == True:
    main()
