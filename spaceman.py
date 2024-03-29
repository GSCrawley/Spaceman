import random
import os
import sys

def load_word():
    '''A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    Returns: string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''


def get_guessed_word(secret_word, letters_guessed):
    return_word = " "
    for letter in secret_word:
        if letter in letters_guessed:
            return_word +=letter + " "
        else:
            return_word += " _ "
    return return_word
    # print(return_word)

    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''


    pass


def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True 
    else:
        return False


    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    guesses_left = len(secret_word)
    
    
    while guesses_left > 0 and not is_word_guessed(secret_word, letters_guessed):
        letter_guess=input("Guess the secret word, one lowercase letter at a time. This word has "+str(len(secret_word))+" letters. You get "+str(guesses_left)+" chances before the spaceman repairs his ship and the game ends. Please choose a letter: ")
        if is_guess_in_word(letter_guess, secret_word):
            letters_guessed.append(letter_guess)
            print("Great! You guessed correctly! Please choose another letter or guess the word.")
            print(get_guessed_word(secret_word, letters_guessed))
        else:
            guesses_left = guesses_left -1
            print("Sorry. You've got "+str(guesses_left)+" guesses left.")
            print(get_guessed_word(secret_word, letters_guessed))
    else: 
        while len(letter_guess) > 1 or not letter_guess.isalpha():
            letter_guess=input("oops! Only one letter at a time please. Please try again. ")

    if is_word_guessed(secret_word, letters_guessed):
                print("Congrats dude you're a genius!")
    else:
        guesses_left = 0
        print("You've guessed wrong too often, so I hate to break it to you bruh but.. GAME OVER. By the way, the word you failed to guess was '"+secret_word+"'.")
        
           
    
           #Restarting the game
#Reference: https://stackoverflow.com/questions/48129942/python-restart-program
def restart():
        choice = input('Would you like to play again? y/n\n')
        if choice == 'y':
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        elif choice == 'n':
            print('Thanks for playing!')
            sys.exit(0)
        else:
            pass
        


        
  
#These function calls that will start the game
if __name__=="__main__":
    secret_word = load_word()
    spaceman(secret_word)
    restart()
    print("Thanks for playing, have a nice day!")
