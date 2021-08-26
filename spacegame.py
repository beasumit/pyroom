import pygame
import os
import time
import random
pygame.font.init()

#setting the windows for the game.
WIDTH,HEIGHT=750,750 
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
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets","background-black.png")),(WIDTH,HEIGHT))

#character
class Ship:
    def __init__(self,x,y,health=100):
        self.x=x
        self.y=y
        self.health=health
        self.ship_image=None
        self.lazer_img=None
        self.laser=[]
        self.cool_down_counter=0

    def draw(self,window):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y,50,50))
        



#core game mechanics.
def main():
    run = True
    FPS = 60
    level=1
    lives=5
    clock = pygame.time.Clock()
    main_font=pygame.font.SysFont("comicssans",50)
    ship=Ship(300,650)
    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_label=main_font.render(f"Lives:{lives}",1,(255,255,255))
        level_label=main_font.render(f"Level:{level}",1,(255,255,255))
        WIN.blit(lives_label,(10,10))
        WIN.blit(level_label,(WIDTH-level_label.get_width()-10,10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
main()



