from tkinter import *

from scene.ProjectionService import ProjectionService
from scene.Scene import Scene

MOVE_SIZE = 5
DEGREE_CHANGE = 1


class MyGUI:
    def __init__(self, master, canvas: Canvas, scene: Scene, projectionService: ProjectionService):
        self.master = master
        self.canvas = canvas
        self.scene = scene
        self.projectionService = projectionService

        master.title("Stanislaw Pawlak Grafika Komputerowa")

        self.label = Label(master, text="Projekt 1")
        self.label.pack()

    def createScene(self, matrix, init):
        self.canvas.create_line(400, 0, 400, 800, fill="red")
        self.canvas.create_line(0, 300, 800, 300, fill="red")
        scenePoints = self.scene.get_scene(self.canvas, self.projectionService, matrix, init)
        for i in range(0, len(scenePoints)):
            self.canvas.create_line(scenePoints[i][0].x + 400, scenePoints[i][0].y + 300,
                                    scenePoints[i][1].x + 400, scenePoints[i][1].y + 300,
                                    fill=scenePoints[i][2])

    def rotateRight(self, event):
        sin, cos = self.projectionService.__getRotationParams__(-DEGREE_CHANGE)
        matrix = self.projectionService.__getRyRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def rotateLeft(self, event):
        sin, cos = self.projectionService.__getRotationParams__(DEGREE_CHANGE)
        matrix = self.projectionService.__getRyRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def rotateUp(self, event):
        sin, cos = self.projectionService.__getRotationParams__(-DEGREE_CHANGE)
        matrix = self.projectionService.__getRxRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def rotateDown(self, event):
        sin, cos = self.projectionService.__getRotationParams__(DEGREE_CHANGE)
        matrix = self.projectionService.__getRxRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def rotateZ1(self, event):
        sin, cos = self.projectionService.__getRotationParams__(-DEGREE_CHANGE)
        matrix = self.projectionService.__getRzRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def rotateZ2(self, event):
        sin, cos = self.projectionService.__getRotationParams__(DEGREE_CHANGE)
        matrix = self.projectionService.__getRzRotationMatrix__(sin, cos)
        self.redraw(matrix)

    def moveRight(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(-MOVE_SIZE, 0, 0))

    def moveLeft(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(MOVE_SIZE, 0, 0))

    def moveUp(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(0, MOVE_SIZE, 0))

    def moveDown(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(0, -MOVE_SIZE, 0))

    def moveForward(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(0, 0, +MOVE_SIZE))

    def moveBackward(self, event):
        self.redraw(self.projectionService.getTranslationMatrix(0, 0, -MOVE_SIZE))

    def zoomIn(self, event):
        self.projectionService.d -= 1
        print(self.projectionService.d)
        self.redraw(self.projectionService.getTranslationMatrix(0, 0, 0))

    def zoomOut(self, event):
        self.projectionService.d += 1
        self.redraw(self.projectionService.getTranslationMatrix(0, 0, 0))

    def redraw(self, matrix):
        self.canvas.delete("all")
        self.createScene(matrix, 0)


root = Tk()
ps = ProjectionService(100)
scene = Scene([])
w = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
gui = MyGUI(root, w, scene, ps)

w.configure(bg="black")
w.bind('<Left>', gui.moveLeft)
w.bind('<Right>', gui.moveRight)
w.bind('<Up>', gui.moveUp)
w.bind('<Down>', gui.moveDown)
w.bind('<[>', gui.moveForward)
w.bind('<]>', gui.moveBackward)
w.bind('<Control-Left>', gui.rotateLeft)
w.bind('<Control-Right>', gui.rotateRight)
w.bind('<Control-Up>', gui.rotateUp)
w.bind('<Control-Down>', gui.rotateDown)
w.bind('<o>', gui.rotateZ1)
w.bind('<p>', gui.rotateZ2)
w.bind('<q>', gui.zoomIn)
w.bind('<w>', gui.zoomOut)
w.focus_set()
w.pack()
gui.createScene(gui.projectionService.getTranslationMatrix(0, 0, 0), 1)
root.mainloop()
