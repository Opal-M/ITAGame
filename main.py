#imports
import pygame
import math
import time
from environment_sprite import Environment_Sprite, Player, update_screen, generate_collision_list
import level
import setup
import level_sprites
import object_sprite
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
        if setup.p.setup.p.y_vel > -10:
            setup.p.setup.p.y_vel -= 1
    elif active_keys[pygame.K_s]:
        if setup.p.setup.p.y_vel < 10:
            setup.p.y_vel += 1
    elif setup.p.y_vel != 0:
        setup.p.y_vel -= (setup.p.y_vel ** 0) * setup.p.y_vel * 0.5
    setup.p.y += setup.p.y_vel


		
# draws all sprites and misc. images
def draw_images():
    setup.p.screen.blit(background, (0, 0))
    # ground_plane.draw()
    setup.p.draw()
    pygame.display.flip()

# points the sprite in the direction of the cursor
def point_cursor():
    relative_angle = math.atan2(pygame.mouse.get_pos()[1] - setup.p.y, pygame.mouse.get_pos()[0] - setup.p.x)*(180/math.pi)+90
    setup.p.rotate(-relative_angle)


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

update_screen(setup.p.screen, setup.p.SCREEN_WIDTH, setup.p.SCREEN_HEIGHT)

'''
**
*                MEDIA
***'''
background = pygame.image.load("Images/background.jpg")
p = Player("Images/Animations/Player_Idle/tile000.png", 35, 0)
# ruby = Sprite("CptnRubyGem.png", 0, 0, False)
# ground_plane = Sprite("Grass.jpg", setusetup.p.SCREEN_WIDTH/2, setusetup.p.SCREEN_HEIGHT * 1.2, True)
# update_collision_list(collision_sprites)
#  for sprites in collision_sprites:
#     if type(sprites) == Sprite:
#         sprites.has_hitbox = True


'''SETUP CODE'''
game_over = False
not_level1_over = False

# block1 = Sprite("Images/Sprites/platform.png", setusetup.p.SCREEN_HEIGHT/2, setusetup.p.SCREEN_WIDTH/1.5, True)
# level_one_platforms = [block1]

level1 = level.Level(level_sprites.level_one)
level2 = level.Level2(level_sprites.level_two)
object_sprite = object_sprite.Object_Sprite("Fruit_Strawberry/tile004.png")
level_sprites.draw_level(1)
generate_collision_list()
while not game_over:
    object_sprite.fruit_game_loop(Player)
    old_level = setup.p.level
    if setup.p.level != old_level:
        level_sprites.draw_level(setup.p.level)
        generate_collision_list()
        old_level = setup.p.level +1
    if setup.p.level == 1:
        level1.game_loop()
    if setup.p.level == 2:
        level2.game_loop()

  # level2()
  # draw_images()
    setup.p.move_player()
    setup.p.draw()
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