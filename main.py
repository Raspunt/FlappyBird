import pygame as pg
import time


size = (600,600)
screen = pg.display.set_mode(size)

pg.display.set_caption("You welcome")

i = 0

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
