from panda3d.core import NodePath

from globals import Globals
from utils import dijkstra
from map.tiles import TileMap


class TerrainError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        pass
    pass


class MatrixError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        pass
    pass


# la matrice passata è nella forma List[Dict[Tuple[int, int], IntEnum]]

class ChurchTerrain(NodePath):
    def __init__(self, matrix):
        super().__init__("ChurchTerrain")
        self._focusXY: tuple[int, int] = (0, 0)
        self._matrix: dict[tuple[int, int], object] = {}

        for tile in matrix:
            if tile in self._matrix:
                raise TerrainError(f'tried to build in {tile}, already {self._matrix[tile]} there')
            if tile[0] < 0 or tile[1] < 0:
                raise MatrixError(f'error building in {tile} is not allowed. can only build on positive coordinates')
            t = matrix[tile]()
            t.reparentTo(self)
            t.setPos(tile[0], tile[1])
            self._matrix[tile] = t
        Globals.setTerrain(self)
        pass

    def focus(self, x: int, y: int):
        print(x, y)
        return

    def path(self, start_node: tuple[int, int], target_node: tuple[int, int]) -> list[tuple[int, int]]:
        if start_node in self._matrix:
            return dijkstra(start_node, target_node, self._matrix)
        return []

    pass


class ChurchLvl1(ChurchTerrain):
    def __init__(self):
        super().__init__({(0, 0): TileMap.Wall,
                          (0, 1): TileMap.Wall,
                          (0, 2): TileMap.Wall,
                          (0, 3): TileMap.Wall,
                          (1, 0): TileMap.Empty,
                          (2, 0): TileMap.Empty,
                          (3, 0): TileMap.Empty,
                          (1, 1): TileMap.Empty,
                          (2, 1): TileMap.Empty,
                          (3, 1): TileMap.Empty,
                          (1, 2): TileMap.Empty,
                          (2, 2): TileMap.Empty,
                          (3, 2): TileMap.Empty})

        print(self.path((1, 1), (2, 2)))

        pass

    pass
