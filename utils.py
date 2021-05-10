Coord = tuple[int, int]


def adjacent_nodes(coord: Coord) -> tuple[Coord, Coord, Coord, Coord]:
    return ((coord[0] - 1, coord[1]),
            (coord[0] + 1, coord[1]),
            (coord[0], coord[1] - 1),
            (coord[0], coord[1] + 1))


def dijkstra(start_node: Coord, target_node: Coord, matrix: dict[Coord, object]) -> list[Coord]:
    path: dict[Coord, Coord] = {start_node: None}
    distances: dict[[Coord], int] = {start_node: 0}
    q: list[Coord] = [start_node]
    traversed: list[Coord] = []
    dist: int
    adj: Coord
    while q:
        inspected: Coord = q.pop()
        dist = distances[inspected] + 1

        for adj in adjacent_nodes(inspected):
            if adj in matrix and matrix[adj].isWalkable:
                if adj not in traversed:
                    q.append(adj)
                if adj in distances:
                    if distances[adj] > dist:
                        distances[adj] = dist
                        path[adj] = inspected
                        pass
                    pass
                else:
                    distances[adj] = dist
                    path[adj] = inspected
                    pass
                pass

            pass
        traversed.append(inspected)
        pass
    t: Coord = target_node
    ret_path: list[Coord] = [target_node]
    if t not in path:
        return []
    while t:
        ret_path.append(path[t])
        t = path[t]
        pass
    return ret_path


def tileAngle(t1, t2) -> float:
    val = (t1[0] - t2[0]) + (t1[1] - t2[1]) * 2
    return {0: .0,
            1: -90.0,
            2: 0.0,
            -2: 180.0,
            -1: 90.0}[val]
