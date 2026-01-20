def find_letter_in_word(word, user_input):
    """Take a word and user input to return a list of the letter placements"""

    try:
        letter_finds={} # Init dictionnary
        for i in range(len(word)):
            if user_input == word[i]: # If the letter is the same as the word letter
                letter_finds[i] = user_input # add to dictionnary
        return letter_finds

    except:
        print("Erreur")
        return

#print(find_letter_in_word("meme", "e"))