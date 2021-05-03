from direct.actor.Actor import Actor


class ChurchActor(Actor):
    def __init__(self, model, anim):
        super().__init__()
        self.loadModel(model)
        # WIP
        if anim:
            self.loadAnims(anim)
            pass

        pass
    pass
