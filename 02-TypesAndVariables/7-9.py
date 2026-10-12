import random
dice_roll_1 = random.randint(1,6)
special1=1
special2=6
print(dice_roll_1)
if dice_roll_1==special1 or dice_roll_1 == special2:
    print("True")
else:
    print("False")