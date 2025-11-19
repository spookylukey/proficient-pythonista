import pygame

from .dirs import BASE_DIR
from .grid import Grid


class Robot:
    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.img = pygame.image.load(BASE_DIR / "robotgame/assets/robot_v2.png")  # .convert_alpha()
        self.rect = self.img.get_rect()
        self.angle = 90  # Degrees
        # Start in center grid cell:
        self.grid_pos = pygame.Vector2(grid.x_tiles // 2, grid.y_tiles // 2)

    @property
    def pos(self) -> pygame.Vector2:
        """
        Top left position of object in world coordinates
        """
        return self.grid_pos * self.grid.tile_size + self.grid.half_offset

    def turn_left(self) -> None:
        self.angle = (self.angle + 90) % 360

    def turn_right(self) -> None:
        self.angle = (self.angle - 90) % 360

    def go_forward(self) -> None:
        direction = pygame.Vector2(1, 0).rotate(-self.angle)
        self.grid_pos = self._constrain_grid_pos(self.grid_pos + direction)

    def go_backwards(self) -> None:
        direction = pygame.Vector2(1, 0).rotate(-self.angle)
        self.grid_pos = self._constrain_grid_pos(self.grid_pos - direction)

    def _constrain_grid_pos(self, grid_pos: pygame.Vector2) -> pygame.Vector2:
        return pygame.Vector2(
            x=max(0, min(grid_pos.x, self.grid.x_tiles - 1)),
            y=max(0, min(grid_pos.y, self.grid.y_tiles - 1)),
        )

    def draw(self, surface: pygame.Surface):
        rotated_img = pygame.transform.rotate(self.img, self.angle)
        new_rect = rotated_img.get_rect(center=self.rect.center)
        new_rect.center = (self.pos.x, self.pos.y)
        surface.blit(rotated_img, new_rect.topleft)
