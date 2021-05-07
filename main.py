from direct.showbase.ShowBase import ShowBase
from actors import Avatar
from map.terrains import ChurchLvl1
from globals import Globals


class Base(ShowBase):
    def __init__(self):
        super().__init__()
        Globals.init(self)

        self._av = Avatar()
        self._av.reparentTo(self.render)
        self._terrain = ChurchLvl1()
        self._terrain.reparentTo(self.render)
        pass
    pass


if __name__ == "__main__":
    Base().run()
    pass
