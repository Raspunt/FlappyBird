import pygame as pg
import sourceGame as sg
import random




class Pipe:
    GAP = 200
    VEL = 1


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



    add_pipe = False
    rem = []
    def OverrideVar(self):
        self.add_pipe = False
        self.rem = []


    def CollideBird(self,pipe,bird):
        if pipe.collide(bird):
            pass
        if pipe.x + pipe.PipeTop.get_width() < 0:
            self.rem.append(pipe)

        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            self.add_pipe = True
        pipe.move()


    def ReCreatePipe(self,pipes,win,score):
        if self.add_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in self.rem:
            pipes.remove(r)
        return score
