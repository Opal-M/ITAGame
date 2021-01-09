from environment_sprite import Environment_Sprite
level_one = [
# Sprite("Grass_Top_1.png", 0, 0, True),
# Sprite("Grass_Top_1.png", 0, 1, True)
]
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
    level_one.append(Environment_Sprite(end, x+length, y, True))
draw_strip(0,13,32,"Grass_Green_Center_Center.png")
draw_strip(0,12,32,"Grass_Green_Top_Center.png")
draw_strip(10,9,10,"Brick_Center_Center.png")
draw_strip(0,14,32,"Grass_Green_Center_Center.png")
draw_strip(0,15,32,"Grass_Green_Center_Center.png")
draw_capped_strip(15,6,8,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
draw_capped_strip(8,3,5,"Brick_Center_Left.png","Brick_Center_Center.png","Brick_Center_Right.png")
