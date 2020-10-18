import math as m
import numpy as np
from matplotlib import pyplot as plt


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


def raytrace(v0, v1, v2):
    res_x = 100
    res_y = 100
    fov = m.pi / 2

    hor = m.tan(fov / 2) * 2
    ver = m.tan(fov / 2) * 2

    O = np.array([0, 0, 0])

    screen = []

    for i in range(res_y):
        row = []
        for j in range(res_x):
            D = np.array([
                (j / res_x) * hor - hor / 2,
                (i / res_y) * ver - ver / 2,
                1])

            inter = intersect_triangle(v0, v1, v2, O, D)[0]
            u = inter[1]
            v = inter[2]

            if ((u>=0 and u<=1) and (v>=0 and v<=1) and ((u+v)>=0 and (u+v)<=1)):
                w = 1 - (u + u)

                row.append(([
                    1 * (1 - (u + v)),
                    1 * (1 - (w + u)),
                    1 * (1 - (w + v))
                ]))
            else:
                row.append((0, 0, 0))

        screen.append(row)

    return screen

v0 = np.array([-0.5, -0.5, 1.5])
v1 = np.array([0, 0.5, 1])
v2 = np.array([0.5, -0.5, 1])

screen = raytrace(v0, v1, v2)

fg = plt.figure()
ax = fg.gca()

plot = ax.imshow(screen, origin='lower')
plt.draw()
plt.pause(1000)
