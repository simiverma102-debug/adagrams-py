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
    word = word.upper()
    letter_bank = letter_bank.copy()            #created a copy so letters doesn't change the letter_bank list
    for letter in word:                         #iterating over letters in the word
        if letter not in letter_bank:           #if letter is not in the letter_bank
            return False                        #return false
        letter_bank.remove(letter)              #else remove the letter from letter_bank
    return True                                 #return true if all the letters are there in letter_bank to make that word


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
    score = 0                            #created empty score variable to store score
    word = word.upper()                  #covert the word into upper case if it is not already
    for letter in word:                  #iterating over letters in the word
        score += score_chart[letter]     #score of the letter is added to the variable score
    if len(word) >= 7:                   #if the len of word is 7 or more 
        score += 8                       #additional 8 points to the score                 
                                         #if condition is outside for loop because its a separate condition
    return score                         #return final score



def get_highest_word_score(word_list):
    #check the score of word and return waysto find the highest score
    highest_score = 0
    best_word = ""
    for word in word_list:                      #iterating words over the word_list
        score = score_word(word)                #gets the score using score_word function
        if score > highest_score:               #if score is greater than highest_score
            highest_score = score               #highest_score will be updated to new score
            best_word = word                    #best_word will also gets updated to new word
        elif score == highest_score:            #if score is equal to highest_score
            if len(word) == 10 and len(best_word)!=10:
                best_word = word
            elif len(best_word)!= 10 and len(word) < len(best_word): #word with fewer letters is preferred unless its 10 letters long
                best_word = word                #word will become best_word        
            
    return best_word, highest_score             #return tuple (best_word, highest_score)