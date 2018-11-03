import math

import numpy as np

from object.Point3D import Point3D


class ProjectionService:
    def __init__(self, d: int):
        self.d = d

    def project(self, point3D: Point3D):
        return self.normalize(point3D)


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

    def normalize(self, point: Point3D) -> Point3D:
        return Point3D(point.x * self.d / point.z,
                       point.y * self.d / point.z,
                       self.d)
