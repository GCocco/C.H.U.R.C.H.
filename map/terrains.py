from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Tuple

from panda3d.core import NodePath
from utils import dijkstra
from map.tiles import TileMap


# la matrice passata è nella forma List[Dict[Tuple[int, int], IntEnum]]

class ChurchTerrain(NodePath):
    def __init__(self, matrix):
        super().__init__("ChurchTerrain")
        self._matrix = {}

        for tile in matrix:
            t = matrix[tile]()
            t.reparentTo(self)
            t.setPos(tile[0], tile[1])
            self._matrix[tile] = t
        pass

    def path(self, start_node, target_node):
        pass

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

    def path(self, start_node: tuple[int, int], target_node: tuple[int, int]) -> list[tuple[int, int]]:
        if start_node in self._matrix:
            return dijkstra(start_node, target_node, self._matrix)
        return []
    pass
