import math as m
import numpy as np
from settings import *
from matrix import rotate_x, rotate_y


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

        self.angle = [0, 0, 0]

    def render(self, scene, ld):
        hor = m.tan(self.fov / 2) * 2
        ver = m.tan(self.fov / 2) * 2

        res_x, res_y = self.res

        screen = []

        for i in range(res_y):
            row = []
            for j in range(res_x):
                d = ((np.array([
                    (j / res_x) * hor - hor / 2,
                    (i / res_y) * ver - ver / 2,
                    1, 1]) @ rotate_x(self.angle[0])) @ rotate_y(self.angle[1]))[:3]

                a = False

                for obj in scene:
                    for face in obj.faces:
                        v1, v2, v3 = [obj.vert[f] for f in face]

                        inter = intersect_triangle(v1, v2, v3, self.pos, d)[0]
                        u = inter[1]
                        v = inter[2]

                        if ((u>=0 and u<=1) and (v>=0 and v<=1) and ((u+v)>=0 and (u+v)<=1)):
                            c = int(min(max(255 * get_light(ld, get_normal(v1, v2, v3)), 0), 255))

                            row.append((c, c, c))

                            a = True

                            break

                if not a:
                    row.append((0, 0, 0))


            screen.append(row)

        return screen

    def rotate_x(self, a):
        self.angle[0] += a

    def rotate_y(self, a):
        self.angle[1] += a


def get_normal(v1, v2, v3):
    ab = v1 - v2
    bc = v2 - v3

    return [ab[1] * bc[2] - ab[2] * bc[1], ab[2] * bc[0] - ab[0] * bc[2], ab[0] * bc[1] - ab[1] * bc[0]]

def get_light(l, n):
    return max(np.dot(l, n) * 0.5 + 0.5, 0)
