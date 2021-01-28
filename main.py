import pygame as pg
import time
import sourceGame as sg
from Bird import Bird


size = (500,800)
screen = pg.display.set_mode(size)

pg.display.set_caption("You welcome")


def drawWindow(win,bird):
    win.blit(sg.BgImg,(0,0))
    bird.draw(win)
    pg.display.update()



running = True
bird = Bird(250,400)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    bird.move()
    drawWindow(screen,bird)
