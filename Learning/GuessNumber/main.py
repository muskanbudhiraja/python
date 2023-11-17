import random

def guessNumber(random_no):
    guess_no=0
    while guess_no!=random_no:
        guess_no=int(input("enter a number:"))
        if guess_no<random_no:
            print("Sorry, No is too low!")
        elif guess_no>random_no:
            print("Sorry, No is too high!")
        else:
            print(f"Yay!! You have guessed the number {guess_no}")


random_no=random.randint(1,10)
print(random_no)
guessNumber(random_no)