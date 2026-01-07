import pygame

pygame.init
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Add sprite")
done=False
screen.fill("green")
pygame.draw.circle(screen,"red",(200,200), 20)
pygame.draw.circle(screen,"blue",(200,100),20,4)
pygame.draw.polygon(screen,"blue",[(300,300),(400,300),(300,400),(400,300),(200,200),(300,200)])
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()