import sys, pygame
import random



pygame.init()
random.seed()

r = random.randint(2, 6)


size = width, height = 640, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("pygametest/ball.gif")
ballrect = ball.get_rect()
rct = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed = [2, 1]
            if event.key == pygame.K_UP:
                speed = [2, 2]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

    pygame.time.wait(1)