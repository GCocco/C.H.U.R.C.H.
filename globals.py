from typing import Union, TYPE_CHECKING


if TYPE_CHECKING:
    from main import Base
    from panda3d.core import NodePath


class Globals:
    __base: Union['Base', None] = None

    @staticmethod
    def init(base):
        assert Globals.__base is None
        Globals.__base = base
        return

    @staticmethod
    def loadModel(model_path) -> 'NodePath':
        return Globals.__base.loader.loadModel(model_path)

    pass
