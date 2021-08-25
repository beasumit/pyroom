import pygame
import os
import time
import random

#setting the windows for the game.
WIDTH,HEIGHT=800,600 # we can directly use the height and width in the below bracket without making any varibale for height and width. 
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("space blast")

 #lodaing images
RED_SPACE_SHIP =pygame.image.load(os.path.join("assets","pixel_ship_red_small.png"))
BLUE_SPACE_SHIP =pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP =pygame.image.load(os.path.join("assets","pixel_ship_green_small.png"))

#player ship
YELLOW_SPACE_SHIP =pygame.image.load(os.path.join("assets","pixel_ship_yellow.png"))

#laser/bullets
RED_LASER =pygame.image.load(os.path.join("assets","pixel_laser_red.png"))
BLUE_LASER =pygame.image.load(os.path.join("assets","pixel_laser_blue.png"))
GREEN_LASER =pygame.image.load(os.path.join("assets","pixel_laser_green.png"))
YELLOW_LASER =pygame.image.load(os.path.join("assets","pixel_laser_yellow.png"))

#Background
BG = pygame.image.load(os.path.join("assets","background-black.png"))

#core game mechanics.
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
main()



