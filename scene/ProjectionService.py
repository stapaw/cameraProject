import math

import numpy as np

from object.Point3D import Point3D


class ProjectionService:
    def __init__(self, d: int):
        self.d = d

    def project(self, point3D: Point3D, move_matrix, rotation_matrix=[]):
        # p = np.array([[point3D.x],
        #               [point3D.y],
        #               [point3D.z],
        #               [1]])

        point3D = point3D.move(move_matrix)
        point3D = point3D.rotate(move_matrix)
        m = np.array([[point3D.x * self.d / point3D.z],
                      [point3D.y * self.d / point3D.z],
                      [self.d],
                      [1]])

        return Point3D(point3D.x * self.d / point3D.z,
                       point3D.y * self.d / point3D.z,
                       self.d)

    def __rotateRx__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.x_degree)
        pointMatrix = rotatedPoint
        return np.matmul(self.__getRxRotationMatrix__(sin, cos), pointMatrix)


    def __rotateRy__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.y_degree)
        pointMatrix = rotatedPoint
        # res = self.__getRyRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRyRotationMatrix__(sin, cos), pointMatrix)
        return res

    def __rotateRz__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.z_degree)
        pointMatrix = rotatedPoint
        # res = self.__getRzRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRzRotationMatrix__(sin, cos), pointMatrix)
        return res

    def __getRxRotationMatrix__(self, sin, cos) -> np.array:
        return np.array([[1, 0, 0, 0],
                         [0, cos, -sin, 0],
                         [0, sin, cos, 0],
                         [0, 0, 0, 1]])

    def __getRyRotationMatrix__(self, sin, cos) -> np.array:
        return np.array([[cos, 0, sin, 0],
                         [0, 1, 0, 0],
                         [-sin, 0, cos, 0],
                         [0, 0, 0, 1]])

    def __getRzRotationMatrix__(self, sin, cos) -> np.array:
        return np.array([[cos, -sin, 0, 0],
                         [sin, cos, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])

    def __getRotationParams__(self, degree):
        rad = math.radians(degree)
        return math.sin(rad), math.cos(rad)

    def getTranslationMatrix(self, x, y, z):
        return np.array([[1, 0, 0, x],
                         [0, 1, 0, y],
                         [0, 0, 1, z],
                         [0, 0, 0, 1]])
