import numpy as np

class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def rotate(self, matrix):
        pointMatrix = np.array([[self.x],
                                [self.y],
                                [self.z],
                                [1]])
        point = np.matmul(matrix, pointMatrix)
        return Point3D(point.item(0) / point.item(3), point.item(1) / point.item(3),
                       point.item(2) / point.item(3))

    def move(self, matrix):
        pointMatrix = np.array([[self.x],
                                [self.y],
                                [self.z],
                                [1]])
        point = np.matmul(matrix, pointMatrix)
        return Point3D(point.item(0) / point.item(3), point.item(1) / point.item(3),
                       point.item(2) / point.item(3))
