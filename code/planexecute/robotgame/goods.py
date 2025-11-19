from functools import cache

import pygame

from .dirs import BASE_DIR
from .grid import Grid


@cache
def chest_img():
    return pygame.image.load(BASE_DIR / "robotgame/assets/box.png").convert_alpha()


class Chest:
    def __init__(self, grid: Grid, at_position: tuple[int, int]) -> None:
        self.img = chest_img()
        self.rect = self.img.get_rect()
        self.grid = grid
        self.grid_pos = pygame.Vector2(*at_position)

    @property
    def pos(self) -> pygame.Vector2:
        """
        Top left position of object in world coordinates
        """
        return self.grid_pos * self.grid.tile_size + self.grid.half_offset

    def draw(self, surface: pygame.Surface):
        new_rect = self.img.get_rect(center=self.rect.center)
        new_rect.center = (self.pos.x, self.pos.y)
        surface.blit(self.img, new_rect.topleft)
