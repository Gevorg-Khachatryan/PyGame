import pygame
import random
from pygame.locals import  *

class Control:
    def __init__(self):
        self.flag_direction="RIGHT"
        self.flag_pouse=True

    def control(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_RIGHT and self.flag_direction!="LEFT":
                    self.flag_direction="RIGHT"
                elif event.key==K_LEFT and self.flag_direction!="RIGHT":
                    self.flag_direction="LEFT"
                elif event.key == K_UP and  self.flag_direction !="DOWN":
                    self.flag_direction ="UP"
                elif event.key == K_DOWN and self.flag_direction !="UP":
                    self.flag_direction ="DOWN"
                elif event.key == K_ESCAPE:
                    exit()
                elif event.key==K_SPACE:
                    if self.flag_pouse==True:
                        self.flag_pouse=False
                    else:
                        self.flag_pouse=True

class Snake():
    def __init__(self):
        self.head=[44,44]
        self.body=[[44,44],[33,44],[22,44]]
        self.apple=[11*random.randint(1,39),11*random.randint(1,39)]

    def move(self,Control):
        if self.head[0]>440:
            self.head[0]=0
        if self.head[1]>440:
            self.head[1]=0
        if self.head[0]<0:
            self.head[0]=440
        if self.head[1]<0:
            self.head[1]=440
        if Control.flag_direction=="RIGHT":
            self.head[0]+=11
        if Control.flag_direction=="LEFT":
            self.head[0]-=11
        if Control.flag_direction=="DOWN":
            self.head[1]+=11
        if Control.flag_direction=="UP":
            self.head[1]-=11

    def animation(self):
        self.body.insert(0, list(self.head))
        if self.head!=self.apple:
            self.body.pop()
        else:
            self.apple = [11 * random.randint(1, 39), 11 * random.randint(1, 39)]
    def draw_snake(self,window):
        pygame.draw.rect(window, pygame.Color("red"), pygame.Rect(self.apple[0], self.apple[1], 10, 10))
        for s in self.body:
            pygame.draw.rect(window,pygame.Color("green"),pygame.Rect(s[0],s[1],10,10))