import pygame as pg
import sourceGame as sg
import random



class Base:
    Vel = 3
    Width = sg.BaseImg.get_width()
    Img = sg.BaseImg


    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.Width

    def move(self):
        self.x1 -= self.Vel
        self.x2 -= self.Vel

        if self.x1 + self.Width < 0:
            self.x1 = self.x2 + self.Width


        if self.x2 + self.Width < 0:
            self.x2 = self.x1 + self.Width

    def draw(self,win):
        win.blit(self.Img,(self.x1,self.y))
        win.blit(self.Img,(self.x2,self.y))
