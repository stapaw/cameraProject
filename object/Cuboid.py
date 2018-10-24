from tkinter import *

from object.Point3D import Point3D


class Cuboid:
    def __init__(self, point3D, length: int, width: int, height: int):
        self.startingPoint = point3D
        self.length = length
        self.width = width
        self.height = height

    def get_points(self) -> list:
        startingPoint = Point3D(self.startingPoint.x, self.startingPoint.y, self.startingPoint.z)
        points = self.__getBase__(startingPoint)

        startingPoint.z += self.height
        startingPoint.y -= self.length

        points += self.__getBase__(startingPoint)
        return points

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
        points = self.get_points()
        return [(points[0], points[1]),
                (points[1], points[2]),
                (points[2], points[3]),
                (points[3], points[0]),
                (points[0], points[4]),
                (points[1], points[5]),
                (points[2], points[6]),
                (points[3], points[7]),
                (points[4], points[5]),
                (points[5], points[6]),
                (points[6], points[7]),
                (points[7], points[4])]
