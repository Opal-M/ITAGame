#imports
import pygame
import math
import time
from environment_sprite import Environment_Sprite, Player, update_screen, generate_collision_list
import level
import setup
import level_sprites
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


		
# draws all sprites and misc. images
def draw_images():
    setup.screen.blit(background, (0, 0))
    # ground_plane.draw()
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
pygame.display.set_icon(pygame.image.load("Images/Animations/Player_Idle/tile000.png"))
pygame.display.set_caption("Game")
pygame.key.set_repeat(10)

update_screen(setup.screen, setup.SCREEN_WIDTH, setup.SCREEN_HEIGHT)

'''
**
*                MEDIA
***'''
background = pygame.image.load("Images/background.jpg")
p = Player("Images/Animations/Player_Idle/tile000.png", 35, 0)
# ruby = Sprite("CptnRubyGem.png", 0, 0, False)
# ground_plane = Sprite("Grass.jpg", setup.SCREEN_WIDTH/2, setup.SCREEN_HEIGHT * 1.2, True)
# update_collision_list(collision_sprites)
#  for sprites in collision_sprites:
#     if type(sprites) == Sprite:
#         sprites.has_hitbox = True


'''SETUP CODE'''
game_over = False
not_level1_over = False

# block1 = Sprite("Images/Sprites/platform.png", setup.SCREEN_HEIGHT/2, setup.SCREEN_WIDTH/1.5, True)
# level_one_platforms = [block1]

title_screen = level.Level(level_sprites.title_screen)
level1 = level.Level(level_sprites.level_one)
level2 = level.Level(level_sprites.level2)
level_sprites.draw_level0(0)
generate_collision_list()
while not game_over:
    old_level = setup.level
    if setup.level != old_level:
        level_sprites.draw_level(setup.level)
        generate_collision_list()
        old_level = setup.level
    setup.level = 2
    if setup.level == 0:
        title_screen.game_loop()
    if setup.level == 1:
        level1.game_loop()
    if setup.level == 2:
        level2.game_loop()
        
  # level2()
  # draw_images()
    p.move_player()
    p.draw()
    # move_ruby()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print("Mouse clicked at", mouse_pos)
    clock.tick(60)

pygame.quit()
print("Game Ended")