import pygame
pygame.init()
screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("First game ever")
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
pygame.quit()