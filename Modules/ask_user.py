import pygame

def ask_user(event , user_text=""):
    """This function gets what the player types on the keyboard"""

    #Check if a keyboard key is pressed
    if event.type == pygame.KEYDOWN:

        #If the pressed key is Enter
        if event.key == pygame.K_RETURN:
            return user_text   #Return the word or letter typed
        
        # If the pressed key is Backspace
        elif event.key == pygame.K_BACKSPACE:
            return user_text[:-1] # Delete the last letter
        
        #Else, add the typed character to the text
        else:
            return user_text + event.unicode

    
    return user_text