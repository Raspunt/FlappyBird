import pygame as pg
import sourceGame as sg
import random

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self,x):
        self.x = x
        self.height = 0

        self.top = 0
        self.botton = 0
        self.PipeTop = pg.transform.flip(sg.PipeImg,False,True)
        self.PipeBotton = sg.PipeImg

        self.passed = False
        self.setHeight()


    def setHeight(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PipeTop.get_height()
        self.botton = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self,win):
        win.blit(self.PipeTop, (self.x,self.top))
        win.blit(self.PipeBotton,(self.x,self.botton))

    def collide(self,bird):
        birdMask = bird.getMask()
        topMask = pg.mask.from_surface(self.PipeTop)
        bottonMask = pg.mask.from_surface(self.PipeBotton)

        topOffset = (self.x -bird.x,self.top - round(bird.y))
        bottonOffset = (self.x -bird.x, self.botton - round(bird.y))

        bPoint = birdMask.overlap(bottonMask,bottonOffset)
        tPoint = birdMask.overlap(topMask,bottonOffset)

        if tPoint or bPoint:
            return True

        return False
