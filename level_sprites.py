from environment_sprite import Environment_Sprite
level_one = [
# Sprite("Grass_Top_1.png", 0, 0, True),
# Sprite("Grass_Top_1.png", 0, 1, True)
]
for number in range(0, 32):
    level_one.append(Environment_Sprite("Grass_Green_Center_Center.png",number ,13 , True))
for number in range(0, 32):
    level_one.append(Environment_Sprite("Grass_Green_Top_Center.png", number, 12, True))