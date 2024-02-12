
### MODULES ###

import os
import random

### WORD LIST ###
wordlist = {"dog":"it barks","cat":"it meows","bird":"it flies","owl":"it hoots","giraffe":"it has a long neck"}


### FUNCTIONS ###

def word_split(word):
    word_split = []
    for letter in word:
        word_split.append(letter)
    return(word_split)

def blanks_progress(word):
    progress = []
    for letter in word:
        progress.append("_")
    return progress

def hangman_progress(index):
    hangmanpics = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    hangman_stage = hangmanpics[index]
    return hangman_stage

def show_progress(blanks,hangman):
    os.system('cls')
    print(blanks)
    print(hangman)


### MAIN PROGRAM ###

word = random.choice(list(wordlist.keys()))
word = word_split(word)

blanks = blanks_progress(word)

hangman_index = 0
game_over = hangman_progress(7)


while True:
    hangman_stage = hangman_progress(hangman_index)
    
    show_progress(blanks,hangman_stage)
    userguess = input("Enter a single letter to guess a letter in the word. Type '1' for a hint. Type '2' to quit. ")

    if len(userguess) > 1:
        print("Your entry cannot be less than or greater than 1 character in length. Please try again.")
        continue
    
    else:
        if userguess in word:
            index = word.index(userguess)
            word[index] = "_"
            blanks[index] = userguess
        else:
            hangman_index += 1
        
        if hangman_index == 7 or userguess == 2:
            show_progress(blanks,game_over)
            print("GAME OVER")
            break
        elif "_" not in blanks:
            show_progress(blanks,hangman_stage)
            print("You win!")
            break

    

        