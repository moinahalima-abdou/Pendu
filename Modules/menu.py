import pygame

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
                    elif btn["action"] == "quit_game": 
                        print("Quitting...") 
                        running = False

    window.fill((240, 240, 240))

    # Draw button 
    for btn in buttons: 
        pygame.draw.rect(window, BLUE, btn["rect"]) 
        text_surface = font.render(btn["text"], True, WHITE) 
        # Center text inside the button 
        text_rect = text_surface.get_rect(center=btn["rect"].center) 
        window.blit(text_surface, text_rect)

    pygame.display.flip()

pygame.quit()


def start_game():
    pv=7 # init pv
    word = random_word_generator()
    letter_finds = []

    playing = True:
    while playing:
        display_word(letter_finds)
