#!/usr/bin/env python
# coding: utf-8

# # Evil Hangman

# ## Motivating Thoughts

# 1. I do not want to cheat
# 2. I only want to choose something about my word when I absolutely must!
# 3. The computer should choose whatever maximizes the total number of possible words

# In[ ]:


def words_of_length_N(N):
    """Function that returns all words of length N.
    
    Inputs: 
            N - Integer
            
    Ouputs:
            words - list of words of length N
    """
    
    words = []
    file = open("/srv/data/ScrabbleWords.txt")
    
    for line in file:
        line = line.strip()
        word_length = len(line)
        if word_length == N:
            words.append(line)
    
    file.close()
    return words


# ## Create the Hangman Pattern

# In[ ]:


def create_hangman_pattern(word, guess):
    """Function to create a generic hangman pattern 
    given a word and a list of guessed letters.
    
    Inputs: 
            word - string
            guess - list of letters
            
    Ouputs:
            pattern - string, hangman pattern
    """
    
    pattern = ""
    
    for letter in word:
        if letter in guess:
            pattern = pattern + letter + " "
        else:
            pattern = pattern + "_ "
    
    return pattern


# In[ ]:


def get_hangman_pattern_for_dictionary(wordlist, guess):
    """Function to create the hangman pattern dictionary.
    
    Inputs: 
            wordlist - list of all viable words
            guess - list of letters
            
    Ouputs:
            patterns - dictionary of hangman patterns
    """
    patterns = {}
    
    for word in wordlist:
        pattern = create_hangman_pattern(word, guess)
        if pattern in patterns:
            patterns[pattern].append(word)
        else:
            patterns[pattern] = [word]
        
    return patterns


# In[ ]:


def find_largest_collection(pattern_dict):
    """Function to find the hangman pattern with the
    largest number of words attached to it.
    
    Inputs: 
            pattern_dict - Dictonary of hangman patterns
            
    Ouputs:
            pattern - string, hangman pattern with the largest 
                        number of words in it.
    """
    
    max_size = 0

    for key in pattern_dict:
        curr_size = len(pattern_dict[key])
        if curr_size > max_size:
            max_size = curr_size
            pattern = key
    
    return pattern


# ## Display functions

# In[ ]:


def display_guessed_letters(guessed_letters):
    lets = " ".join(guessed_letters)
    print(f"Previously guessed letters: {lets}")


# ## Make the actual game

# In[ ]:


def evil_hangman():
    """Function to play evil hangman!
    
    Inputs:
            None
    
    Outputs:
            None
    """
    N = 8  # Length of secret word
    wordlist = words_of_length_N(N)
    guessed_letters = []
    secret_pattern = "_ "*N
    turns_left = 7
    
    while turns_left > 0:
        
        print(f"The secret word is: {secret_pattern}")
        display_guessed_letters(guessed_letters)
        print(f"You have {turns_left} wrong guesses left.")
        
        guess = input("Please guess a letter (EXIT to quit): ").lower()
        
        if guess == "exit":
            print("\n\nQuiting now....")
            return
        
        if guess in guessed_letters:
            print("You have already guessed that letter.  Try again.\n")
        
        else:
            guessed_letters.append(guess)
            pd = get_hangman_pattern_for_dictionary(wordlist, guessed_letters)
            new_pattern = find_largest_collection(pd)
            wordlist = pd[new_pattern]
            
            print(f"\n\nDEBUG ONLY - DEBUG ONLY - DEBUG ONLY")
            print(f"Size of wordlist: {len(wordlist)}")
            if len(wordlist) < 100:
                print("words are: ",end="")
                for i in range(len(wordlist)):
                    print(wordlist[i], end=", ")
                    if i % 4 == 0:
                        print("")
                print("")
            print(f"DEBUG ONLY - DEBUG ONLY - DEBUG ONLY\n\n")
            
            if new_pattern == secret_pattern:
                turns_left = turns_left - 1
                print("\n**************************************")
                print(f"Incorrect.")
                print("**************************************\n")
            else:
                secret_pattern = new_pattern
            
            if secret_pattern.count("_") == 0:
                print("\n\n###############")
                print("You win!")
                print("###############\n\n")
                break
    
    print("You Lose.")

