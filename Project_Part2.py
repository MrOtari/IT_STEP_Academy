### Guessing Game

import random                         #import random library to choose the random number later

def guess_number():
    number = random.randint(0,100)    #computer chooses number between 0 and 100
    max_attempts = 3                  #maximum amount of attempts is defines as 10
    attempts = 0                      

    while attempts < max_attempts:    #player can try to guess number less than maximum amount of attempts
        try:                          #try the following code at first
            x = int(input())          #player writes numbers
            if x > 100 or x < 0:      #but if the number is out of range (0,100), programme prints error and asks player to enter the number in above-mentioned range 
                print("Enter the integer between 0 and 100")
                continue
            attempts += 1                 #game counts the number of attempts
            if x < number:                #if number is less than number defined in game, programme gives hint to say higher number and vice versa
                print("Higher number")
            elif x > number:
                print("Lower number")
            else:                         #once the player will guess the number, loop stops and programe prints that player has won
                print("Win")
                return
        except ValueError:                #if condition mentioned in try section is not satisfy, print the following sentenc
            print("Enter the integer between 0 and 100")

    print(f"Attempts are over. The number was {number}.")       #if player cannot guess the number during the maximum amount of attempts, programme informs player that attempts are over
    
guess_number()  
    


### Rock, Paper, Scissors

options = ["Rock", "Paper", "Scissors"]    #make a list of options

while True:
    player_1 = input("player_1 chose: ")   #make a choice of player 1
    if player_1 not in options:
        print("Incorrect word")
        continue
    else:
        break
        
player_2 = random.choice(options)        #use random.choice for player 2 to randomly choose from options list
print("player_2 chose:", player_2)       #Store the random choice of player 2 as a variable

if player_1 == "Rock" and player_2 == "Scissors":     #by using if and elif blocks write down the all options that can be chosen by the players
    print("Won player_1")                             #print the results
elif player_1 == "Rock" and player_2 == "Paper":
    print("Won player_1")
elif player_1 == "Paper" and player_2 == "Scissors":
    print("Won player_2")
elif player_1 == "Scissors" and player_2 == "Paper":
    print("Won player_1")
elif player_1 == "Scissors" and player_2 == "Rock":
    print("Won player_2")
elif player_1 == "Paper" and player_2 == "Rock":
    print("Won player_2")
elif player_1 == player_2:
    print("Draw")