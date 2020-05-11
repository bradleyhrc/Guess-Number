import random
from time import sleep

#Generate a random number from 1 to 10
randomnumber = random.randint(1, 10)

tries = 0

name = input("Hello, what's your name? \n")

print("Ok {}, guess a number between 1 and 10. I'll give you three tries. :)".format(name.title()))

#While loop that will only happen thrice. One is added to tries before each guess and can thus keep track
while tries < 3:
    tries += 1
    guess = int(input("Take a guess: "))
    #If correct number
    if guess == randomnumber:
        print("Congratulations! You guessed my number in {} tries, you win! \nThat was fun! Feel free to play again. :) ".format(tries))
        break
    #This is to break from the loop and avoid a hint from showing on the last try if it is wrong
    elif (guess < randomnumber or guess > randomnumber) and tries >= 3:
        break
    #Gives a hint
    elif guess > randomnumber:
        print("Too high! Try again: ")
    #Gives a hint
    elif guess < randomnumber:
        print("Too low! Try again: ")

#This is the message that will display if the number could not be guessed in three turns
if tries >= 3:
    print("Sorry, you couldn't guess the number {} fast enough. Try again next time! :) ".format(randomnumber))

#Waits 1.5 seconds before urging the player to close the program
sleep(1.5)
input("Press Enter to close program. ")
