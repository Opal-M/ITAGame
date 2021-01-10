import pygame
from environment_sprite import Environment_Sprite
from object_sprite import Object_Sprite

level_one = [
# Sprite("Grass_Top_1.png", 0, 0, True),
# Sprite("Grass_Top_1.png", 0, 1, True)
]
level_two= []
# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Center_Center.png",number , 13 , True))
# for number in range(0, 32):
#     level_one.append(Environment_Sprite("Grass_Green_Top_Center.png", number, 12, True))

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
        level_one.append(Object_Sprite("Fruit_Strawberry/tile004.png", 18, 1, True))
    elif number == 2:
        pass    

