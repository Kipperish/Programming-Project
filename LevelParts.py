import pygame
from Colours import *

#Road class to implement road features into levels
class Road():
    def __init__(self, width, length, centrePos):
        self.width = width
        self.length = length
        self.centrePos = centrePos
        self.rect = pygame.Rect(0, 0, self.length, self.width)
        self.rect.center = self.centrePos
        self.colour = grey

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

straightRoad = Road(150, 1080, (540, 360))
