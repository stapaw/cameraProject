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

        master.title("A simple GUI")

        self.label = Label(master, text="Projection")
        self.label.pack()

    def createScene(self):
        self.canvas.create_line(400, 0, 400, 800, fill="red")
        self.canvas.create_line(0, 300, 800, 300, fill="red")
        scenePoints = self.scene.get_scene(self.canvas, self.projectionService)
        for i in range(0, len(scenePoints)):
            self.canvas.create_line(scenePoints[i][0].item(0) + 400, scenePoints[i][0].item(1) + 300,
                                    scenePoints[i][1].item(0) + 400, scenePoints[i][1].item(1) + 300,
                                    fill=scenePoints[i][2])

    def rotateRight(self, event):
        self.projectionService.y_degree -= DEGREE_CHANGE
        self.redraw()

    def rotateLeft(self, event):
        self.projectionService.y_degree += DEGREE_CHANGE
        self.redraw()

    def rotateUp(self, event):
        self.projectionService.x_degree -= DEGREE_CHANGE
        self.redraw()

    def rotateDown(self, event):
        self.projectionService.x_degree += DEGREE_CHANGE
        self.redraw()

    def rotateZ1(self, event):
        self.projectionService.z_degree -= DEGREE_CHANGE
        self.redraw()

    def rotateZ2(self, event):
        self.projectionService.z_degree += DEGREE_CHANGE
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

    def moveForward(self, event):
        self.projectionService.z_move += MOVE_SIZE
        self.redraw()

    def moveBackward(self, event):
        self.projectionService.z_move -= MOVE_SIZE
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
ps = ProjectionService(100)
scene = Scene()
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
gui.createScene()
root.mainloop()
