import pygame
from Modules.display_word import display_word
from Modules.random_word_generator import random_word_generator
from Modules.verify_letter import verify_letter
from Modules.draw_stickman import draw_stickman

import time

pygame.init()
window = pygame.display.set_mode((680, 440))
pygame.display.set_caption("Hangman Game")

WHITE = (240,240,240)
BLACK = (20,20,20)
BLUE = (20,20,255)

font = pygame.font.SysFont(None, 36)

buttons = [ 
    {"rect": pygame.Rect(240, 120, 200, 60), "text": "Play", "action":"start_game"}, 
    {"rect": pygame.Rect(240, 200, 200, 60), "text": "Quit", "action":"quit_game"}, 
]

def start_game(score):
    try:
        pv = 7
        word = random_word_generator() # Generate a random word
        print(word) # log for debug
        letter_finds = [] 
        tried_letters = []
        user_input = ""
        
        # Key repeat configuration (enable rapid backspace deletion)
        pygame.key.set_repeat(400, 50)

        playing = True

        while playing:
            # 1. DRAWING
            window.fill(WHITE) # Clear screen

            # Draw Stickman (always visible)
            draw_stickman(window, pv)

            # Display the hidden/revealed word
            display_text = display_word(letter_finds, word)
            text_surface = font.render(display_text, True, BLACK)
            text_rect = text_surface.get_rect(center=(window.get_width()//2, 380))
            window.blit(text_surface, text_rect)

            # Display User Input (top left)
            if user_input:
                input_surface = font.render(user_input, True, BLACK)
                input_rect = input_surface.get_rect(topleft=(20, 20))
                window.blit(input_surface, input_rect)

            # Display Tried Letters (top right)
            if tried_letters:
                tried_text = " ".join(tried_letters)
                tried_surface = font.render(tried_text, True, BLACK)
                tried_rect = tried_surface.get_rect(topright=(window.get_width() - 20, 20))
                window.blit(tried_surface, tried_rect)

            pygame.display.flip()

            # 2. EVENT HANDLING
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.key.set_repeat(0)
                    return score
                
                elif event.type == pygame.KEYDOWN:
                    # Validate Input (Enter)
                    if event.key == pygame.K_RETURN:
                        if len(user_input) > 0:
                            # Verify Word
                            if len(user_input) == len(word):
                                if word == user_input: 
                                    score += 1
                                    print("You win")

                                    window.fill(WHITE)
                                    text_surface = font.render("You win", True, BLACK)
                                    text_rect = text_surface.get_rect(center=(window.get_width()//2, window.get_height()//2))
                                    window.blit(text_surface, text_rect)
                                    pygame.display.flip()
                                    time.sleep(3)
                                    
                                    pygame.key.set_repeat(0)
                                    return score
                                else:
                                    pv -= 1
                            # Verify Letter
                            elif len(user_input) == 1:
                                if user_input not in tried_letters:
                                    tried_letters.append(user_input)

                                if verify_letter(user_input, word):
                                    letter_finds.append(user_input)
                                    
                                    # Check if all letters are found
                                    if all(char in letter_finds for char in word):
                                        score += 1
                                        print("You win")

                                        window.fill(WHITE)
                                        text_surface = font.render("You win", True, BLACK)
                                        text_rect = text_surface.get_rect(center=(window.get_width()//2, 380))
                                        window.blit(text_surface, text_rect)
                                        pygame.display.flip()
                                        time.sleep(3)
                                        
                                        pygame.key.set_repeat(0)
                                        return score

                                elif not verify_letter(user_input, word):
                                    pv -= 1
                            else:
                                print("Error - input length")
                            
                            # Reset input after validation
                            user_input = ""

                    # Backspace
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]

                    # Typing Letters
                    elif event.unicode.isalpha() and len(user_input) < len(word):
                        user_input += event.unicode.lower()
            
            # 3. CHECK END GAME (LOSS)
            if pv == 0:
                print(pv)
                # Ensure the last stickman part is drawn
                window.fill(WHITE)
                draw_stickman(window, pv) # Draw full stickman
                
                text_surface = font.render("You loose", True, BLACK)
                text_rect = text_surface.get_rect(center=(window.get_width()//2, 380))
                window.blit(text_surface, text_rect)
                pygame.display.flip()
                time.sleep(3)
                
                pygame.key.set_repeat(0)
                return score

    except Exception as e :
        print("Error - start_game -", e)


def menu():
    try:
        score = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    for btn in buttons: 
                        if btn["rect"].collidepoint(event.pos):
                            if btn["action"] == "start_game": 
                                print("Starting the game...")
                                score = start_game(score)
                            elif btn["action"] == "quit_game": 
                                print("Quitting...") 
                                running = False

            window.fill((240, 240, 240))

            # Display Score
            score_surface = font.render(f"Score: {score}", True, BLACK)
            score_rect = score_surface.get_rect(topleft=(10, 10))
            window.blit(score_surface, score_rect)

            # Draw button 
            for btn in buttons: 
                pygame.draw.rect(window, BLUE, btn["rect"]) 
                text_surface = font.render(btn["text"], True, WHITE) 
                # Center text inside the button 
                text_rect = text_surface.get_rect(center=btn["rect"].center) 
                window.blit(text_surface, text_rect)

            pygame.display.flip()

        pygame.quit()
    except Exception as e :
        print("Error - menu -", e)
menu()