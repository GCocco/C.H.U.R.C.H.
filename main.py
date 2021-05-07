from direct.showbase.ShowBase import ShowBase
from actors import Avatar
from map.terrains import ChurchLvl1
from globals import Globals


class Base(ShowBase):
    def __init__(self):
        super().__init__()

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
        self._av.setPos(1, 0)
        self._av.walk((2, 2))

        self.doMethodLater(.01, self._raycast_task, "ray_task")
        self.addTask(self._camMovementTask, "cam_task")

        self.accept("mouse1", Globals.onClick)

        pass

    def _camMovementTask(self, task):
        if self.mouseWatcherNode.hasMouse():
            x = self.mouseWatcherNode.getMouseX()
            y = self.mouseWatcherNode.getMouseY()
            self._pickerRay.setFromLens(self.camNode, x, y)
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
