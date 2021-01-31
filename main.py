import pygame as pg
import time
import sourceGame as sg
from Bird import Bird
from Base import Base
from Pipe import Pipe


size = (500,800)
screen = pg.display.set_mode(size)

pg.display.set_caption("You welcome")





def drawWindow(win,bird,pipes,base,Store):
    win.blit(sg.BgImg,(0,0))

    for pipe in pipes:
        pipe.draw(win)

    bird.draw(win)
    base.draw(win)

    x, y = win.get_size()
    text = sg.StatFont.render("Score: " + str(Store),1,(255,255,255))
    win.blit(text,(x - 10 - text.get_width(),10))

    pg.display.update()


score = 0
running = True
bird = Bird(250,400)
base = Base(730)
pipes = [Pipe(700)]
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bird.jump()


    bird.move()
    for pipe in pipes :
        pipe.OverrideVar()
        pipe.CollideBird(pipe,bird)
        pipe.move()
    score = pipe.ReCreatePipe(pipes,screen,score)


    base.move()
    drawWindow(screen,bird,pipes,base,score)
