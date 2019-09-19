import pygame
from control import Control,Snake
pygame.init()
window = pygame.display.set_mode([451,451])
pygame.display.set_caption("Snake")
control=Control()
snake=Snake()
speed=0
drop=500
level=3
while True:

    control.control()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           exit()
    window.fill(pygame.Color("black"))
    if len(snake.body)>level:
        level+=7
        drop-=100


    if speed%drop==0 and control.flag_pouse:
        snake.animation()
        snake.move(control)
    snake.draw_snake(window)
    speed+=1
    pygame.display.flip()