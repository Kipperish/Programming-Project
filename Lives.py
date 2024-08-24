import pygame
from Utilities import *

class Lives():
    def __init__(self):
        self.images = {3 : scaleImage(pygame.image.load("Images\\Lives Sprites\\threeLives.png").convert_alpha(), 0.9), 
                       2 : scaleImage(pygame.image.load("Images\\Lives Sprites\\twoLives.png").convert_alpha(), 0.9), 
                       1 : scaleImage(pygame.image.load("Images\\Lives Sprites\\oneLives.png").convert_alpha(), 0.9), 
                       0 : scaleImage(pygame.image.load("Images\\Lives Sprites\\zeroLives.png").convert_alpha(), 0.9)}
        self.currentImage = self.images[3]
        self.rect = self.currentImage.get_rect()
        self.rect.center = (900, 50)
