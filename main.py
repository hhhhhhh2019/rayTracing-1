import math as m
import numpy as np
from camera import Camera
from object import *
import pygame as pg
from settings import *


screen = pg.display.set_mode(RES)
clock = pg.time.Clock()

scene = [
    Object(np.array([
        [-0.5, -0.5, 1.5],
        [0, 0.5, 1],
        [0.5, -0.5, 1]
    ]),
    np.array([[0, 1, 2]]))
    # load_obj('object1.obj')
]

camera = Camera(np.array([0, 0, 0]), [100, 100], m.pi / 2)

while True:
    screen.fill((0, 0, 0))

    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()

    camera.render(screen, scene)

    pg.display.flip()
    pg.display.set_caption(str(clock.get_fps()))
