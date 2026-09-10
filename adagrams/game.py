from random import randint
#import random

def draw_letters():
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }
    hand = []                                    #hand of 10 letters

    for i in range(10):                          #given the range of 10 letters
        index = randint(0, len(LETTER_POOL) - 1) #(0, 26 -1) -- (0, 25)
        letter = list(LETTER_POOL.keys())[index] #take keys from LETTER_POOL and convert them into list
                                                 # whatever index got picked from 0-25, that letter gets picked from the LETTER_POOL
        hand.append(letter)                      #add the letter to the hand list
        LETTER_POOL[letter] -= 1                 #decrease the letter by 1 from LETTER_POOL
        if LETTER_POOL[letter] == 0:             #if Letter count is already 0
            del LETTER_POOL[letter]              #delete the letter from pool

    return hand
    


def uses_available_letters(word, letter_bank):
    word = word.upper()                          # word we want to check
    letter_bank = letter_bank.copy()
    for letter in word:
        if letter not in letter_bank:
            return False
        letter_bank.remove(letter)

    return True    

    

#we need to check whether we can make the word with the letters in our hand


def score_word(word):
    score_chart = {
        'A': 1, 
        'B': 3, 
        'C': 3, 
        'D': 2, 
        'E': 1, 
        'F': 4, 
        'G': 2, 
        'H': 4, 
        'I': 1, 
        'J': 8, 
        'K': 5, 
        'L': 1, 
        'M': 3, 
        'N': 1, 
        'O': 1, 
        'P': 3, 
        'Q': 10, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'U': 1, 
        'V': 4, 
        'W': 4, 
        'X': 8, 
        'Y': 4, 
        'Z': 10
    }
    score = 0
    
    for letter in word:
        score += score_chart[letter]
    if len(word) >= 7:
        score += 8
        
    return score



def get_highest_word_score(word_list):
    pass