from words import data
import random


def is_valid_word():
    word = random.choice(data)
    while '-' in word or ' ' in word:
        return random.choice(data)
    return word


def hangman():
    word = is_valid_word()
    print(word)
    used_alphabets = set()
    word_alphabets = set(word)

    while len(word_alphabets) > 0:
        print('U have used these letters:', ' '.join(used_alphabets))
        user_alphabet = input("guess the letter:")

        if user_alphabet in word_alphabets:
            word_alphabets.remove(user_alphabet)
        elif user_alphabet in used_alphabets:
            print("U have already entered these letters, try something new!")
        else:
            print("wrong guess! try something else")
        used_alphabets.add(user_alphabet)

        word_list = [
            letter if letter in used_alphabets else '_' for letter in word]
        print(' '.join(word_list))


hangman()
