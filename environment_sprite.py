#imports
import pygame
import os
import time
import statistics
from setup import SCREEN_HEIGHT, SCREEN_HEIGHT
import math
import setup

# Brings the collision_list from main.py to sprite.py
# It might be possible to assign collision_list here then import it into main.py
# but this works for now
collision_list = []
sprite_list = []
def generate_collision_list(current_level=sprite_list):
    for sprite in current_level:
        if sprite.has_collision:
            collision_list.append(sprite)
# def update_collision_list(update):
#     global collision_list
#     collision_list.append(update)

# Brings the screen variable as well as the SCREEN_WIDTH and SCREEN_HEIGHT
# constansts from main.py to sprite.py
def update_screen(input_screen, input_SCREEN_WIDTH, input_SCREEN_HEIGHT):
    global screen,SCREEN_WIDTH,SCREEN_HEIGHT
    screen = input_screen
    SCREEN_WIDTH = input_SCREEN_WIDTH
    SCREEN_HEIGHT = input_SCREEN_HEIGHT


# creating player class- movement, hitbox, animation 
class Player(pygame.sprite.Sprite):
    def __init__(self, filename, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        scale_multiple = 2.5
        self.x = x * 16 * scale_multiple + (8 * scale_multiple)
        self.y = y * 16 * scale_multiple + (8 * scale_multiple)
        self.jump_timer = 0
        self.x_vel = 0
        self.y_vel = 0
        self.x_speed_limit = 20
        self.base_image = pygame.image.load(filename)
        self.image = pygame.image.load(filename)
        self.is_visible = True
        self.has_hitbox = False
        self.JUMP_LIMIT = 2
        self.jump_check = False
        self.jump_lock = False
        self.jump_lock2 = False
        self.jump_strike = 0
        self.frame_number = 0
        self.animation_time = time.time()
        self.direction = "right"
        self.size = 1
    
    # Moves the hero
    # In charge of hero gravity, jumping, moving left and right.
    # Calls the collision functions
    def move_player(self):
        active_keys = pygame.key.get_pressed()
        if active_keys[pygame.K_w] and self.jump_timer <= self.JUMP_LIMIT:
            self.jump_check = True
            if not self.jump_lock:
                if self.jump_strike == 1:
                    self.y_vel = 0
                self.y_vel -= self.JUMP_LIMIT / ((abs(self.y_vel) + 0.01) * 25)
                self.jump_timer += 0.3
        if not (active_keys[pygame.K_w] and self.jump_timer <= self.JUMP_LIMIT) or self.jump_lock:
            self.y_vel += 1
        if not active_keys[pygame.K_w] and self.jump_check:
            if self.jump_strike == 0:
                self.jump_timer = 0
                self.jump_strike = 1
                self.jump_check = False
            elif self.jump_strike == 1:
                self.jump_lock = True
        if (active_keys[pygame.K_a] or active_keys[pygame.K_d]) and - self.x_speed_limit < self.x_vel < self.x_speed_limit:
            self.rect = self.base_image.get_rect()
            move_left_requirement = self.x + self.x_vel > 0 + (self.rect.width/2)
            move_right_requiremnet = self.x + self.x_vel + (self.rect.width/2) < setup.SCREEN_WIDTH
            if not move_left_requirement:
                self.x_vel = 0
                self.x = self.rect.width/2 - 5
            if not move_right_requiremnet:
                self.x_vel = 0
                self.x = setup.SCREEN_WIDTH - (self.rect.width/2) + 5
            if active_keys[pygame.K_a] and move_left_requirement:
                self.x_vel -= 3
            if active_keys[pygame.K_d] and move_right_requiremnet:
                self.x_vel += 3

        elif self.x_vel != 0:
            self.x_vel += - self.x_vel / 2

            if -0.1 < self.x_vel < 0.1:
                self.x_vel = 0


        if 0 < self.x_vel:
            self.direction = "right"
        if 0 > self.x_vel:
            self.direction = "left"
        self.hori_collision()
        self.vert_collision()

    # Contextually runs animations (ex: if player is running player run animation)
    def player_animation(self):
        active_keys = pygame.key.get_pressed()
        if (active_keys[pygame.K_w] and self.jump_strike == 1) or (self.jump_strike == 1 and self.jump_lock):
            self.play_animation("Player_Double_Jump", 0.08)
        elif self.y_vel > 0:
            self.play_animation("Player_Fall")
        elif self.x_vel == 0:
            self.play_animation("Player_Idle")
        elif self.x_vel != 0:
            self.play_animation("Player_Run")


    # Rotates the sprite to the angle inputed as an argument
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.base_image, angle)

    def draw(self):
        self.player_animation()
        if self.is_visible:
            # pygame.draw.rect(screen, (255, 0, 0), self.rect)
            if self.direction == "left":
                self.image = pygame.transform.flip(self.base_image, True, False)
            if self.direction == "right":
                self.image = self.base_image
            dimensions = self.image.get_rect()
            setup.screen.blit(self.image, (self.x - dimensions[2]/2, self.y - dimensions[3]/2))
        
    def is_touching(self, other_sprite):
        if self.is_visible and other_sprite.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x - (self.rect.width / 2)
            self.rect.y = self.y - (self.rect.height / 2)
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x - (other_sprite.rect.width / 2)
            other_sprite.rect.y = other_sprite.y - (other_sprite.rect.height / 2)
            return pygame.sprite.collide_rect(self, other_sprite)
        else: return False

# ////////COLLISION///////////
# ///////////////////////////
# code for when sprites touch each other

    def vert_collision(self):
        if not self.will_collide():
            self.y += self.y_vel
        elif self.collide_with().y > self.y:
            self.y = self.collide_with().rect.y - self.rect.height / 2
            self.y_vel = 0
            self.jump_timer = 0
            self.jump_check = False
            self.jump_lock = False
            self.jump_strike = 0
        elif self.collide_with().y - self.collide_with().rect.height < self.y:
            self.y = self.collide_with().rect.y + self.collide_with().rect.height + self.rect.height / 2
            self.y_vel = 0

    
    def collide_with(self):
        # checks what is being colliding with self
        result = None
        sprites_dict = {}
        for sprite in collision_list:
            if self.will_collide_sprite(sprite):
                sprites_dict[sprite.rect.y] = sprite
                result = True
        if result:
            return sprites_dict[max(sprites_dict)]

    # checks if self will collide with any of the sprites on collision_list
    # next frame, returns boolean
    def will_collide(self):
        # tests if self will collide with any sprites on the collision list
        result = None
        for sprite in collision_list:
            sprite_type = type(sprite)
            if self.will_collide_sprite(sprite):
                result = True

        if result:
            return True
        else:
            return False

    # checks if two sprites will collide next frame, returns boolean
    def will_collide_sprite(self, other_sprite):
        # tests if two sprites will collide
        if self.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x - (self.rect.width / 2)
            self.rect.y = self.y - (self.rect.height / 2) + self.y_vel
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x - (other_sprite.rect.width / 2)
            other_sprite.rect.y = other_sprite.y - (other_sprite.rect.height / 2)
            return pygame.sprite.collide_rect(self, other_sprite)
        else:
            return False

    def hori_collision(self):
        if not self.will_collide_x():
            self.x += self.x_vel
        elif self.x < self.collide_with_x().x:
            self.x = self.collide_with_x().rect.x - self.rect.height / 2
            self.x_vel = 0
        elif self.collide_with_x().x - self.collide_with_x().rect.width < self.x:
            self.x = self.collide_with_x().rect.x + self.collide_with_x().rect.width + self.rect.width / 2
            self.x_vel = 0
            # if not
            #     self.y_vel = 0

    def collide_with_x(self):
        # checks what is being colliding with self
        result = None
        sprites_dict = {}
        for sprite in collision_list:
            if self.will_collide_sprite_x(sprite):
                sprites_dict[sprite.rect.x] = sprite
                result = True
        if result:
            return sprites_dict[max(sprites_dict)]

    def will_collide_x(self):
        # tests if self will collide with any sprites on the collision list
        result = None
        for sprite in collision_list:
            if self.will_collide_sprite_x(sprite):
                result = True
        if result:
            return True
        else:
            return False

    def will_collide_sprite_x(self, other_sprite):
        # tests if two sprites will collide
        if self.is_visible:
            self.rect = self.image.get_rect()
            self.rect.x = self.x - (self.rect.width / 2) + self.x_vel
            self.rect.y = self.y - (self.rect.height / 2)
            other_sprite.rect = other_sprite.image.get_rect()
            other_sprite.rect.x = other_sprite.x - (other_sprite.rect.width / 2)
            other_sprite.rect.y = other_sprite.y - (other_sprite.rect.height / 2)
            return pygame.sprite.collide_rect(self, other_sprite)
        else:
            return False

# /////////////////////////
        
    def hide(self):
        self.is_visible = False
    
    def show(self):
        self.is_visible = True
    
    # scales the player relative to the screen
    # not good, needs a remake
    def scale_relative(self):
        SCALE_MODIFIER = 500
        screen_avg = statistics.mean([setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT]) // SCALE_MODIFIER
        self.base_image = pygame.transform.scale(self.base_image, (self.base_image.get_rect().width * screen_avg, self.base_image.get_rect().height * screen_avg))
				
		# arguments: the file where the animation frames are located
    # optional speed argument (defaults 0.06)	
    def play_animation(self, animation_file, speed=0.06):
        #sets the animation directory to the path to the folder listed
        # as an argument including that folder
        animation_dir = os.path.dirname(__file__) + "/Images/Animations/"+animation_file
        # creates a list of all files in the animation folder
        animation_list = os.listdir(animation_dir)
        # this if statement acts as a for loop but works with the video game
        # frame system
        if self.frame_number < len(animation_list):
            # this if limits the speed of the animation
            if time.time() >= self.animation_time + speed:
                self.base_image = pygame.image.load(animation_dir + "/" + animation_list[self.frame_number])
                base_image_rect = self.base_image.get_rect()
                self.base_image = pygame.transform.scale(
                    self.base_image,
                    (math.floor(base_image_rect.width * 2.5),
                     math.floor(base_image_rect.height * 2.5))
                )
                self.animation_time = time.time()
                self.frame_number += 1
        else:
            self.frame_number = 0
        # print(animation_list[self.frame_number])

# creates the sprite class, used for general sprites
class Environment_Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, collision=False, rescale = True):
        pygame.sprite.Sprite.__init__(self)
        scale_multiple = 2.5
        self.x = x * 16 * scale_multiple + (8 * scale_multiple)
        self.y = y * 16 * scale_multiple + (8 * scale_multiple)
        self.x_vel = 0
        self.y_vel = 0
        filename = "Images/Environmental_Sprites/" + image
        self.base_image = pygame.image.load(filename)
        base_image_rect = self.base_image.get_rect()
        if rescale:
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
