import pygame
import button
import textbutton
import tkinter as tk
import fnmatch
# from musicplayertest import listbox
import pygame_gui
import os
from pygame import mixer
import vlc

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
# details for music
# musicpath = "E:\\AIProjectFrontEnd\\music"
musicpath = "E:/AIProjectFrontEnd/music"
pattern = "*.mp3"
mixer.init()
# listbox
selectionlist = pygame_gui.elements.UISelectionList(
    relative_rect=pygame.Rect((400, 400), (200, 200)), item_list=[], manager=manager, allow_double_clicks=False, object_id="#musicselectionlist")

# Initial Insert into listbox
itemlist = []
for root, dirs, files in os.walk(musicpath):
    for filename in fnmatch.filter(files, pattern):
        itemlist.append(filename)
selectionlist.add_items(itemlist)

# Music Player Buttons
play_image = pygame.image.load("assets/play_button.png").convert_alpha()
pause_image = pygame.image.load("assets/pause_button.png").convert_alpha()
next_image = pygame.image.load("assets/next_button.png").convert_alpha()
prev_image = pygame.image.load("assets/prev_button.png").convert_alpha()

play_button = button.Button(200, 700, play_image, 0.5)
pause_button = button.Button(150, 700, pause_image, 0.5)
next_button = button.Button(250, 700, next_image, 0.5)
prev_button = button.Button(100, 700, prev_image, 0.5)
# Main Menu Button
musicplayer_button = textbutton.Button("Music Player", 150, 150, (300, 300), 6)

# Back Button
back_button = textbutton.Button("Back", 50, 50, (0, 0), 6)

# Select Song Button
select_song_button = textbutton.Button("select", 50, 50, (400, 700), 6)


def select_song():
    elemselected = selectionlist.get_single_selection()
    # mixer.music.load(musicpath+"\\"+elemselected)
    # print(musicpath+"\\"+elemselected)
    # mixer.music.play()
    filetoplay = vlc.MediaPlayer("file:///"+musicpath+"/"+elemselected)
    filetoplay.play()


# Refresh List Button
refresh_list_button = textbutton.Button("refresh", 50, 50, (500, 700), 6)


def refreshlist():
    for i in selectionlist.item_list:
        selectionlist.remove_items(i['text'])


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
        WIN.fill(LILAC)
        if menu_state == "player":
            # Show music player
            manager.draw_ui(WIN)
            play_button.draw(WIN)
            pause_button.draw(WIN)
            next_button.draw(WIN)
            prev_button.draw(WIN)
            if select_song_button.draw(WIN):
                select_song()
            if refresh_list_button.draw(WIN):
                refreshlist()
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
