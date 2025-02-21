import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("My Game")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with a color (RGB)
    window.fill((0, 0, 0))  # Black

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()