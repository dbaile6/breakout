#Quicksand font by Andrew Paglinawan

import pygame,random,time
pygame.init()

#Game display options

gwidth = 640
gheight = 480
clock=pygame.time.Clock()
screen=pygame.display.set_mode([gwidth,gheight])
pygame.display.set_caption('Jail Break')


#put the colors for tiles here

#sets width and height

def txtaes(color, size, text, x, y):
    pygame.font.Font('bold', "quicksand.ttf")
    txtfont=font.render(txt,True,color)
    txtrect=txttxt.get_rect()
    txtrect.center=x,y
    screen.blit(txttxt,txtrect)

#Game logic

#Draw background
