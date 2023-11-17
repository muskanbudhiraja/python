import random


def game():
    userChoice = input("choose 'r' for rock, 'p' for paper, 's' for scissors:")
    compChoice = random.choice(['r', 'p', 's'])
    print(compChoice)
    if userChoice == compChoice:
        return ('Its a tie!!')
    if is_win(userChoice, compChoice):
        return ('U win !!')
    return 'U Lost !!'
    # else:
    #     winner(userChoice, compChoice)


def winner(user, comp):
    if ((user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p')):
        print('U win !!')
    else:
        print('I win !!')


def is_win(user, comp):
    if ((user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p')):
        return True
    return False


print(game())
