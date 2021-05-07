from panda3d.core import NodePath
from globals import Globals, standardShader
from enum import IntEnum


class BaseTile(NodePath):
    _model_ref = None

    @property
    def getModelRef(self) -> NodePath:
        if BaseTile._model_ref:
            return BaseTile._model_ref
        BaseTile._model_ref = Globals.loadModel("./models/tiles/tile.egg")
        return BaseTile._model_ref

    def setPos(self, x, y):
        super().setPos(float(x), float(y), 0.0)
        return

    def __init__(self, name: str, is_walkable=True, can_edit=True):
        super().__init__(name)
        self._walkable = is_walkable
        self._can_edit = can_edit
        self.setShader(standardShader)
        pass

    @property
    def isWalkable(self):
        return self._walkable

    @property
    def canEdit(self):
        return self._can_edit
    pass


class EmptyTile(BaseTile):
    _model_ref = None

    def __init__(self):
        super().__init__("empty", is_walkable=True, can_edit=False)
        self.getModelRef.instanceTo(self)
        pass
    pass


class EditableTile(BaseTile):
    _model_ref = None

    @property
    def getModelRef(self) -> NodePath:
        if BaseTile._model_ref:
            return BaseTile._model_ref
        BaseTile._model_ref = Globals.loadModel("./models/tiles/tile.egg")

    def __init__(self, is_walkable=True):
        super().__init__("Editable", is_walkable=is_walkable, can_edit=True)
        self.getModelRef.instanceTo(self)
        pass
    pass


class WallTile(BaseTile):
    _model_ref = None

    @property
    def getModelRef(self) -> NodePath:
        if WallTile._model_ref:
            return WallTile._model_ref
        WallTile._model_ref = Globals.loadModel("./models/tiles/wall.egg")
        return WallTile._model_ref

    def __init__(self):
        super().__init__("Wall", is_walkable=False, can_edit=False)
        self.getModelRef.instanceTo(self)


class TileMap:
    Empty = EmptyTile
    Wall = WallTile
    Buildable = EditableTile
    pass
