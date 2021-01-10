#screen settings
import pygame
from environment_sprite import Player
SCREEN_WIDTH = int(1280)
SCREEN_HEIGHT = int(640)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
level = 1
p = Player("Images/Animations/Player_Idle/tile000.png", 35, 0)
