import math as m
from camera import Camera
from object import *
from matplotlib import pyplot as plt
from settings import *


obj = Object(np.array([
        [-1, -1, -1],
        [-1, 1, -1],
        [1, 1, -1],
        [1, -1, -1],
        [-1, -1, 1],
        [-1, 1, 1],
        [1, 1, 1],
        [1, -1, 1]
    ]),
    np.array([
        [2, 1, 0],
        [3, 2, 0],
        [2, 6, 3],
        [3, 6, 7],
        [5, 2, 1],
        [6, 2, 5]
    ]))

scene = [
    obj
]

camera = Camera(np.array([2, 2, -3]), [100, 100], m.pi / 1.5)

camera.rotate_x(0.5)
camera.rotate_y(-0.5)

light_dir = [1, 0.1, 0]

screen = camera.render(scene, light_dir)

print(len(screen[0]), len(screen))

fg = plt.figure()
ax = fg.gca()

plot = ax.imshow(screen, origin='lower')
plt.draw()
plt.pause(1000)