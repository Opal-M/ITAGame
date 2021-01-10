from environment_sprite import Environment_Sprite, sprite_list
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
    if setup.level == 0:
      self.draw_background()
      self.logic()

class Level1:
  from level_sprites import draw_strip
  def __init__(self,variable):
    self.self = self
    self.variable = variable
  def draw_stuff(self):
    draw_strip(0,13,32,"Grass_Green_Center_Center.png")
    draw_strip(0,12,32,"Grass_Green_Top_Center.png")
    draw_strip(10,9,10,"Brick_Center_Center.png")
    draw_strip(0,14,32,"Grass_Green_Center_Center.png")
    draw_strip(0,15,32,"Grass_Green_Center_Center.png")