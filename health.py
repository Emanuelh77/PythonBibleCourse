import random

health = 50

difficulty = 3

potionHealth = int(random.randint(25,50) / difficulty)

health += potionHealth

print(health)

pizza = 10