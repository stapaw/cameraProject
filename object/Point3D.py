import numpy as np

class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def rotate(self, matrix):
        return np.matmul(matrix, self.__get_point_matrix())

    def move(self, matrix):
        moved = np.matmul(matrix, self.__get_point_matrix())
        self.x = moved.item(0)
        self.y = moved.item(1)
        self.z = moved.item(2)

    def __get_point_matrix(self):
        return np.array([[self.x],
                         [self.y],
                         [self.z],
                         [1]])
