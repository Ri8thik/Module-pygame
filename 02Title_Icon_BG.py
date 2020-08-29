import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))

## use to set the title of the pygame
title=pygame.display.set_caption("Games")

## use to set the icon on the pygame
icon = pygame.image.load("pack.jpg")
pygame.display.set_icon(icon)

## first we import the image in bg 
bg=pygame.image.load("images.jpg")

## here we change the size if image which is upload in bg 
bg=pygame.transform.scale(bg,(800,600))

## here while loop
running=True
while running:
## it is used to se the screen color 
    screen.fill((0,0,0))
## it is used to set the bg which we want
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    pygame.display.update()
