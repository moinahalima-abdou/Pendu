def verify_letter(user_input, word):
"""verify if a letter is in a word and return a boolean"""
    for char in word:
        if char == user_input:
            return True
    return False