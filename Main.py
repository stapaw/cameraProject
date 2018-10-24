from tkinter import *

from scene.ProjectionService import ProjectionService
from scene.Scene import Scene

MOVE_SIZE = 30
DEGREE_CHANGE = 1


class MyGUI:
    def __init__(self, master, canvas: Canvas, scene: Scene, projectionService: ProjectionService):
        self.master = master
        self.canvas = canvas
        self.scene = scene
        self.projectionService = projectionService

        master.title("A simple GUI")

        self.label = Label(master, text="Projection")
        self.label.pack()

    def createScene(self):
        scenePoints = self.scene.get_scene(self.canvas, self.projectionService)
        for i in range(0, len(scenePoints) - 1):
            if i % 2 == 0:
                self.canvas.create_line(scenePoints[i].item(0), scenePoints[i].item(1),
                                        scenePoints[i + 1].item(0), scenePoints[i + 1].item(1), fill="white")

    def rotateRight(self, event):
        self.projectionService.y_degree += DEGREE_CHANGE
        self.redraw()

    def rotateLeft(self, event):
        self.projectionService.y_degree -= DEGREE_CHANGE
        self.redraw()

    def rotateUp(self, event):
        self.projectionService.x_degree += DEGREE_CHANGE
        self.redraw()

    def rotateDown(self, event):
        self.projectionService.x_degree -= DEGREE_CHANGE
        self.redraw()

    def moveRight(self, event):
        self.projectionService.x_move -= MOVE_SIZE
        self.redraw()

    def moveLeft(self, event):
        self.projectionService.x_move += MOVE_SIZE
        self.redraw()

    def moveUp(self, event):
        self.projectionService.y_move += MOVE_SIZE
        self.redraw()

    def moveDown(self, event):
        self.projectionService.y_move -= MOVE_SIZE
        self.redraw()

    def zoomIn(self, event):
        self.projectionService.d -= 1
        print(self.projectionService.d)
        self.redraw()

    def zoomOut(self, event):
        self.projectionService.d += 1
        self.redraw()

    def redraw(self):
        self.canvas.delete("all")
        self.createScene()


root = Tk()
ps = ProjectionService(15)
scene = Scene()
w = Canvas(root, width=600, height=400, bd=0, highlightthickness=0)
gui = MyGUI(root, w, scene, ps)

w.configure(bg="black")
w.bind('<Left>', gui.moveLeft)
w.bind('<Right>', gui.moveRight)
w.bind('<Up>', gui.moveUp)
w.bind('<Down>', gui.moveDown)
w.bind('<Control-Left>', gui.rotateLeft)
w.bind('<Control-Right>', gui.rotateRight)
w.bind('<Control-Up>', gui.rotateUp)
w.bind('<Control-Down>', gui.rotateDown)
w.bind('<q>', gui.zoomIn)
w.bind('<w>', gui.zoomOut)
w.focus_set()
w.pack()
gui.createScene()
root.mainloop()
