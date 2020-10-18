import numpy as np


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

        print(vert, faces)