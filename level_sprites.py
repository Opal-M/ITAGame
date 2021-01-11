import pygame
from environment_sprite import Environment_Sprite, generate_collision_list,sprite_list
from object_sprite import Object_Sprite
import Media

strawberry = Object_Sprite("Fruit_Strawberry/tile004.png", 27, 10)
title_screen = []
level_one = []
level_two = []

end_screen = []


level_three = []
level_four = []

# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Center_Center.png",number , 13 , True))
# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Top_Center.png", number, 12, True))

#ATTENTION FOR THE BRONZE SPRITES I MISSPELLED VERTICLE USE THE WORD 'veritical'

#def draw_stripx(x,y,length,image,blist=[]):
  #for number in range(0,length):
      #blist.append(Environment_Sprite(image, x+number, y, True))
def draw_capped_stripx(x,y,length,start,middle,end,blist):
  global title_screen, level_one, level_two,level_three,level_four
  blist.append(Environment_Sprite(start, x, y, True))
  for number in range(1,length):
    blist.append(Environment_Sprite(middle, x+number, y, True))
  blist.append(Environment_Sprite(end, x+(length-1), y, True))
def draw_levelx(number):
    if number == 0:

      #ground
      draw_capped_stripx(0,14,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png",title_screen)
      draw_capped_stripx(0,15,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",title_screen)
      draw_capped_stripx(0,14,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png",title_screen)
      draw_capped_stripx(0,16,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",title_screen)
      draw_capped_stripx(0,17,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",title_screen)
      #T
      draw_capped_stripx(2,2,3,"Bronze_Bar_Left.png","Bronze_Bar_Horizontal.png","Bronze_Bar_Right.png",title_screen)
      draw_capped_stripx(3,3,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png",title_screen)
      draw_capped_stripx(3,4,1,"Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png",title_screen)
      #I
      draw_capped_stripx(6,2,3,"Metal_Bar_Left.png","Metal_Bar_Horizontal.png","Metal_Bar_Right.png",title_screen)
      draw_capped_stripx(7,3,1,"Metal_Bar_Vertical.png","Metal_Bar_Vertical.png","Metal_Bar_Vertical.png",title_screen)
      draw_capped_stripx(6,4,3,"Metal_Bar_Left.png","Metal_Bar_Horizontal.png","Metal_Bar_Right.png",title_screen)
      #K
      draw_capped_stripx(10,2,1,"Copper_Bar_Top.png","Copper_Bar_Top.png","Copper_Bar_Top.png",title_screen)
      draw_capped_stripx(12,2,1,"Copper_Solid.png","Copper_Solid.png","Copper_Solid.png",title_screen)
      draw_capped_stripx(10,3,2,"Copper_Bar_Vertical.png","Copper_Bar_Right.png","Copper_Bar_Right.png",title_screen)
      draw_capped_stripx(10,4,1,"Copper_Bar_Bottom.png","Copper_Bar_Bottom.png","Copper_Bar_Bottom.png",title_screen)
      draw_capped_stripx(12,4,1,"Copper_Solid.png","Copper_Solid.png","Copper_Solid.png",title_screen)
      #I
      draw_capped_stripx(14,2,3,"Gold_Bar_Left.png","Gold_Semi_Solid_Horizontal.png","Gold_Bar_Right.png",title_screen)
      draw_capped_stripx(15,3,1,"Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png",title_screen)
      draw_capped_stripx(14,4,3,"Gold_Bar_Left.png","Gold_Semi_Solid_Horizontal.png","Gold_Bar_Right.png",title_screen)
      #-
      draw_capped_stripx(18,3,2,"Grass_Pink_Top_Left.png","Grass_Pink_Top_Right.png","Grass_Pink_Top_Right.png",title_screen)
      #O
      draw_capped_stripx(21,2,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png",title_screen)
      draw_capped_stripx(21,3,1,"Leaf_Slab_Left.png","Leaf_Slab_Left.png","Leaf_Slab_Left.png",title_screen)
      draw_capped_stripx(23,3,1,"Leaf_Slab_Right.png","Leaf_Slab_Right.png","Leaf_Slab_Right.png",title_screen)
      draw_capped_stripx(21,4,3,"Leaf_Corner_Bottom_Left.png","Leaf_Slab_Bottom.png","Leaf_Corner_Bottom_Right.png",title_screen)
      #H
      draw_capped_stripx(25,2,1,"Brick_Top_Left.png","Brick_Top_Left.png","Brick_Top_Left.png",title_screen)
      draw_capped_stripx(27,2,1,"Brick_Top_Right.png","Brick_Top_Right.png","Brick_Top_Right.png",title_screen)
      draw_capped_stripx(25,3,3,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png",title_screen)
      draw_capped_stripx(25,4,1,"Brick_Bottom_Left.png","Brick_Bottom_Left.png","Brick_Bottom_Left.png",title_screen)
      draw_capped_stripx(27,4,1,"Brick_Bottom_Right.png","Brick_Bottom_Right.png","Brick_Bottom_Right.png",title_screen)
      #!
      draw_capped_stripx(29,2,1,"Wood_Slab_Left.png","Wood_Slab_Left.png","Wood_Slab_Left.png",title_screen)
      draw_capped_stripx(29,3,1,"Wood_Slab_Left.png","Wood_Slab_Left.png","Wood_Slab_Left.png",title_screen)
      draw_capped_stripx(29,4,1,"Wood_Cube_Bottom_Left.png","Wood_Cube_Bottom_Left.png","Wood_Cube_Bottom_Left.png",title_screen)
      #_
      draw_capped_stripx(2,6,28,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",title_screen)
      title_screen.append(Environment_Sprite("Gold_Solid.png", 15, 13, True))
      title_screen.append(Environment_Sprite("WASD_To_Move.png", 4, 8.7, False, False))
      title_screen.append(Environment_Sprite("SPACE_To_Jump.png", 15, 8.7, False, False))
      title_screen.append(Environment_Sprite("TOUCH_Strawberry.png", 27, 8, False, False))
      #end zone
      #print (title_screen)
      generate_collision_list()
    if number == 1:
      #ground
      draw_capped_stripx(0,14,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png",level_one)

      draw_capped_stripx(0,15,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",level_one)
      draw_capped_stripx(0,14,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png",level_one)
      draw_capped_stripx(0,16,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",level_one)
      draw_capped_stripx(0,17,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png",level_one)
      #first platform
      draw_capped_stripx(10,11,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png",level_one)
      #2nd
      draw_capped_stripx(15,8,8,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png",level_one)
      #3rd
      draw_capped_stripx(8,6,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png",level_one)
      #4th
      draw_capped_stripx(15,4,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png",level_one)
      #end zone
      level_one.append(strawberry)
      generate_collision_list()
    if number == 2:
      #top layer of grass: y = 14 
      draw_capped_stripx(0,14,32,"Stone_Corner_Top_Left.png","Stone_Slab_Top.png","Stone_Corner_Top, Right.png",level_two)
      draw_capped_stripx(0,15,32,"Stone_Slab_Left.png","Void.png","Stone_Slab_Right.png",level_two)
      draw_capped_stripx(8,11,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png",level_two)
      draw_capped_stripx(12,9,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png",level_two)
      draw_capped_stripx(16,7,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png",level_two)
      draw_capped_stripx(20,5,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png",level_two)
      level_two.append(Environment_Sprite("Leaf_Slab_Left.png", 23, 13, True))
      level_two.append(Environment_Sprite("Leaf_Slab_Left.png", 23, 12, True))
      level_two.append(Environment_Sprite("Leaf_Slab_Left.png", 23, 11, True))
      level_two.append(Environment_Sprite("Leaf_Slab_Left.png", 23, 10, True))
      level_two.append(Environment_Sprite("Leaf_Corner_Top_Left.png", 23, 9, True))
      level_two.append(strawberry)
      print(level_two)
      generate_collision_list()
      
    if number == 3:
      #ground
 
      draw_capped_stripx(0,14,32, "Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(0,15,32, "Grass_Orange_Center_Left.png","Grass_Orange_Center_Center.png","Grass_Orange_Center_Right.png", level_three)
      #platforms
      draw_capped_stripx(2,12,3,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(9,9,3,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(14,6,3,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(14,2,1,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(20,3,2,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      draw_capped_stripx(5,2,1,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png",level_three)
      #anti cheat wall 
      level_three.append(Environment_Sprite("Grass_Orange_Top_Left.png", 4, 0, True))
      level_three.append(Environment_Sprite("Grass_Orange_Center_Left.png",4,1, True))
      #strawberry
      level_three.append(strawberry)
      generate_collision_list()

      
      
    if number == 4:
#ground

      draw_capped_stripx(0,14,32,"Copper_Bar_Left.png","Copper_Bar_Horizontal.png","Copper_Bar_Right.png",level_four)
      draw_capped_stripx(0,15,32,"Copper_Bar_Left.png","Copper_Bar_Horizontal.png","Copper_Bar_Right.png",level_four)
      #first platform
      draw_capped_stripx(5,11,3,"Metal_Bar_Left.png","Metal_Bar_Horizontal.png","Metal_Bar_Right.png",level_four)
      draw_capped_stripx(7,10,1,"Metal_Bar_Vertical.png","Metal_Bar_Vertical.png","Metal_Bar_Vertical.png",level_four)
      draw_capped_stripx(7,9,2,"Metal_Bar_Left.png","Metal_Bar_Right.png","Metal_Bar_Right.png",level_four)
      #second platform
      draw_capped_stripx(13,7,3,"Bronze_Bar_Left.png","Bronze_Bar_Horizontal.png","Bronze_Bar_Right.png",level_four)
      draw_capped_stripx(15,6,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png",level_four)
      draw_capped_stripx(15,5,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png",level_four)
      draw_capped_stripx(15,4,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png",level_four)
      draw_capped_stripx(15,3,1,"Bronze_Bar_Top.png","Bronze_Bar_Top.png","Bronze_Bar_Top.png",level_four)
      #third platform
      draw_capped_stripx(4,4,1,"Gold_Solid.png","Gold_Solid.png","Gold_Solid.png",level_four)
      #fourth platform
      draw_capped_stripx(26,4,1,"Gold_Bar_Top.png","Gold_Bar_Top.png","Gold_Bar_Top.png",level_four)
      draw_capped_stripx(26,5,1,"Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png",level_four)
      draw_capped_stripx(26,6,1,"Gold_Bar_Bottom.png","Gold_Bar_Bottom.png","Gold_Bar_Bottom.png",level_four)
      draw_capped_stripx(24,3,1,"Bronze_Bar_Top.png","Bronze_Bar_Top.png","Bronze_Bar_Top.png",level_four)
      draw_capped_stripx(24,4,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png",level_four)
      draw_capped_stripx(24,5,1,"Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png",level_four)
      draw_capped_stripx(22,2,1,"Metal_Bar_Top.png","Metal_Bar_Top.png","Metal_Bar_Top.png",level_four)
      draw_capped_stripx(22,3,1,"Metal_Bar_Vertical.png","Metal_Bar_Vertical.png","Metal_Bar_Vertical.png",level_four)
      draw_capped_stripx(22,4,1,"Metal_Bar_Bottom.png","Metal_Bar_Bottom.png","Metal_Bar_Bottom.png",level_four)
      draw_capped_stripx(20,1,1,"Copper_Bar_Top.png","Copper_Bar_Top.png","Copper_Bar_Top.png",level_four)
      draw_capped_stripx(20,2,1,"Copper_Bar_Vertical.png","Copper_Bar_Vertical.png","Copper_Bar_Vertical.png",level_four)
      draw_capped_stripx(20,3,1,"Copper_Bar_Bottom.png","Copper_Bar_Bottom.png","Copper_Bar_Bottom.png",level_four)
      #final platform
      draw_capped_stripx(29,13,1,"Copper_Bar_Bottom.png","Copper_Bar_Bottom.png","Copper_Bar_Bottom.png",level_four)
      draw_capped_stripx(29,12,1,"Copper_Bar_Vertical.png","Copper_Bar_Vertical.png","Copper_Bar_Vertical.png",level_four)
      draw_capped_stripx(29,11,1,"Copper_Bar_Vertical.png","Copper_Bar_Vertical.png","Copper_Bar_Vertical.png",level_four)
      draw_capped_stripx(29,10,1,"Copper_Bar_Vertical.png","Copper_Bar_Vertical.png","Copper_Bar_Vertical.png",level_four)
      draw_capped_stripx(29,9,1,"Copper_Bar_Top.png","Copper_Bar_Top.png","Copper_Bar_Top.png",level_four)
      #end zoned
      level_four.append(strawberry)
      generate_collision_list()
      
    if number == 5:
        Media.p.x = 640
        Media.p.y = -100
        draw_capped_stripx(0, 14, 32, "Grass_Green_Top_Left.png", "Grass_Green_Top_Center.png",
                           "Grass_Green_Top_Right.png", end_screen)
        draw_capped_stripx(0, 15, 32, "Grass_Green_Center_Left.png", "Grass_Green_Center_Center.png",
                           "Grass_Green_Center_Right.png", end_screen)
        draw_capped_stripx(0, 14, 32, "Grass_Green_Top_Left.png", "Grass_Green_Top_Center.png",
                           "Grass_Green_Top_Right.png", end_screen)
        draw_capped_stripx(0, 16, 32, "Grass_Green_Center_Left.png", "Grass_Green_Center_Center.png",
                           "Grass_Green_Center_Right.png", end_screen)
        draw_capped_stripx(0, 17, 32, "Grass_Green_Center_Left.png", "Grass_Green_Center_Center.png",
                           "Grass_Green_Center_Right.png", end_screen)
        end_screen.append(Environment_Sprite("You_Won.png", 15.5, 7, False, False))
        generate_collision_list()

