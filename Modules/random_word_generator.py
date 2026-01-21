import random


def random_word_generator():
    
    """Function that returns a random word from the file 'words.txt'."""

    #Open the file 'words.txt' in read mode
    with open("Modules/words.txt", "r") as f:  

        #Read all lines from the file and create a list of words
        word = f.read().splitlines()

    # Return a word randomly chosen from the list
    return random.choice(word)

random_word_generator()

