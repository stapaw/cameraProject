from tkinter import *

import numpy as np

from object.Point3D import Point3D
from scene import ProjectionService


class Cuboid:
    def __init__(self, point3D, length: int, width: int, height: int, color):
        self.startingPoint = point3D
        self.length = length
        self.width = width
        self.height = height
        self.color = color
        self.points = []

    def init_points(self) -> list:
        startingPoint = Point3D(self.startingPoint.x, self.startingPoint.y, self.startingPoint.z)
        points = self.__getBase__(startingPoint)

        startingPoint.z += self.height
        startingPoint.y -= self.length

        points += self.__getBase__(startingPoint)
        self.points = points
        return points

    def set_points(self, points):
        self.points = points

    def update_points(self, projection: ProjectionService, matrix: np.array):
        for i in range(0, len(self.points)):
            self.points[i] = projection.project(self.points[i], matrix)
        print(self.points[0].x, self.points[0].y, self.points[0].z)
        print(self.points[1].x, self.points[1].y, self.points[1].z)
        print("next:")


    def __getBase__(self, startingPoint):
        points = []
        points.append(Point3D(startingPoint.x, startingPoint.y, startingPoint.z))

        startingPoint.x += self.width
        points.append(Point3D(startingPoint.x, startingPoint.y, startingPoint.z))

        startingPoint.y += self.length
        points.append(Point3D(startingPoint.x, startingPoint.y, startingPoint.z))

        startingPoint.x -= self.width
        points.append(Point3D(startingPoint.x, startingPoint.y, startingPoint.z))

        return points

    def getPointsForLines(self, canvas: Canvas):
        return [(self.points[0], self.points[1]),
                (self.points[1], self.points[2]),
                (self.points[2], self.points[3]),
                (self.points[3], self.points[0]),
                (self.points[0], self.points[4]),
                (self.points[1], self.points[5]),
                (self.points[2], self.points[6]),
                (self.points[3], self.points[7]),
                (self.points[4], self.points[5]),
                (self.points[5], self.points[6]),
                (self.points[6], self.points[7]),
                (self.points[7], self.points[4])]

    def getColor(self):
        return self.color
