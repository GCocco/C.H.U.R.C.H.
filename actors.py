from direct.actor.Actor import Actor
from panda3d.core import Shader

from globals import Globals, standardShader


class ChurchActor(Actor):
    def __init__(self, model: str, anim: dict[str, str]):
        super().__init__(model, anim)
        pass

    def setPos(self, x: int, y: int) -> None:
        super().setPos(x+.5, y+.5, 0.0)
        return

    def getCoord(self) -> tuple[int, int]:
        return int(self.getX()), int(self.getY())

    def walk(self, destination: tuple[int, int]):
        path = Globals.getPath(self.getCoord(), destination)
        print(path)
        pass

    pass


class Avatar(ChurchActor):
    def __init__(self):
        super().__init__("./models/pgs/avatar.egg", {"Idle": "./models/pgs/avatar-Idle.egg",
                                                     "Walk": "./models/pgs/avatar-Walk.egg"})
        self.setShader(standardShader)
        self.loop("Walk")
