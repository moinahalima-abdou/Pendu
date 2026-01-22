import pygame

def ask_user(word, window, font, display_text):
    """This function captures what the player types on the keyboard"""
    pygame.key.set_repeat(400, 50) # Enable key repeat
    pygame.event.clear() # Clear existing events
    user_input=""
    WHITE = (240, 240, 240)
    BLACK = (20, 20, 20)

    while True:
        # Clear the screen
        window.fill(WHITE)

        # Display the hidden word in the center
        text_surface = font.render(display_text, True, BLACK)
        text_rect = text_surface.get_rect(center=(window.get_width()//2, window.get_height()//2))
        window.blit(text_surface, text_rect)

        # Show the user input at the top left
        if user_input:
            input_surface = font.render(user_input, True, BLACK)
            input_rect = input_surface.get_rect(topleft=(20, 20))
            window.blit(input_surface, input_rect)
        
        pygame.display.flip()

        for event in pygame.event.get():
            # Check if a keyboard key is pressed
            if event.type == pygame.KEYDOWN:

                # If the pressed key is Enter
                if event.key == pygame.K_RETURN:
                    if len(user_input) > 0: # Only confirm if not empty
                        pygame.key.set_repeat(0) # Disable key repeat
                        return user_input   # Return the word or letter typed
                
                # If the pressed key is Backspace
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1] # Delete the last letter
                
                # Add the typed character to the text if it is a letter and not longer than the word
                elif len(user_input) < len(word) and event.unicode.isalpha():
                    user_input += event.unicode.lower()

                else :
                    print("Word is max size or not a letter")
            
            # Quit management
            elif event.type == pygame.QUIT:
                pygame.key.set_repeat(0) # Disable key repeat
                return None