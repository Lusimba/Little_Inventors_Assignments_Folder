import random
import sys
wordList = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat","hello","play","phone"
           ]
guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
def start():
    print("Hello!\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("Permision Denied")
        else:
            break
start()
def starter():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gameChoice = input("Is It?\n").upper()

        if gameChoice == "YES" or gameChoice == "Y" or gameChoice == "YE":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue
starter()
def create_word():
    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("The word You need to guess has", length_word, "characters")
    print(guess_word)
def guessing():
    guess_taken = 1

    while guess_taken <= 10:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage: #checking if letter has been already used
            print("You have already tryed that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word): 
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 11:
                    print("You lost :(! The secret word was",secretWord)
create_word()
guessing()

print("Game Over!")