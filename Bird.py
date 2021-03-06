import pygame as pg
import neat
import time
import os
import random
import sourceGame as sg


class Bird:
    Imgs = sg.BirdImgs
    Max_Rotation = 25
    RotVel = 20
    AnimationTime = 5


    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tilt =  0
        self.tickCount = 0
        self.vel = 0
        self.height = self.y
        self.imgsCount = 0
        self.img =  self.Imgs[0]

    def jump(self):
        self.vel = -1
        self.tickCount = 0
        self.height = self.y

    def move(self):
        self.tickCount += 1
        d = self.vel * self.imgsCount + 0.5 * self.tickCount**2

        if d >=  5:
            d = 2

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.Max_Rotation:
                self.tilt = self.Max_Rotation
        else:
            if self.tilt > -90:
                self.tilt -= self.RotVel

    def draw(self,win):
        self.imgsCount += 1
        if self.imgsCount < self.AnimationTime:
            self.img = self.Imgs[0]
        elif self.imgsCount < self.AnimationTime*2:
            self.img = self.Imgs[1]
        elif self.imgsCount < self.AnimationTime*3:
            self.img = self.Imgs[2]
        elif self.imgsCount < self.AnimationTime*4:
            self.img = self.Imgs[0]
        elif self.imgsCount < self.AnimationTime*4 + 1:
            self.img = self.Imgs[1]
            self.imgsCount = 0

        if self.tilt <= -80 :
            self.img = self.Imgs[1]
            self.imgsCount =  self.AnimationTime * 2

        rotatedImage = pg.transform.rotate(self.img,self.tilt)
        newRect = rotatedImage.get_rect(center = self.img.get_rect(topleft = (self.x,self.y)).center)
        win.blit(rotatedImage,newRect.topleft)

    def getMask(self):
        return pg.mask.from_surface(self.img)
