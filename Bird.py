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
    Animation = 5


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
        self.vel = -10.5
        self.tiltCount = 0
        self.height = self.y

    def Move(self):
        self.tiltCount += 1

        d = self.vel * self.imgsCount + 1.5 * self.tickCount**2

        if d >=  16:
