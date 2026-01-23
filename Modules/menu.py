import pygame
from Modules.display_word import display_word
from Modules.random_word_generator import random_word_generator
from Modules.verify_letter import verify_letter
from Modules.draw_stickman import draw_stickman
from Modules.start_game import start_game

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


def menu():
"""Show the menu of the game with start and quit"""
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

                                score = start_game(score, window, font,)

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