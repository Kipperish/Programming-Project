import pygame
from Vehicles import Car, SportsCar, Truck, colourList
from Buttons import *
from TextBox import *
from Utilities import scaleImage, LinkedList
from Colours import *

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
        pygame.display.flip()
