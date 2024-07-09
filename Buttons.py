import pygame

# Button Class Which Handles Player Clicks


class Button:
    def __init__(self, text, position, width, height, colour, hoverColour):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.originalColour = colour
        self.colour = colour
        self.hoverColour = hoverColour
        self.rect = pygame.Rect(position[0], position[1], width, height)
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        textSurface = self.font.render(self.text, True, (255, 255, 255))
        textRect = textSurface.get_rect(center=self.rect.center)
        screen.blit(textSurface, textRect)

    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mousePos):
                return True
            else:
                return False
        else:
            return False

    def isHovered(self):
        mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            self.colour = self.hoverColour
        else:
            self.colour = self.originalColour

    def update(self, screen):
        self.draw(screen)
        self.isHovered()


class LevelButton(Button):
    def __init__(self, text, position, width, height, colour, hoverColour, level):
        Button.__init__(self, text, position, width,
                        height, colour, hoverColour)
        self.level = level
