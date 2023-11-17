import random
low=1
high=1000
def computerGuess(low,high):
    type='a'
    while type!='c':
        guessingNumber=random.randint(low,high)
        type=input(f"Is {guessingNumber} too high, too low or correct:")
        if(type=='h'):
            high=guessingNumber-1
        elif(type=='l'):
            low=guessingNumber+1
        else:
            print(f"Hurray!! Your number is {guessingNumber}")

computerGuess(low,high)