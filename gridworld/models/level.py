from gridworld.contracts import LevelState
from gridworld.models.tile import Tile


class LevelError(ValueError):
    """JSON loading error or violation of the map contract."""


class Level:
    """To implement — S0-02. Terrain grid loaded from levels/n0.json."""

    def __init__(self, data: dict) -> None:
        raise NotImplementedError("S0-02: validate the map and create its tiles")

    @classmethod
    def load(cls, path: str) -> "Level":
        raise NotImplementedError("S0-02: read JSON and convert errors to LevelError")

    def get_start(self) -> tuple[int, int]:
        raise NotImplementedError("S0-02: return the starting coordinates")

    def get_tile(self, x: int, y: int) -> Tile:
        raise NotImplementedError("S0-02: look up a tile; raise IndexError outside the grid")

    def is_walkable(self, x: int, y: int) -> bool:
        raise NotImplementedError("S0-02: query the tile; return False outside the grid")

    def is_exit(self, x: int, y: int) -> bool:
        raise NotImplementedError("S0-02: query the tile; return False outside the grid")

    def to_state(self) -> LevelState:
        raise NotImplementedError("S0-02: create a new independent level state")
