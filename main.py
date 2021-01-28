import pygame as pg
import time
import sourceGame as sg
from Bird import Bird


size = (600,600)
screen = pg.display.set_mode(size)

pg.display.set_caption("You welcome")


def drawWindow(win,bird):
    win.blit(sg.BgImg,(0,0))
    bird.draw(win)
    pg.display.update()




running = True
bird = Bird(400,400)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    drawWindow(screen,bird)
