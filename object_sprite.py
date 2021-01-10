#imports
import pygame
import os
import time
import statistics
from setup import p
import math
from environment_sprite import sprite_list, collision_list, Player
class Object_Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, collision=False):
        pygame.sprite.Sprite.__init__(self)
        scale_multiple = 2.5
        self.x = x * 16 * scale_multiple + (8 * scale_multiple)
        self.y = y * 16 * scale_multiple + (8 * scale_multiple)
        self.x_vel = 0
        self.y_vel = 0
        filename = "Images/Animations/" + image
        print(filename)
        self.base_image = pygame.image.load(filename)
        base_image_rect = self.base_image.get_rect()
        self.base_image = pygame.transform.scale(
            self.base_image,
            (math.floor(base_image_rect.width * scale_multiple), math.floor(base_image_rect.height * scale_multiple)))
        self.image = self.base_image
        self.is_visible = True
        self.has_collision = collision
        sprite_list.append(self)


        # def scale_relative(self):
        # scales the sprite relative to the screen
        # SCALE_MODIFIER = 500
        # screen_avg = statistics.mean([setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT]) // SCALE_MODIFIER
        # self.base_image = pygame.transform.scale(self.base_image, (
        # self.base_image.get_rect().width * screen_avg, self.base_image.get_rect().height * screen_avg))

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.base_image, angle)

    def draw(self):
        if self.is_visible:
            # pygame.draw.rect(screen, (255, 0, 0), self.rect)
            dimensions = self.image.get_rect()
            setup.screen.blit(self.image, (self.x - dimensions[2] / 2, self.y - dimensions[3] / 2))

    def is_touching(self, other_sprite):
        if self.is_visible and other_sprite.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x - (self.rect.width / 2)
            self.rect.y = self.y - (self.rect.height / 2)
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x - (other_sprite.rect.width / 2)
            other_sprite.rect.y = other_sprite.y - (other_sprite.rect.height / 2)
            return pygame.sprite.collide_rect(self, other_sprite)
        else:
            return False


    def hide(self):
        self.is_visible = False

    def show(self):
        self.is_visible = True

    #code to check if player has picked up fruit    
    def fruit_collide (self, player):
        print ("hello")
        if p.will_collide_sprite(self):
            print("hello")
            setup.level = setup.level +1
            self.hide 
            collision_list.remove(self)
    def fruit_game_loop (self,player):
        self.fruit_collide(player)