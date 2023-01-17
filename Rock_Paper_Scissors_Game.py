from random import choice                                             #Provides access to the choice method in the random module

number = input ('How many rounds do you want to play? ')                #Asks user how many rounds they want to play

while number.isnumeric() == False or int(number) == 0:                     #If user input is not a number or 0 it will repeat until a valid number is given
    number = input ('Invalid entry. Please insert an integer greater than 0: ')

def play():
    m=0                       #Initializes the while loop
    score = {'computer': 0, 'player': 0, 'tie': 0, 'invalid entry': 0}      #Initializes the score
    while m<int(number):

        computer_choice = choice(["rock", "paper", 'scissors'])         #Computer chooses rock, paper, or scissor randomly
        winner1 = 'player wins'
        winner2 = 'computer wins'
        player_choice = input ("Chose rock, paper, scissors: ")       #Player chooses rock, paper, scissors
    
        if player_choice!= "rock" and player_choice!= "paper" and player_choice!="scissors":           #Informs the player of an invalid entry
            print ("Invalid entry. Please try again")
            score['invalid entry']+=1
            m-=1
        elif (computer_choice == 'rock' and player_choice == 'paper') or (computer_choice == 'paper' and player_choice == 'scissors') or (computer_choice == 'scissors' and player_choice == 'rock'):  #Win conditions for a player
            print ("Player chose", player_choice, 'and computer chose', computer_choice, 'therefore', winner1)
            score['player']+=1
        elif (computer_choice == 'paper' and player_choice == 'rock') or (computer_choice == 'scissors' and player_choice == 'paper') or (computer_choice == 'rock' and player_choice == 'scissors'):  #Win conditions for the computer
            print ("Player chose", player_choice, 'and computer chose', computer_choice, 'therefore', winner2) 
            score['computer']+=1
        elif computer_choice == player_choice:    #Conditions for a tie
            print ('Both computer and player selected', player_choice)
            score['tie']+=1
        m+=1
    print (score)      #Gives the total score after all rounds are played
play()