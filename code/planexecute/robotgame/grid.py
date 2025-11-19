from dataclasses import dataclass
from functools import cached_property


@dataclass(frozen=True)
class Grid:
    x_tiles: int
    y_tiles: int
    tile_size: int

    @cached_property
    def width(self) -> int:
        return self.tile_size * self.x_tiles

    @cached_property
    def height(self) -> int:
        return self.tile_size * self.y_tiles
