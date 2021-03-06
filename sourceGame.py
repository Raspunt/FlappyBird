import pygame as pg
import time
import os


BirdImgs = [pg.transform.scale2x(pg.image.load(os.path.join("imgs","bird1.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs","bird2.png"))),
            pg.transform.scale2x(pg.image.load(os.path.join("imgs","bird3.png")))]

PipeImg = pg.transform.scale2x(pg.image.load(os.path.join("imgs","pipe.png")))
BaseImg = pg.transform.scale2x(pg.image.load(os.path.join("imgs","base.png")))
BgImg = pg.transform.scale2x(pg.image.load(os.path.join("imgs","bg.png")))


pg.font.init()
StatFont = pg.font.SysFont("comicsans",50)
