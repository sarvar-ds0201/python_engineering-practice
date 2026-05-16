import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        number = random.randint(1, self.sides)
        print(number)



die_6 = Die()

print("Броски 6-гранного кубика:")
for _ in range(10):
    die_6.roll_die()


die_10 = Die(10)

print("\nБроски 10-гранного кубика:")
for _ in range(10):
    die_10.roll_die()


die_20 = Die(20)

print("\nБроски 20-гранного кубика:")
for _ in range(10):
    die_20.roll_die()
