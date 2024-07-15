import pygame
from Colours import *

pygame.font.init()

# Text Box class for placing a box of text on the screen


class TextBox:
    def __init__(self, text, position, width, height, colour):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.font = pygame.font.SysFont('Comic Sans MS', 15)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        textSurface = self.font.render(self.text, True, (38, 38, 38))
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)


aboutTextBox = TextBox(
    "This game is about learning to drive. Each level will judge you and give a star rating. You can customise vehicle here", (540-250, 50), 500, 100, white)
