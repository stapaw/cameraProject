from tkinter import *

from object.Cuboid import Cuboid
from object.Point3D import Point3D
from scene.ProjectionService import ProjectionService


class Scene:
    def __init__(self):
        pass

    def get_scene(self, canvas: Canvas, projection: ProjectionService):
        figures = self.__initScene__()
        fs = []
        for figure in figures:
            linesPoints = figure.getPointsForLines(canvas)
            for line in linesPoints:
                fs.append(projection.project(line[0]))
                fs.append(projection.project(line[1]))
        return fs

    def __initScene__(self):
        figures = []
        figures.append(Cuboid(point3D=Point3D(x=50, y=50, z=50.0), width=100, height=20, length=70))
        figures.append(Cuboid(point3D=Point3D(x=170, y=50, z=50.0), width=100, height=20, length=70))
        return figures
