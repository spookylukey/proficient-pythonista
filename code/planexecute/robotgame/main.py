import pygame

from robotgame.grid import Grid
from robotgame.robot import Robot

from .constants import TILE_SIZE, X_TILES, Y_TILES

GRID = Grid(x_tiles=X_TILES, y_tiles=Y_TILES, tile_size=TILE_SIZE)


def main():
    pygame.init()  # Init Pygame
    win = pygame.display.set_mode((GRID.width, GRID.height))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(150, 150)

    # Create robot instance and set initial position
    robot = Robot(grid=GRID)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    robot.turn_left()
                elif event.key == pygame.K_RIGHT:
                    robot.turn_right()
                elif event.key == pygame.K_UP:
                    robot.go_forward()
                elif event.key == pygame.K_DOWN:
                    robot.go_backwards()

        # Draw background
        win.fill((255, 255, 255))
        for y in range(0, GRID.y_tiles):
            pygame.draw.line(
                win,
                color=(0, 0, 0),
                start_pos=(0, y * GRID.tile_size),
                end_pos=(GRID.width, y * GRID.tile_size),
            )
        for x in range(0, GRID.x_tiles):
            pygame.draw.line(
                win,
                color=(0, 0, 0),
                start_pos=(x * GRID.tile_size, 0),
                end_pos=(x * GRID.tile_size, GRID.height),
            )

        # Draw robot
        rotated_img = pygame.transform.rotate(robot.img, robot.angle)
        new_rect = rotated_img.get_rect(center=robot.rect.center)
        new_rect.center = (robot.pos.x, robot.pos.y)
        win.blit(rotated_img, new_rect.topleft)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
