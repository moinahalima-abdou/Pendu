def display_word(letter_finds, word):
    display = ""
    for char in word:
        if char in letter_finds:
            display += char + " "
        else:
            display += "_ "
    return display
