from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

from globals import Globals, standardShader


class ChurchActor(Actor):
    def __init__(self, model: str, anim: dict[str, str]):
        super().__init__(model, anim)
        pass

    def move(self, x: int, y: int) -> None:
        super().setPos(x+.5, y+.5, 0.0)
        return

    def getCoord(self) -> tuple[int, int]:
        return int(self.getX()), int(self.getY())

    def walk(self, destination: tuple[int, int]):
        path = Globals.getPath(self.getCoord(), destination)
        if not path:
            return

        actor_seq = Sequence()
        print(path)
        path.pop()
        while path:
            node = path.pop()
            print(node)
            actor_seq.append(self.posInterval(.3, (node[0] + .5, node[1] + .5, .0), name="walk"))
            pass
        print(actor_seq)
        actor_seq.start()

        pass
    pass


class Avatar(ChurchActor):
    def __init__(self):
        super().__init__("./models/pgs/avatar.egg", {"Idle": "./models/pgs/avatar-Idle.egg",
                                                     "Walk": "./models/pgs/avatar-Walk.egg"})
        self.setShader(standardShader)
        self.loop("Walk")
