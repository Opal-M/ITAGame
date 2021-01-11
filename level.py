from environment_sprite import Environment_Sprite, sprite_list, generate_collision_list
import level_sprites
import pygame
import setup


class Level:
  def __init__(self, level_list):
    # self.player_health = player_health
    self.background = pygame.image.load("Images/background.jpg")
    # Sprite("Grass.jpg", setup.SCREEN_HEIGHT/2, setup.SCREEN_WIDTH/0.5)
    # self.platforms_list = platforms_list
    self.collision_list = level_list

  def update_platforms_list(self, update):
    global platforms_list
    platforms_list.append(update)

  def draw_background(self):
    setup.screen.blit(self.background, (0, 0))
    for obj in sprite_list:
      obj.draw()

  def logic(self):
    pass
    #if Player.x > dlkhg
    #if player is hit by enemy:
      #health -= 1
    #if ending is_touching player:
      #level count += 1


  def game_loop(self):
    old_level = setup.level
    if setup.level != old_level:
        level_sprites.draw_levelx(setup.level)
        print("Trench")
        generate_collision_list()
        old_level = setup.level
    self.draw_background()
    self.logic()

    
class Level1:
  def __init__(self,variable):
    self.self = self
class Level2:
  def __init__(self,variable):
    self.self = self
