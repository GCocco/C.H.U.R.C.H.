from typing import Union, TYPE_CHECKING
from panda3d.core import Shader


if TYPE_CHECKING:
    from main import Base
    from panda3d.core import NodePath
    from map.terrains import ChurchTerrain


# noinspection PyArgumentList
standardShader: Shader = Shader.load(Shader.SL_GLSL,
                                     vertex="./shaders/standard.vert",
                                     fragment="./shaders/standard.frag")


class Globals:
    _base: Union['Base', None] = None
    _terrain: 'ChurchTerrain' = None
    _focus_coord: tuple[int, int] = 0, 0
    _on_click_func = lambda x: print(x)

    @staticmethod
    def getCoord() -> tuple[int, int]:
        return Globals._focus_coord

    @staticmethod
    def focus(pos: tuple[float, float, float]):
        if pos[0] < 0 or pos[1] < 0:
            Globals._focus_coord = (None, None)
            return
        if int(pos[0]) is not Globals._focus_coord[0] or int(pos[1]) is not Globals._focus_coord[1]:
            Globals._focus_coord = (int(pos[0]), int(pos[1]))
            return
        return

    @staticmethod
    def onClick():
        if Globals._focus_coord is not (None, None):
            Globals._on_click_func(Globals._focus_coord)
            pass
        return

    @staticmethod
    def setOnClickFunction(on_click_func):
        Globals._on_click_func = on_click_func

    @staticmethod
    def init(base):
        assert Globals._base is None
        Globals._base = base
        return

    @staticmethod
    def setTerrain(terrain: 'ChurchTerrain'):
        Globals._terrain = terrain
        return

    @staticmethod
    def getPath(start_node, target_node):
        return Globals._terrain.path(start_node, target_node)

    @staticmethod
    def loadModel(model_path) -> 'NodePath':
        return Globals._base.loader.loadModel(model_path)

    pass
