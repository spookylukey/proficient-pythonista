from dataclasses import dataclass

from pygame import Surface

from .goods import Chest
from .robot import Robot


@dataclass
class World:
    robot: Robot
    chests: list[Chest]

    def draw(self, surface: Surface):
        self.robot.draw(surface)
        for chest in self.chests:
            chest.draw(surface)
