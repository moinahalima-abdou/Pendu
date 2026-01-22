import pygame
from display_word import display_word
from random_word_generator import random_word_generator
from verify_letter import verify_letter
from ask_user import ask_user
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
        pv=7
        word = random_word_generator() # Generate a random word
        print(word) # log for debug
        letter_finds = [] 
        
        playing = True

        while playing:

            window.fill(WHITE) # Background color

            # Display the word 
            display_text = display_word(letter_finds, word)
            text_surface = font.render(display_text, True, BLACK)
            text_rect = text_surface.get_rect(center=(window.get_width()//2, window.get_height()//2))
            window.blit(text_surface, text_rect)

            pygame.display.flip()

            user_input = ask_user(word, window, font, display_text)
            if user_input is None: # if the user quit to prevent crashing
                return score

            if len(user_input) == len(word):
                if word == user_input: 
                    score += 1
                    print("You win")

                    window.fill(WHITE) # Background color

                    text_surface = font.render("You win", True, BLACK)
                    text_rect = text_surface.get_rect(center=(window.get_width()//2, window.get_height()//2))
                    window.blit(text_surface, text_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    playing = False

                    return score
                else:
                    pv-=1
            elif len(user_input) == 1:
                if verify_letter(user_input, word):
                    letter_finds += user_input
                elif not verify_letter(user_input,word): # if the letter is not in the word
                    pv-=1
            else:
                print("Error - input length")


            if pv == 0:
                print(pv)
                window.fill(WHITE) # Background color

                text_surface = font.render("You loose", True, BLACK)
                text_rect = text_surface.get_rect(center=(window.get_width()//2, window.get_height()//2))
                window.blit(text_surface, text_rect)
                pygame.display.flip()
                time.sleep(3)
                return score

            print(pv)

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
                                print("Starting the game...") # call your game loop here 
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