#imports
import pygame
import math
import time
from sprite import Sprite, Player, update_screen
from sprite import update_collision_list
import level1
import setup
# from sprite import Player
#screen settings
clock = pygame.time.Clock()

'''
*
* METHODS
*
'''

def fly_hero():
    active_keys = pygame.key.get_pressed()
    if active_keys[pygame.K_w]:
        if p.y_vel > -10:
            p.y_vel -= 1
    elif active_keys[pygame.K_s]:
        if p.y_vel < 10:
            p.y_vel += 1
    elif p.y_vel != 0:
        p.y_vel -= (p.y_vel ** 0) * p.y_vel * 0.5
    p.y += p.y_vel

# a temporary function to move the groundplane every frame (call every frame)
def move_groundplane(x_change):
    ground_plane.x -= x_change
		
# draws all sprites and misc. images
def draw_images():
    setup.screen.blit(background, (0, 0))
    ground_plane.draw()
    p.draw()
    pygame.display.flip()

# points the sprite in the direction of the cursor
def point_cursor():
    relative_angle = math.atan2(pygame.mouse.get_pos()[1] - p.y, pygame.mouse.get_pos()[0] - p.x)*(180/math.pi)+90
    p.rotate(-relative_angle)


'''
*
*          INITIALIZTION
**'''
pygame.init()
pygame.display.init()
#sets favicon for the website i think
pygame.display.set_icon(pygame.image.load("CptnRubyGem.png"))
pygame.display.set_caption("Game")
pygame.key.set_repeat(10)

update_screen(setup.screen, setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT)

'''
**
*                MEDIA
***'''
background = pygame.image.load("milkyway.png")
p = Player("Images/Animations/Player_Idle/tile000.png", setup.SCREEN_WIDTH/2, setup.SCREEN_HEIGHT/2)
# ruby = Sprite("CptnRubyGem.png", 0, 0, False)
ground_plane = Sprite("Grass.jpg", setup.SCREEN_WIDTH/2, setup.SCREEN_HEIGHT * 1.2, True)
collision_sprites = [ground_plane]
update_collision_list(collision_sprites)
#  for sprites in collision_sprites:
#     if type(sprites) == Sprite:
#         sprites.has_hitbox = True

'''SETUP CODE'''
game_over = False
not_level1_over = False

block1 = Sprite("Images/Sprites/platform.png",setup.SCREEN_HEIGHT/2,setup.SCREEN_WIDTH/2)
level_one_platforms = [block1]

level1 = level1.Level(level_one_platforms)

while not game_over:
  if setup.level == 1:
    level1.game_loop()
  # level2()
  # draw_images()
  p.move_player()
    # move_ruby()
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          game_over = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
          mouse_pos = pygame.mouse.get_pos()
          print("Mouse clicked at", mouse_pos)
  clock.tick(60)

pygame.quit()
print("Game Ended")