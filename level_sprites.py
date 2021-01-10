import pygame
from environment_sprite import Environment_Sprite
from object_sprite import Object_Sprite
title_screen = []
level_one = [
# Sprite("Grass_Top_1.png", 0, 0, True),
# Sprite("Grass_Top_1.png", 0, 1, True)
]
# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Center_Center.png",number , 13 , True))
# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Top_Center.png", number, 12, True))

#ATTENTION FOR THE BRONZE SPRITES I MISSPELLED VERTICLE USE THE WORD 'veritical'

def draw_strip(x,y,length,image):
    for number in range(0,length):
        title_screen.append(Environment_Sprite(image, x+number, y, True))
def draw_capped_strip0(x,y,length,start,middle,end): #This has a 0 because its different
    title_screen.append(Environment_Sprite(start, x, y, True))
    for number in range(1,length):
        title_screen.append(Environment_Sprite(middle, x+number, y, True))
    title_screen.append(Environment_Sprite(end, x+(length-1), y, True))
def draw_level0(number):
    if number == 0:
        #ground
        draw_capped_strip0(0,13,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        draw_capped_strip0(0,12,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png")
        draw_capped_strip0(0,14,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        draw_capped_strip0(0,15,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        #T
        draw_capped_strip0(2,2,3,"Bronze_Bar_Left.png","Bronze_Bar_Horizontal.png","Bronze_Bar_Right.png")
        draw_capped_strip0(3,3,1,"Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png","Bronze_Bar_Veritical.png")
        draw_capped_strip0(3,4,1,"Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png","Bronze_Bar_Bottom.png")
        #I
        draw_capped_strip0(6,2,3,"Metal_Bar_Left.png","Metal_Bar_Horizontal.png","Metal_Bar_Right.png")
        draw_capped_strip0(7,3,1,"Metal_Bar_Vertical.png","Metal_Bar_Vertical.png","Metal_Bar_Vertical.png")
        draw_capped_strip0(6,4,3,"Metal_Bar_Left.png","Metal_Bar_Horizontal.png","Metal_Bar_Right.png")
        #K
        draw_capped_strip0(10,2,1,"Copper_Bar_Top.png","Copper_Bar_Top.png","Copper_Bar_Top.png")
        draw_capped_strip0(12,2,1,"Copper_Solid.png","Copper_Solid.png","Copper_Solid.png")
        draw_capped_strip0(10,3,2,"Copper_Bar_Vertical.png","Copper_Bar_Right.png","Copper_Bar_Right.png")
        draw_capped_strip0(10,4,1,"Copper_Bar_Bottom.png","Copper_Bar_Bottom.png","Copper_Bar_Bottom.png")
        draw_capped_strip0(12,4,1,"Copper_Solid.png","Copper_Solid.png","Copper_Solid.png")
        #I
        draw_capped_strip0(14,2,3,"Gold_Bar_Left.png","Gold_Semi_Solid_Horizontal.png","Gold_Bar_Right.png")
        draw_capped_strip0(15,3,1,"Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png","Gold_Semi_Solid_Vertical.png")
        draw_capped_strip0(14,4,3,"Gold_Bar_Left.png","Gold_Semi_Solid_Horizontal.png","Gold_Bar_Right.png")
        #-
        draw_capped_strip0(18,3,2,"Grass_Pink_Top_Left.png","Grass_Pink_Top_Right.png","Grass_Pink_Top_Right.png")
        #O
        draw_capped_strip0(21,2,3,"Leaf_Corner_Top_Left.png","Leaf_Slab_Top.png","Leaf_Corner_Top_Right.png")
        draw_capped_strip0(21,3,1,"Leaf_Slab_Left.png","Leaf_Slab_Left.png","Leaf_Slab_Left.png")
        draw_capped_strip0(23,3,1,"Leaf_Slab_Right.png","Leaf_Slab_Right.png","Leaf_Slab_Right.png")
        draw_capped_strip0(21,4,3,"Leaf_Corner_Bottom_Left.png","Leaf_Slab_Bottom.png","Leaf_Corner_Bottom_Right.png")
        #H
        draw_capped_strip0(25,2,1,"Brick_Top_Left.png","Brick_Top_Left.png","Brick_Top_Left.png")
        draw_capped_strip0(27,2,1,"Brick_Top_Right.png","Brick_Top_Right.png","Brick_Top_Right.png")
        draw_capped_strip0(25,3,3,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
        draw_capped_strip0(25,4,1,"Brick_Bottom_Left.png","Brick_Bottom_Left.png","Brick_Bottom_Left.png")
        draw_capped_strip0(27,4,1,"Brick_Bottom_Right.png","Brick_Bottom_Right.png","Brick_Bottom_Right.png")
        #!
        draw_capped_strip0(29,2,1,"Wood_Slab_Left.png","Wood_Slab_Left.png","Wood_Slab_Left.png")
        draw_capped_strip0(29,3,1,"Wood_Slab_Left.png","Wood_Slab_Left.png","Wood_Slab_Left.png")
        draw_capped_strip0(29,4,1,"Wood_Cube_Bottom_Left.png","Wood_Cube_Bottom_Left.png","Wood_Cube_Bottom_Left.png")
        #_
        draw_capped_strip0(2,6,28,"Grass_Orange_Top_Left.png","Grass_Orange_Top_Center.png","Grass_Orange_Top_Right.png")
        #end zone
        title_screen.append(Object_Sprite("Fruit_Strawberry/tile004.png", 30, 10, False))

def draw_strip(x,y,length,image):
    for number in range(0,length):
        level_one.append(Environment_Sprite(image, x+number, y, True))
def draw_capped_strip(x,y,length,start,middle,end):
    level_one.append(Environment_Sprite(start, x, y, True))
    for number in range(1,length):
        level_one.append(Environment_Sprite(middle, x+number, y, True))
    level_one.append(Environment_Sprite(end, x+(length-1), y, True))
def draw_level(number):
    if number == 1:
        #ground
        draw_capped_strip(0,13,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        draw_capped_strip(0,12,32,"Grass_Green_Top_Left.png","Grass_Green_Top_Center.png","Grass_Green_Top_Right.png")
        draw_capped_strip(0,14,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        draw_capped_strip(0,15,32,"Grass_Green_Center_Left.png","Grass_Green_Center_Center.png","Grass_Green_Center_Right.png")
        #first platform
        draw_capped_strip(10,9,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
        #2nd
        draw_capped_strip(15,6,8,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
        #3rd
        draw_capped_strip(8,4,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
        #4th
        draw_capped_strip(15,2,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
        #end zone
        level_one.append(Object_Sprite("Fruit_Strawberry/tile004.png", 18, 1, False))

