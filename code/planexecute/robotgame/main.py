import pygame

from robotgame.robot import Robot

from .constants import HEIGHT, TILE_SIZE, WIDTH, X_TILES, Y_TILES


def main():
    pygame.init()  # Init Pygame
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    pygame.key.set_repeat(150, 150)

    # Create robot instance and set initial position
    robot = Robot()

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    robot.angle = (robot.angle + 90) % 360
                elif event.key == pygame.K_RIGHT:
                    robot.angle = (robot.angle - 90) % 360
                elif event.key == pygame.K_UP:
                    direction = pygame.Vector2(1, 0).rotate(-robot.angle)
                    robot.pos += direction * TILE_SIZE
                elif event.key == pygame.K_DOWN:
                    direction = pygame.Vector2(1, 0).rotate(-robot.angle)
                    robot.pos -= direction * TILE_SIZE

        # Keep robot within grid bounds
        robot.pos.x = max(0, min(robot.pos.x, (X_TILES - 1) * TILE_SIZE))
        robot.pos.y = max(0, min(robot.pos.y, (Y_TILES - 1) * TILE_SIZE))

        # Draw background
        win.fill((255, 255, 255))

        # Draw robot
        rotated_img = pygame.transform.rotate(robot.img, robot.angle)
        new_rect = rotated_img.get_rect(center=robot.rect.center)
        new_rect.center = (robot.pos.x + TILE_SIZE / 2, robot.pos.y + TILE_SIZE / 2)
        win.blit(rotated_img, new_rect.topleft)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
