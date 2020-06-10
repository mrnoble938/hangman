# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:37:24 2020

@author: noble
"""
import random
import os

def randword(file:str) -> str:
    '''
    Parameters
    ----------
    file : str
        Path to a txt file of words for selection

    Returns
    -------
    str
        word to play hangman with.
    '''
    with open(file,"r") as f:
        lines = f.readlines()
    word_idx = random.randint(0,len(lines)-1)
    word = lines[word_idx].strip()
    return word
    

def hangman(word:str):
    wrong_guesses = 0
    stages = ["", 
              "  ________      ",
              "  |      |      ",
              "  |      0      ",
              "  |     /|\     ",
              "  |     / \     ",
              "  |             ",
              "__|__            "]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman\n')
    print((' '.join(letter_board)))
    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_idx = [idx for idx, char in enumerate(remaining_letters) if char == guess]
            for idx in character_idx:
                letter_board[idx] = guess
                remaining_letters[idx] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses + 1]))
        print('You lose! The words was {}'.format(word))
        
if __name__ == "__main__":
    file = "hangman_words.txt"
    
    word = randword(file)
    hangman(word)