import pygame
import os
import time
import random

#lodaing images
RED_SPACE_SHIP = pygame.image.load(os.path.join("asset","pixel_ship_red_small.png"))
BLUE_SPACE_SHIP =pygame.image.load(os.path.join("asset","pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP =pygame.image.load(os.path.join("asset","pixel_ship_green_small.png"))
#player ship
YELLOW_SPACE_SHIP =pygame.image,load(os.path.join("asset","pixel_ship_yellow.png"))

#laser/bullets
RED_LASER =pygame.image.load(os.path.join("asset","pixel_laser_red.png"))
BLUE_LASER =pygame.image.load(os.path.join("asset","pixel_laser_blue.png"))
GREEN_LASER =pygame.image.load(os.path.join("asset","pixel_laser_green.png"))
YELLOW_LASER =pygame.image.load(os.path.join("asset","pixel_laser_yellow.png"))

#Background
BG = pygame.image.load(os.path.join("asset","background-black.png"))