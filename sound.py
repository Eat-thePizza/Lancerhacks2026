import pygame
import time

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

#Description: Plays a sound (MUST HAVE SOMETHING RUNNING AFTER SO IT HAS THE TIME TO PLAY)
def background_music(path: str):
    pygame.mixer.music.load(path)
    print("Mixer frequency:", pygame.mixer.get_init())
    pygame.mixer.music.play(0)


# Tester Call
#background_music("testingmusic.mp3")