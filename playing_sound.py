# Play one of the sound files in the 'class' folder.

# We are using a library (a code tool) called 'pygame'
# to play the sound files:
import pygame

# Next, we need to initialize pygame, which is like turning it on:
pygame.init() 

# Now that it's initialized, we can create a Sound object and
# tell it which sound file we want to play (replace 
# '/home/pi/class/a_random_sound.wav' with the path to an actual
# sound file):
cool_sound = pygame.mixer.Sound('/home/pi/class/a_random_sound.wav')

# play the sound!
cool_sound.play()