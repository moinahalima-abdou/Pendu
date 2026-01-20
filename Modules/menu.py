def menu():
    try:
        pv=7 # init pv
        letter_finds = {}
        word = random_word_generator() # Select a random word

        while true:
            display_word(letter_finds) # Show the word length
            user_input = ask_user() # Ask user to input a word or a letter

            if 1 < user_input < len(user_input): # If input is in a word size
                if word == user_input : # check win 
                    print("You win")
                    return
                else:
                    pv-=1
                    print(pv)

            elif user_input == 1: # If input is a letter 
                if verify_letter(user_input, word): # Check if it's in word
                    letter_finds += find_letter_in_word() # Add letter placement
                elif not verify_letter(user_input,word): # if the letter is not in the word
                    pv-=1
                    print(pv)
                
            else: 
                print("Error - input length")

            if pv == 0 :
                print("You Loose")
                return

    except:
        print("Error")