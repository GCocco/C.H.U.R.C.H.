from direct.showbase.ShowBase import ShowBase
from actors import Avatar
from map.terrains import ChurchLvl1
from globals import Globals


class Base(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self._cam_pos_node = self.render.attachNewNode("cam_pos")
        self._cam_pitch_node = self._cam_pos_node.attachNewNode("cam_pitch")
        self.camera.reparentTo(self._cam_pitch_node)
        self.camera.setPos(0, -10, 3)
        self._rotate: bool = False
        self._rot = (0.0, 0.0)
        self._cam_angles = (.0, .0)

        def setRotate(val):
            if val:
                self._rot = self.mouseWatcherNode.getMouse()
                self._cam_angles = (self._cam_pos_node.getH(), self._cam_pitch_node.getP())
            self._rotate = val
            return
        self.accept("mouse2", setRotate, extraArgs=[True])
        self.accept("mouse2-up", setRotate, extraArgs=[False])

        from panda3d.core import CollisionNode, Plane, CollisionPlane
        from panda3d.core import CollisionRay, CollisionHandlerQueue, CollisionTraverser

        collider_node = self.render.attachNewNode(CollisionNode("mapCollider"))
        collider_node.node().addSolid(CollisionPlane(Plane((.0, .0, 1), (.0, .0, .0))))

        picker_node = CollisionNode('mouseRay')
        picker_node_path = self.cam.attachNewNode(picker_node)
        self._pickerRay = CollisionRay()

        picker_node.addSolid(self._pickerRay)

        self._collisionHandler = CollisionHandlerQueue()
        self._traverser = CollisionTraverser()
        self._traverser.addCollider(picker_node_path, self._collisionHandler)

        Globals.init(self)

        self._terrain = ChurchLvl1()
        self._terrain.reparentTo(self.render)
        self._av = Avatar()
        self._av.reparentTo(self.render)
        self._av.move(1, 0)

        self.doMethodLater(.01, self._raycast_task, "ray_task")
        self.addTask(self._camMovementTask, "cam_task")

        self.accept("mouse1", Globals.onClick)
        Globals.setOnClickFunction(self._av.walk)

        pass

    def _camMovementTask(self, task):
        if self.mouseWatcherNode.hasMouse():
            x = self.mouseWatcherNode.getMouseX()
            y = self.mouseWatcherNode.getMouseY()
            self._pickerRay.setFromLens(self.camNode, x, y)
            if self._rotate:
                self._cam_pos_node.setH(self._cam_angles[0] + (self._rot[0] + x)*10)
                self._cam_pitch_node.setP(self._cam_angles[1] + (self._rot[1] + y)*10)
                return task.cont
            else:
                if abs(x) > .9:
                    self._cam_pos_node.setX(self._cam_pos_node, x*.1)
                    pass
                if abs(y) > .9:
                    self._cam_pos_node.setY(self._cam_pos_node, y*.1)
                    pass
                return task.cont
        return task.cont

    def _raycast_task(self, task):
        # noinspection PyArgumentList
        self._traverser.traverse(self.render)
        if self._collisionHandler.getNumEntries() > 0:
            self._focus = Globals.focus(self._collisionHandler.getEntry(0).getSurfacePoint(self.render))
            return task.cont
        return task.cont


    pass


if __name__ == "__main__":
    Base().run()
    pass
