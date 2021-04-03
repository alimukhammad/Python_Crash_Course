import sys
import pygame

def run_game():
    pygame.init()
    bg_color = (230, 230, 230) # background color (light grey)

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color) # redraws the screen during each pass through the loop
        pygame.display.flip()

run_game()