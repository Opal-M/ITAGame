from sprite import Sprite
import pygame
import setup


class Level:
  def __init__(self, platforms_list):
    # self.player_health = player_health
    self.background = pygame.image.load("milkyway.png")
    Sprite("Grass.jpg",setup.SCREEN_HEIGHT/2,setup.SCREEN_WIDTH/2)
    self.platforms_list = platforms_list

  def update_platforms_list(self, update):
    global platforms_list
    platforms_list.append(update)

  def draw_background(self):
    setup.screen.blit(self.background, (0, 0))
    #for obj in Sprite:
      #obj.draw()
    pygame.display.flip()

  def logic(self):
    while setup.level == 1:
      pass
    #if player is hit by enemy:
      #health -= 1
    #if ending is_touching player:
      #level count += 1
  def game_loop(self):
    self.draw_background()
    self.logic()
  