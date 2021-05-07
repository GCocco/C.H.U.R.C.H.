from direct.actor.Actor import Actor
from panda3d.core import Shader


class ChurchActor(Actor):
    def __init__(self, model, anim):
        super().__init__(model, anim)
        pass
    pass


class Avatar(ChurchActor):
    def __init__(self):
        super().__init__("./models/pgs/avatar.egg", {"Idle": "./models/pgs/avatar-Idle.egg",
                                                     "Walk": "./models/pgs/avatar-Walk.egg"})
        # noinspection PyArgumentList
        self.setShader(Shader.load(Shader.SL_GLSL,
                                   vertex="./shaders/standard.vert",
                                   fragment="./shaders/standard.frag"))
        self.loop("Walk")
