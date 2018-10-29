import math

import numpy as np

from object.Point3D import Point3D


class ProjectionService:
    def __init__(self, d: int):
        self.d = -d
        self.x_move = 0
        self.y_move = 0
        self.z_move = 0
        self.x_degree = 0
        self.y_degree = 0
        self.z_degree = 0

    def project(self, point3D: Point3D):
        print(self.x_move, self.y_move)
        p = np.array([[point3D.x],
                      [point3D.y],
                      [point3D.z],
                      [1]])

        point = np.matmul(self.getTranslationMatrix(), p)
        point = self.rotate(point)
        new_point3D = Point3D(point.item(0) / point.item(3), point.item(1) / point.item(3),
                              point.item(2) / point.item(3))
        m = np.array([[new_point3D.x * self.d / new_point3D.z],
                      [new_point3D.y * self.d / new_point3D.z],
                      [self.d],
                      [1]])

        return m

    # def move(self, point) -> Point3D:
    #     movedPoint = Point3D(point.x, point.y, point.z)
    #     movedPoint.x += self.x_move
    #     movedPoint.y += self.y_move
    #     movedPoint.z += self.z_move
    #     return movedPoint

    def rotate(self, point) -> np.array:
        rotatedPoint = point
        rotatedPoint = self.__rotateRx__(rotatedPoint)
        rotatedPoint = self.__rotateRy__(rotatedPoint)
        rotatedPoint = self.__rotateRz__(rotatedPoint)

        return rotatedPoint

    def __rotateRx__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.x_degree)
        pointMatrix = rotatedPoint
        # res = self.__getRxRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRxRotationMatrix__(sin, cos), pointMatrix)
        # rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        # rotatedPoint.x /= w
        # rotatedPoint.y /= w
        # rotatedPoint.z /= w
        return res

    def __rotateRy__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.y_degree)
        pointMatrix = rotatedPoint
        # res = self.__getRyRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRyRotationMatrix__(sin, cos), pointMatrix)
        # rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        # rotatedPoint.x /= w
        # rotatedPoint.y /= w
        # rotatedPoint.z /= w
        return res

    def __rotateRz__(self, rotatedPoint: np.array) -> np.array:
        sin, cos = self.__getRotationParams__(self.z_degree)
        pointMatrix = rotatedPoint
        # res = self.__getRzRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRzRotationMatrix__(sin, cos), pointMatrix)
        # rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        # rotatedPoint.x /= w
        # rotatedPoint.y /= w
        # rotatedPoint.z /= w
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

    def getTranslationMatrix(self):
        return np.array([[1, 0, 0, self.x_move],
                         [0, 1, 0, self.y_move],
                         [0, 0, 1, self.z_move],
                         [0, 0, 0, 1]])
