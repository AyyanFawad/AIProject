import pygame
import button
import textbutton
import tkinter as tk
import fnmatch
# from musicplayertest import listbox
import pygame_gui

HEIGHT, WIDTH = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moody")


# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LILAC = (200, 162, 200)

# Game Variables
FPS = 60
menu_state = "main"

# manager
manager = pygame_gui.UIManager((600, 800))

# listbox
selectionlist = pygame_gui.elements.UISelectionList(
    relative_rect=pygame.Rect((400, 400), (200, 200)), item_list=["0", "1", "2", "3", "4", "5"], manager=manager, allow_double_clicks=False, object_id="#musicselectionlist")

# Music Player Buttons
play_image = pygame.image.load("assets/play_button.png").convert_alpha()
pause_image = pygame.image.load("assets/pause_button.png").convert_alpha()
next_image = pygame.image.load("assets/next_button.png").convert_alpha()

play_button = button.Button(50, 100, play_image, 1)
pause_button = button.Button(50, 200, pause_image, 1)
next_button = button.Button(50, 300, next_image, 1)

# Main Menu Button
musicplayer_button = textbutton.Button("Music Player", 150, 150, (300, 300), 6)

# Back Button
back_button = textbutton.Button("Back", 50, 50, (0, 0), 6)


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    global menu_state
    WIN.fill(LILAC)
    clock = pygame.time.Clock()
    RUNNING = True

    while RUNNING:
        clock.tick(FPS)
        # UIREFRESHRATE = clock.tick(60)/1000
        # if play_button.draw(WIN):
        #     print("play what u ape")
        # if pause_button.draw(WIN):
        #     print("pause what u ape")
        # if next_button.draw(WIN):
        #     print("next to what u ape")
        WIN.fill(LILAC)
        if menu_state == "player":
            # Show music player
            play_button.draw(WIN)
            pause_button.draw(WIN)
            next_button.draw(WIN)
            manager.draw_ui(WIN)
            if back_button.draw(WIN):
                menu_state = "main"
        elif menu_state == "main":
            if musicplayer_button.draw(WIN):
                menu_state = "player"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            manager.process_events(event)

        manager.update(clock.tick(60)/1000)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
