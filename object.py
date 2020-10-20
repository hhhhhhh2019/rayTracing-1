import numpy as np
from matrix import rotate_y


def load_obj(file):
    vertex, faces = np.array(), np.array()
    with open(file) as f:
        for line in f:
            if line.startswith('v '):
                vertex.append([float(i) for i in line.split()[1:]])
            elif line.startswith('f'):
                faces_ = line.split()[1:]
                faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

    return Object(vertex, faces)


class Object:
    def __init__(self, vert, faces):
        self.vert, self.faces = vert, faces

    def rotate_y(self, a):
        new_vert = []

        for i in self.vert:
            vert = [i[0], i[1], i[2], 1] @ rotate_y(a)
            new_vert.append(vert[:3])

        self.vert = new_vert