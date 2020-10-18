import math as m
import numpy as np
import pygame as pg
from settings import *


def intersect_triangle(v0, v1, v2, o, d):
    e1 = v1 - v0
    e2 = v2 - v0
    t = o - v0
    p = np.cross(d, e2)
    q = np.cross(t, e1)

    return 1 / (np.dot(p, e1)) * np.transpose([
        [np.dot(q, e2)],
        [np.dot(p, t)],
        [np.dot(q, d)]
    ])


class Camera:
    def __init__(self, pos, res,fov):
        self.pos = pos
        self.res = res
        self.fov = fov

        self.surface = pg.Surface(res)

    def render(self, screen, scene):
        hor = m.tan(self.fov / 2) * 2
        ver = m.tan(self.fov / 2) * 2

        for i in range(self.res[1]):
            for j in range(self.res[0]):
                d = np.array([
                    (j / self.res[0]) * hor - hor / 2,
                    (i / self.res[1]) * ver - ver / 2,
                    1])

                for obj in scene:
                    for face in obj.faces:
                        # print([obj.vert[f] for f in face])
                        v0, v1, v2 = [obj.vert[f] for f in face]

                        inter = intersect_triangle(v0, v1, v2, self.pos, d)[0]
                        u = inter[1]
                        v = inter[2]

                        if (0 <= u <= 1) and (0 <= v <= 1) and (0 <= (u+v) <= 1):
                            pg.draw.rect(self.surface, (255, 255, 255), (j, i, 1, 1))

        screen.blit(pg.transform.scale(self.surface, RES), (0, 0))
