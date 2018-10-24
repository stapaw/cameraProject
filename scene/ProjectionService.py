import math

import numpy as np

from object.Point3D import Point3D


class ProjectionService:
    def __init__(self, d: int):
        self.d = d
        self.x_move = 0
        self.y_move = 0
        self.z_move = 0
        self.x_degree = 0
        self.y_degree = 0
        self.z_degree = 0
        self.projectionMatrix = np.array([[1, 0, 0, 0],
                                          [0, 1, 0, 0],
                                          [0, 0, 1, 0],
                                          [0, 0, 1 / d, 0]]
                                         )

    def project(self, point3D: Point3D):
        point = self.move(point3D)
        point = self.rotate(point)
        m = np.array([[point.x * self.d / point.z],
                      [point.y * self.d / point.z],
                      [self.d],
                      [1]])

        return m

    def move(self, point) -> Point3D:
        movedPoint = Point3D(point.x, point.y, point.z)
        movedPoint.x += self.x_move
        movedPoint.y += self.y_move
        movedPoint.z += self.z_move
        return movedPoint

    def rotate(self, point) -> Point3D:
        rotatedPoint = Point3D(point.x, point.y, point.z)
        rotatedPoint = self.__rotateRx__(rotatedPoint)
        rotatedPoint = self.__rotateRy__(rotatedPoint)
        rotatedPoint = self.__rotateRz__(rotatedPoint)

        return rotatedPoint

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

    def __rotateRx__(self, rotatedPoint: Point3D) -> Point3D:
        sin, cos = self.__getRotationParams__(self.x_degree)
        pointMatrix = np.array([rotatedPoint.x,
                                rotatedPoint.y,
                                rotatedPoint.z, 1])
        # res = self.__getRxRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRxRotationMatrix__(sin, cos), pointMatrix)
        rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        rotatedPoint.x /= w
        rotatedPoint.y /= w
        rotatedPoint.z /= w
        return rotatedPoint

    def __rotateRy__(self, rotatedPoint: Point3D) -> Point3D:
        sin, cos = self.__getRotationParams__(self.y_degree)
        pointMatrix = np.array([rotatedPoint.x,
                                rotatedPoint.y,
                                rotatedPoint.z, 1])
        # res = self.__getRyRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRyRotationMatrix__(sin, cos), pointMatrix)
        rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        rotatedPoint.x /= w
        rotatedPoint.y /= w
        rotatedPoint.z /= w
        return rotatedPoint

    def __rotateRz__(self, rotatedPoint: Point3D) -> Point3D:
        sin, cos = self.__getRotationParams__(self.z_degree)
        pointMatrix = np.array([rotatedPoint.x,
                                rotatedPoint.y,
                                rotatedPoint.z, 1])
        # res = self.__getRzRotationMatrix__(sin, cos) * pointMatrix
        res = np.matmul(self.__getRzRotationMatrix__(sin, cos), pointMatrix)
        rotatedPoint.x, rotatedPoint.y, rotatedPoint.z, w = res[0], res[1], res[2], res[3]
        rotatedPoint.x /= w
        rotatedPoint.y /= w
        rotatedPoint.z /= w
        return rotatedPoint

    def __getRotationParams__(self, degree):
        rad = math.radians(degree)
        return math.sin(rad), math.cos(rad)
