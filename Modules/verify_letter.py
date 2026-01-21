def verify_letter(user_input, word):
    for char in word:
        if char == user_input:
            return True
    return False