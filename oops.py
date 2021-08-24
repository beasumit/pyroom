import pygame   
pygame.init()
HEIGHT,WIDTH=800,600
display = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.update()

open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
pygame.quit()
quit() 
