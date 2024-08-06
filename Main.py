import pygame
from Vehicles import Car, SportsCar, Truck, colourList
from Buttons import *
from TextBox import *
from Utilities import scaleImage, LinkedList
from Colours import *
from LevelParts import *

# Initialises a screen
backgroundColour = white
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Epic Driving Game')

# Sets a frame tick counter so the speed isn't dependant of processor speed
fps = 60
clock = pygame.time.Clock()
pygame.font.init()

# Initialises a car
car = Car()

# Initialises a Truck
truck = Truck()

# Initialises a sports car
sportsCar = SportsCar()

# Creates a looped linked list for the player to rotate vehicles when changing
vehicleList = LinkedList()
vehicleList.insertAtFront(sportsCar)
vehicleList.insertAtFront(truck)
vehicleList.insertAtFront(car)
vehicleList.loop()

# Initialises the player
player = vehicleList.head.data

# Keeps track of the current game state
gameRunning = True
mainMenuRunning = True
settingsRunning = False
levelMenuRunning = False
level1Running = False
level2Running = False
level3Running = False
level4Running = False
level5Running = False
level6Running = False

# Main Game Loop
while gameRunning:
    # Initialises the loop for the Main Menu
    while mainMenuRunning:
        clock.tick(fps)
        screen.fill(backgroundColour)
        playButton.update(screen)
        settingsButton.update(screen)
        quitButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainMenuRunning = False
                gameRunning = False
            if settingsButton.isClicked(event):
                mainMenuRunning = False
                settingsRunning = True
            if quitButton.isClicked(event):
                mainMenuRunning = False
                gameRunning = False
            if playButton.isClicked(event):
                mainMenuRunning = False
                levelMenuRunning = True
        pygame.display.flip()

    # Creates Loop for settings screen
    while settingsRunning:
        clock.tick(fps)
        screen.fill(backgroundColour)
        aboutTextBox.draw(screen)
        homeButton.update(screen)
        changeColourButton.update(screen)
        changeVehicleButton.update(screen)
        player.rect.center = (700, 590)
        screen.blit(player.originalImage, player.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settingsRunning = False
                gameRunning = False
            if homeButton.isClicked(event):
                settingsRunning = False
                mainMenuRunning = True
            if changeColourButton.isClicked(event):
                colourList.rotate()
                player.originalImage = scaleImage(pygame.image.load(
                    player.sprites[colourList.head.data]).convert_alpha(), 1)
            if changeVehicleButton.isClicked(event):
                vehicleList.rotate()
                player = vehicleList.head.data
                player.originalImage = scaleImage(pygame.image.load(
                    player.sprites[colourList.head.data]).convert_alpha(), 1)
        pygame.display.flip()

    # Creates loop for level select screen
    while levelMenuRunning:
        clock.tick(fps)
        screen.fill(backgroundColour)
        homeButton.update(screen)
        level1Button.update(screen)
        level2Button.update(screen)
        level3Button.update(screen)
        level4Button.update(screen)
        level5Button.update(screen)
        level6Button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                levelMenuRunning = False
                gameRunning = False

            if homeButton.isClicked(event):
                levelMenuRunning = False
                mainMenuRunning = True

            if level1Button.isClicked(event):
                levelMenuRunning = False
                level1Running = True

            if level2Button.isClicked(event):
                levelMenuRunning = False
                level2Running = True

            if level3Button.isClicked(event):
                levelMenuRunning = False
                level3Running = True

            if level4Button.isClicked(event):
                levelMenuRunning = False
                level4Running = True

            if level5Button.isClicked(event):
                levelMenuRunning = False
                level5Running = True

            if level6Button.isClicked(event):
                levelMenuRunning = False
                level6Running = True

        pygame.display.flip()

    while level1Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)
        straightRoad.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level1Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level1Running = False
                levelMenuRunning = True
        pygame.display.flip()#
    
    while level2Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level2Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level2Running = False
                levelMenuRunning = True
        pygame.display.flip()
    
    while level3Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level3Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level3Running = False
                levelMenuRunning = True
        pygame.display.flip()
    
    while level4Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level4Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level4Running = False
                levelMenuRunning = True
        pygame.display.flip()
    
    while level5Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level5Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level5Running = False
                levelMenuRunning = True
        pygame.display.flip()
    
    while level6Running:
        clock.tick(fps)
        screen.fill(green)
        homeButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level6Running = False
                gameRunning = False
            if homeButton.isClicked(event):
                level6Running = False
                levelMenuRunning = True
        pygame.display.flip()
