#Quicksand font by Andrew Pagliwanan
#Background image provided by Unlucky Software
#Original music by Dylan Bailey


import pygame, sys, time
import py

#Code for Music
pygame.init()
pygame.mixer.init()
FPS = 30
fpsClock = pygame.time.Clock()
song = 'music.ogg'
pygame.mixer.music.load(song)
pygame.mixer.music.play(loops=-1, start=0.0)

# Initialize display
screen = pygame.display.set_mode([640,480])

#Defines custom font

myfont = pygame.font.SysFont("Quicksand-Bold.otf", 25)

# Reference colors

black = [0, 0, 0]
red = [255, 0, 0]

#Create characteristics of bricks

class Brick(pygame.sprite.Sprite):
    image = None

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        if Brick.image is None:
                Brick.image = pygame.image.load("brick.png")
        self.image = Brick.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.topleft = (self.x, self.y)

#Settings for text display
def msg(txt,color,size,x,y):
    font=pygame.font.SysFont("bold",size)
    msgtxt=font.render(txt,True,color)
    msgrect=msgtxt.get_rect()
    msgrect.center=x,y
    screen.blit(msgtxt,msgrect)

# Create ball movement settings (Need to rewrite to put in classes)

ball_x = 100
ball_y = 200
ball_radius = 8
ball_color = [222,50,50]
ball_speed_x = 4
ball_speed_y = 6

# Movement settings for the paddle (Need to rewrite to put in classes)

paddle_x = 20
paddle_y = 450
paddle_width = 60
paddle_height = 20
paddle_color = [64,100,41]
paddle_speed = 10

#Score to be tracked

score = 0

brick_array = []
for i in range(1,8):
    brick1 = Brick(75*i,50)
    brick_array.append(brick1)


pygame.key.set_repeat(20, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            coordinates = pygame.mouse.get_pos()
            paddle_x = coordinates[0] - paddle_width/2
            if paddle_x < 0:
                paddle_x = 0
            if paddle_x > screen.get_width() - paddle_width:
                paddle_x = screen.get_width() - paddle_width



    pygame.time.delay(10)
    screen.fill(black)
    msg("Jailbreak",red,40,200,100)
    icon=pygame.image.load("background.jpg")
    icon=pygame.transform.scale(icon,[640,480])
    screen.blit(icon,[1, 1])
    wait=1

    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x
    if ball_y > screen.get_height() - ball_radius:
        ball_speed_y = -ball_speed_y

    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
    if ball_x < ball_radius:
        ball_speed_x = -ball_speed_x

    if ball_x > screen.get_width() - ball_radius:
        ball_speed_x = -ball_speed_x


    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2) #circles are measured from the center, so have to subtract 1 radius from the x and y
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    if ball_rect.colliderect(paddle_rect):
        ball_speed_y = -ball_speed_y

    for brick in brick_array:
        if brick.rect.colliderect(ball_rect):
            score = score + 1
            brick_array.remove(brick)
            ball_speed_y = - ball_speed_y


    score_label = myfont.render(str(score), 1, pygame.color.THECOLORS['white'])
    screen.blit(score_label, (5, 10))
    for brick in brick_array:
        screen.blit(brick.image, brick.rect)
    pygame.draw.circle(screen, ball_color, [int(ball_x), int(ball_y)], ball_radius, 0)
    pygame.draw.rect(screen, paddle_color, [paddle_x, paddle_y, paddle_width, paddle_height], 0)
    pygame.display.update()


pygame.mixer.stop()
pygame.quit()
