import pygame as pg
import time
import sourceGame as sg
from Bird import Bird
from Base import Base
from Pipe import Pipe


size = (500,800)
screen = pg.display.set_mode(size)

pg.display.set_caption("You welcome")


def drawWindow(win,bird,pipes,base):
    win.blit(sg.BgImg,(0,0))

    for pipe in pipes:
        pipe.draw(win)

    bird.draw(win)
    base.draw(win)
    pg.display.update()



running = True
bird = Bird(250,400)
base = Base(730)
pipes = [Pipe(700)]
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # bird.move()
    #
    for pipe in pipes :
        pipe.move()

    base.move()
    drawWindow(screen,bird,pipes,base)
