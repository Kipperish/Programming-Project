import pygame
from Utilities import *

class Star():
    def __init__(self, position):
        self.image = scaleImage(pygame.image.load("Images\Star Sprites\starBg.png").convert_alpha(), 0.2)
        self.rect = self.image.get_rect()
        self.rect.center = position