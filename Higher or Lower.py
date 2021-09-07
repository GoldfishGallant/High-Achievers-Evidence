from random import randint
import time
global guesses
global target
target = 0
guesses = 0
def try_again():
    global guesses
    retry = input("Would you like to play again?[Y/N]\n")
    if retry == "Y" or retry == "y" or retry == "yes" or retry == "Yes":
        guesses = 0
        start()
    elif retry == "N" or retry == "n" or retry == "no" or retry == "No":
        guesses = 0
        menu()  
    else:
        print ("--Please enter either Y or N.--\n(Yes or No)\n")
        try_again()

def hard():
    global target
    global guesses
    print ("You have "+str(guesses)+" guesses left!\n")
    if guesses <= 0:
        print ("Sorry you've run out of guesses.")
        try_again()
                
    elif guesses >= 0:
        try:
            guess = int(input("Please choose a number from 1 to 10,000: "))
            guesses = guesses -1
            if guess > target:
                print ("\nLower\n")
                hard()
            elif guess < target:
                print ("\nHigher\n")
                hard()
            elif guess == target:
                print ("You win!")
                try_again()
        except ValueError:
            print ("\n--Please only enter a number--\n")
            hard()

def medium():
    global target
    global guesses
    print ("You have "+str(guesses)+" guesses left!\n")
    if guesses <= 0:
        print ("Sorry you've run out of guesses.")
        try_again()   
    elif guesses >= 0:
        try:
            guess = int(input("Please choose a number from 1 to 1,000: "))
            guesses = guesses -1
            if guess > target:
                print ("\nLower\n")                
                medium()
            elif guess < target:
                print ("\nHigher\n")
                medium()
            elif guess == target:
                print ("You win!")
                try_again()

        except ValueError:
            print ("\n--Please only enter a number--\n")
            medium()
    
def easy():
    global target
    global guesses
    print ("You have "+str(guesses)+" guesses left!\n")
    if guesses <= 0:
        print ("Sorry you've run out of guesses.")
        try_again()
                
    elif guesses >= 0:
        try:
            guess = int(input("Please choose a number from 1 to 100: "))
            guesses = guesses -1
            if guess > target:
                print ("\nLower\n")
                easy()
            elif guess < target:
                print ("\nHigher\n")
                easy()
            elif guess == target:
                print ("You win!")
                try_again()
        except ValueError:
            print ("\n--Please only enter a number--\n")
            easy()
            
def start():
    global guesses
    global target
    print ("Please select a dificulty.\n")
    difficulty = input ("1.Begginer (1-100) 10 Guesses\n2.Intermediate (1-1,000) 10 Guesses\n3.Expert (1-10,000) 15 Guesses\n")
    if difficulty == "1":
        target = (randint(1,100))
        guesses = 10
        easy()
    elif difficulty == "2":
        target = (randint(1,1000))
        guesses = 10
        medium()
    elif difficulty == "3":
        guesses = 15
        target = (randint(1,10000))
        hard()
    else:
        print ("--Please select one of the options listed.--\n")
        start()
        
def menu():
    global mistakes
    print ("Type the number next to the option you wish to select and hit enter.\n")
    play = input ("1.Play\n2.Instructions\n")
    if play == "1":
        start()
    elif play == "2":
        print ("In this game, our random number generator will choose a number at random.\nThen you will be asked to select a number, the game will output either")
        print ("Higher or Lower. Your goal is to input the random chosen number\nin a select amount of guesses.\n")
        input ("Press enter to continue\n")
        start()
    else:
       print ("--Please select one of the options listed.--\n")
       menu()
        
print ("Welcome to Higher or Lower!\n")
time.sleep(0.4)
menu()







