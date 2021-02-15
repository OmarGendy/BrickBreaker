import pygame
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
file_dir = os.path.join(main_dir, "files")

# GAME CONSTANTS #
speed = 1                    # Speed of the player
ball_speed = 1               # Speed of the ball
width = 100                  # Width of the player
screen_width = 2000          # Width of the screen

pygame.init()
screen = pygame.display.set_mode(size=(screen_width, 1000), flags=0, depth=0, display=0, vsync=0)


def main():
    # Title and Icon
    pygame.display.set_caption("Brick Breaker")
    icon = pygame.image.load(os.path.join(file_dir, "brick.png"))
    pygame.display.set_icon(icon)

    # Player Initialization
    player_color = (0, 100, 100)
    player = pygame.rect.Rect(1000-(width/2), 980, width, 10)
    pygame.draw.rect(screen, player_color, player)

    # Ball Initialization
    ball_color = (0, 255, 255)
    ball = pygame.rect.Rect(995, 750, 10, 10)
    pygame.draw.circle(screen, ball_color, (ball.x, ball.y), 5)

    # Main Game Loop
    running = True
    while running:

        # Closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Pressing a button
        keys = pygame.key.get_pressed()

        # Left and right controls, with edge detection
        if keys[pygame.K_LEFT] and player.x > 1:
            pygame.draw.rect(screen, (0, 0, 0), player)
            player.move_ip(-1 * speed, 0)
            pygame.draw.rect(screen, player_color, player)
        if keys[pygame.K_RIGHT] and player.x + width < screen_width - 1:
            pygame.draw.rect(screen, (0, 0, 0), player)
            player.move_ip(1 * speed, 0)
            pygame.draw.rect(screen, player_color, player)
        pygame.display.update()


if __name__ == "__main__":
    main()