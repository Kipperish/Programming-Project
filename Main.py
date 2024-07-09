import pygame
from Vehicles import Car, SportsCar, Truck, colourList
from Buttons import Button, LevelButton
from Utilities import scaleImage, LinkedList

# Colour RGB Values
white = (255, 255, 255)
orange = (255, 169, 10)
lightOrange = (220, 185, 120)
grey = (153, 153, 153)
darkGrey = (120, 120, 120)
black = (38, 38, 38)

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
