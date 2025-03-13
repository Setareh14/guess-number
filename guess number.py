import random 

def number_guessing ():
    number_guessing = random.randint(1,100)
    luck_of_play = 5
    
    print('<< Start number guessing game >> \n Guess a number between 1 and 100')
    
    for luck_of_play in range (luck_of_play):
        guess = int(input(f'luck_of_play {luck_of_play + 1 } :'))
        
        if  guess == number_guessing :
           print (' you win ! ')
           return
        elif guess < number_guessing:
           print (' say a bigger number ')
        else:
            print('say a smaller number')
        
    print(f'you did not say it right \n Right number is { number_guessing }')    
        
number_guessing()        
        
        