from tkinter import *

from object.Cuboid import Cuboid
from object.Point3D import Point3D
from scene.ProjectionService import ProjectionService


class Scene:
    def __init__(self, figures):
        self.figures = figures

    def get_scene(self, canvas: Canvas, projection: ProjectionService, matrix, init):
        if (init == 1):
            self.figures = self.__initScene__()
            for figure in self.figures:
                figure.init_points()
        fs = []
        for figure in self.figures:
            figure.update_points(matrix)
            linesPoints = figure.getPointsForLines(canvas)
            for oneline in linesPoints:
                line = (projection.project(oneline[0]), projection.project(oneline[1]), figure.getColor())
                fs.append(line)
        print()
        return fs

    def __initScene__(self):
        figures = []
        figures.append(Cuboid(point3D=Point3D(x=5, y=5, z=100), width=20, height=20, length=20, color="blue"))
        figures.append(Cuboid(point3D=Point3D(x=5, y=-25, z=100), width=20, height=20, length=20, color="white"))
        figures.append(Cuboid(point3D=Point3D(x=-25, y=5, z=100), width=20, height=20, length=20, color="red"))
        figures.append(Cuboid(point3D=Point3D(x=-25, y=-25, z=100), width=20, height=20, length=20, color="green"))
        return figures
