import pygame
import button

HEIGHT, WIDTH = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moody")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60
# load button image
play_image = pygame.image.load("assets/play_button.png").convert_alpha()
pause_image = pygame.image.load("assets/pause_button.png").convert_alpha()
next_image = pygame.image.load("assets/next_button.png").convert_alpha()

play_button = button.Button(20, 20, play_image, 0.2)
pause_button = button.Button(400, 400, pause_image, 0.1)
next_button = button.Button(500, 500, next_image, 0.3)


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    RUNNING = True
    while RUNNING:
        clock.tick(FPS)
        if play_button.draw(WIN):
            print("play what u ape")
        if pause_button.draw(WIN):
            print("pause what u ape")
        if next_button.draw(WIN):
            print("next to what u ape")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
