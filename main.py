#imports
import pygame
import math
import time
from environment_sprite import Player, update_screen, generate_collision_list, sprite_list, collision_list
import Media
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
        if Media.p.Media.p.y_vel > -10:
            Media.p.Media.p.y_vel -= 1
    elif active_keys[pygame.K_s]:
        if Media.p.Media.p.y_vel < 10:
            Media.p.y_vel += 1
    elif Media.p.y_vel != 0:
        Media.p.y_vel -= (Media.p.y_vel ** 0) * Media.p.y_vel * 0.5
    Media.p.y += Media.p.y_vel


		
# draws all sprites and misc. images
def draw_images():
    Media.p.screen.blit(background, (0, 0))
    # ground_plane.draw()
    Media.p.draw()
    pygame.display.flip()

# points the sprite in the direction of the cursor
def point_cursor():
    relative_angle = math.atan2(pygame.mouse.get_pos()[1] - Media.p.y, pygame.mouse.get_pos()[0] - Media.p.x)*(180/math.pi)+90
    Media.p.rotate(-relative_angle)


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

# update_screen(Media.p.screen, Media.p.SCREEN_WIDTH, Media.p.SCREEN_HEIGHT)

'''
**
*                MEDIA
***'''
background = pygame.image.load("Images/background.jpg")
p = Player("Images/Animations/Player_Idle/tile000.png", 35, 0)
# ruby = Sprite("CptnRubyGem.png", 0, 0, False)
# ground_plane = Sprite("Grass.jpg", setuMedia.p.SCREEN_WIDTH/2, setuMedia.p.SCREEN_HEIGHT * 1.2, True)
# update_collision_list(collision_sprites)
#  for sprites in collision_sprites:
#     if type(sprites) == Sprite:
#         sprites.has_hitbox = True


'''SETUP CODE'''
game_over = False
not_level1_over = False

# block1 = Sprite("Images/Sprites/platform.png", setuMedia.p.SCREEN_HEIGHT/2, setuMedia.p.SCREEN_WIDTH/1.5, True)
# level_one_platforms = [block1]
#instances
title_screen_class = level.Level(level_sprites.title_screen)
level1 = level.Level(level_sprites.level_one)
level2 = level.Level(level_sprites.level_two)
level3 = level.Level(level_sprites.level_three)
level4 = level.Level(level_sprites.level_four)
end_screen = level.Level(level_sprites.end_screen)



#Creating setup lists for game loop
level_sprites.draw_levelx(setup.level)
generate_collision_list()
old_level = setup.level

#Main game loop
while not game_over:
    level_sprites.strawberry.fruit_game_loop(Player)
    #Cnditional to draw new background when level changes
    if setup.level != old_level:
        level_sprites.draw_levelx(setup.level)
        collision_list.clear()
        if setup.level == 0:
            
            level_list = level_sprites.title_screen
        elif setup.level == 1:
     
            level_list = level_sprites.level_one

            # multiply by 40 + 20
            level_sprites.strawberry.x = (18 * 40) + 20
            level_sprites.strawberry.y = (1 * 40) + 20
            # multiply by 60
            level_sprites.strawberry.x = 17 * 60

        elif setup.level == 2:
           
            level_list = level_sprites.level_two
    
        elif setup.level == 3:
  
            level_list = level_sprites.level_three
        elif setup.level == 4:

            level_list = level_sprites.level_four

        elif setup.level == 5:
            level_list = level_sprites.end_screen


        level_sprites.strawberry.fruit_game_loop(Player)

        generate_collision_list(level_list)
        old_level = setup.level
    if setup.level == 0:
        title_screen_class.game_loop()
    elif setup.level == 1:
        level_sprites.strawberry.fruit_game_loop(Player)
        level_sprites.strawberry.x = (18 * 40) + 20
        level_sprites.strawberry.y = (1 * 40) + 20
        level1.game_loop()
        for base_image in level_sprites.title_screen:
            base_image.is_visible = False
            base_image.has_collision = False
    elif setup.level == 2:
        #level_sprites.strawberry.fruit_game_loop(Player)
        level_sprites.strawberry.x = (25 * 40) + 20
        level_sprites.strawberry.y = (11 * 40) + 20
        level2.game_loop()
        level_sprites.strawberry.fruit_game_loop(Player)
        for base_image in level_sprites.level_one:
            if base_image != level_sprites.strawberry:
                base_image.is_visible = False
                base_image.has_collision = False
    elif setup.level == 3:
        level_sprites.strawberry.fruit_game_loop(Player)
        level_sprites.strawberry.x = (5 * 40) + 20
        level_sprites.strawberry.y = (1 * 40) + 20
        level3.game_loop()
        for base_image in level_sprites.level_two:
            if base_image != level_sprites.strawberry:
                base_image.is_visible = False
                base_image.has_collision = False
    elif setup.level == 4:
        level_sprites.strawberry.fruit_game_loop(Player)
        level_sprites.strawberry.x = (30.5 * 40) + 20
        level_sprites.strawberry.y = (13 * 40) + 20
        level4.game_loop()
        for base_image in level_sprites.level_three:
            if base_image != level_sprites.strawberry:
                base_image.is_visible = False
                base_image.has_collision = False
    elif setup.level == 5:
        level_sprites.strawberry.hide()
        end_screen.game_loop()
        for base_image in level_sprites.level_four:
            if base_image != level_sprites.strawberry:
                base_image.is_visible = False
                base_image.has_collision = False

    Media.p.move_player()
    Media.p.draw()
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