# Play a sound by pushing a button.  See 'playing_sound.py'
# and 'hello_world_with_button.py' for a line-by-line 
# description of what's going on.

# Can you think of any ways to make the script simpler
# or more organized? Can you think of any way to make it
# work without having to define a function?

import pygame
from gpiozero import Button

pygame.init()
cool_sound = pygame.mixer.Sound('/home/pi/class/a_random_sound.wav')

def play_cool_sound():
    cool_sound.play()

btn = Button(17)
btn.when_pressed = play_cool_sound

while True:
    pass
