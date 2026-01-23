import pygame

def draw_stickman(window, pv):
    """Display the stickman with pv in parameters"""
    BLACK = (20, 20, 20)
    width = window.get_width()
    height = window.get_height()
    
    start_x = width // 2 - 50
    start_y = height // 2 - 80

    # Draw the gallows (structure) at the first mistake (pv decreases from 7 to 6)
    if pv <= 6:
        # Base
        pygame.draw.line(window, BLACK, (start_x - 50, start_y + 150), (start_x + 50, start_y + 150), 5)
        # Vertical Pole
        pygame.draw.line(window, BLACK, (start_x, start_y + 150), (start_x, start_y - 50), 5)
        # Top Bar
        pygame.draw.line(window, BLACK, (start_x, start_y - 50), (start_x + 100, start_y - 50), 5)
        # Rope
        pygame.draw.line(window, BLACK, (start_x + 100, start_y - 50), (start_x + 100, start_y), 5)
    
    if pv <= 5:
        # Head
        pygame.draw.circle(window, BLACK, (start_x + 100, start_y + 20), 20, 5)
    
    if pv <= 4:
        # Body
        pygame.draw.line(window, BLACK, (start_x + 100, start_y + 40), (start_x + 100, start_y + 100), 5)
    
    if pv <= 3:
        # Left Arm
        pygame.draw.line(window, BLACK, (start_x + 100, start_y + 50), (start_x + 70, start_y + 80), 5)

    if pv <= 2:
        # Right Arm
        pygame.draw.line(window, BLACK, (start_x + 100, start_y + 50), (start_x + 130, start_y + 80), 5)
    
    if pv <= 1:
        # Left Leg
        pygame.draw.line(window, BLACK, (start_x + 100, start_y + 100), (start_x + 70, start_y + 140), 5)

    if pv <= 0:
        # Right Leg
        pygame.draw.line(window, BLACK, (start_x + 100, start_y + 100), (start_x + 130, start_y + 140), 5)
