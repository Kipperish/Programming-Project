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


# Colour RGB Values
white = (255, 255, 255)
orange = (255, 169, 10)
lightOrange = (220, 185, 120)
grey = (153, 153, 153)
darkGrey = (120, 120, 120)
black = (38, 38, 38)

pygame.font.init()

# Creates the different Buttons used in the program
playButton = Button("Play", (540-100, 360), 200, 75, lightOrange, orange)

settingsButton = Button("Settings", (440, 450), 200, 75, grey, darkGrey)

homeButton = Button("Home", (20, 10), 90, 50, grey, darkGrey)

quitButton = Button("Quit", (20, 10), 90, 50, grey, darkGrey)

changeColourButton = Button(
    "Change Colour", (440, 600), 200, 75, grey, darkGrey)

changeVehicleButton = Button(
    "Change Vehicle", (440, 500), 200, 75, grey, darkGrey)

level1Button = LevelButton("level 1", (75, 100),
                           275, 100, lightOrange, orange, None)

level2Button = LevelButton("level 2", (400, 100),
                           275, 100, lightOrange, orange, None)

level3Button = LevelButton("level 3", (725, 100),
                           275, 100, lightOrange, orange, None)

level4Button = LevelButton("level 4", (75, 300),
                           275, 100, lightOrange, orange, None)

level5Button = LevelButton("level 5", (400, 300),
                           275, 100, lightOrange, orange, None)

level6Button = LevelButton("level 6", (725, 300),
                           275, 100, lightOrange, orange, None)
