from gridworld.contracts import TileKind


class Tile:
    """To implement — S0-02. Terrain without player or rendering logic."""

    def __init__(self, kind: TileKind) -> None:
        raise NotImplementedError("S0-02: validate and store the tile kind")

    def is_walkable(self) -> bool:
        raise NotImplementedError("S0-02: a wall tile is not walkable")

    def is_exit(self) -> bool:
        raise NotImplementedError("S0-02: identify the exit")

    def to_state(self) -> TileKind:
        raise NotImplementedError("S0-02: expose the terrain kind")
