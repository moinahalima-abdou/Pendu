def display_word(letter_finds, word):
    """Function that hide the word and display finded words"""
    
    display = ""
    for char in word:
        if char in letter_finds:
            display += char + " "
        else:
            display += "_ "
    return display
