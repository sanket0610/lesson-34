import pygame

pygame.init
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Add sprite")
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,"red",pygame.Rect(180,120,200,250))
    pygame.display.flip()