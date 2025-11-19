import pygame

from .constants import TILE_SIZE
from .dirs import BASE_DIR


class Robot:
    def __init__(self) -> None:
        self.img = pygame.image.load(BASE_DIR / "robotgame/assets/robot_v2.png").convert_alpha()
        self.pos = pygame.Vector2(10 * TILE_SIZE, 7 * TILE_SIZE)  # Start in center grid cell
        self.rect = self.img.get_rect()
        self.angle = 0  # Degrees
