# Python Math Box

# Dice Roll
# mb_dice(n,i) rolls n dice, each die for i times
# Can only roll 5 dice at maximum due to a few limitations
def dice_roll(n,i):
    dice_1 = []
    dice_2 = []
    dice_3 = []
    dice_4 = []
    dice_5 = []
    sum_dice_1 = 0
    sum_dice_2 = 0
    sum_dice_3 = 0
    sum_dice_4 = 0
    sum_dice_5 = 0
    if n > 5:
        print("----------")
        print("Only accept 5 dice at maximum.")
        print("----------")
    elif n <= 5:
        # Rolls and displays the numbers and the sum of 1 die
        if n == 1:
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_1.append(dice_num)
            m = 0
            print("----------")
            print("Dice 1:")
            for o in dice_1:
                print (o, end = " | ")
                sum_dice_1 = sum_dice_1 + o
            print("")
            print("Total:",sum_dice_1)
            print("----------")
        # Rolls and displays the numbers and the sum of 2 dice
        elif n == 2:
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_1.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_2.append(dice_num)
            m = 0
            print("----------")
            print("Dice 1:")
            for o in dice_1:
                print (o, end = " | ")
                sum_dice_1 = sum_dice_1 + o
            print("")
            print("Total:",sum_dice_1)
            print("")
            print("Dice 2:")
            for o in dice_2:
                print (o, end = " | ")
                sum_dice_2 = sum_dice_2 + o
            print("")
            print("Total:",sum_dice_2)
            print("")
            print("Total of 2 dice:",sum_dice_1 + sum_dice_2)
            print("----------")
        # Rolls and displays the numbers and the sum of 3 dice
        elif n == 3:
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_1.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_2.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_3.append(dice_num)
            m = 0
            print("----------")
            print("Dice 1:")
            for o in dice_1:
                print (o, end = " | ")
                sum_dice_1 = sum_dice_1 + o
            print("")
            print("Total:",sum_dice_1)
            print("")
            print("Dice 2:")
            for o in dice_2:
                print (o, end = " | ")
                sum_dice_2 = sum_dice_2 + o
            print("")
            print("Total:",sum_dice_2)
            print("")
            print("Dice 3:")
            for o in dice_3:
                print (o, end = " | ")
                sum_dice_3 = sum_dice_3 + o
            print("")
            print("Total:",sum_dice_3)
            print("")
            print("Total of 3 dice:",sum_dice_1 + sum_dice_2 + sum_dice_3)
            print("----------")
        # Rolls and displays the numbers and the sum of 4 dice
        elif n == 4:
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_1.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_2.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_3.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_4.append(dice_num)
            m = 0
            print("----------")
            print("Dice 1:")
            for o in dice_1:
                print (o, end = " | ")
                sum_dice_1 = sum_dice_1 + o
            print("")
            print("Total:",sum_dice_1)
            print("")
            print("Dice 2:")
            for o in dice_2:
                print (o, end = " | ")
                sum_dice_2 = sum_dice_2 + o
            print("")
            print("Total:",sum_dice_2)
            print("")
            print("Dice 3:")
            for o in dice_3:
                print (o, end = " | ")
                sum_dice_3 = sum_dice_3 + o
            print("")
            print("")
            print("Dice 4:")
            for o in dice_4:
                print (o, end = " | ")
                sum_dice_4 = sum_dice_4 + o
            print("")
            print("Total:",sum_dice_4)
            print("")
            print("Total of 4 dice:",sum_dice_1 + sum_dice_2 + sum_dice_3 + sum_dice_4)
            print("----------")
        # Rolls and displays the numbers and the sum of 5 dice
        elif n == 5:
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_1.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_2.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_3.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_4.append(dice_num)
            m = 0
            for m in range(1,i+1):
                dice_num = random.choice([1,2,3,4,5,6])
                dice_5.append(dice_num)
            m = 0
            print("----------")
            print("Dice 1:")
            for o in dice_1:
                print (o, end = " | ")
                sum_dice_1 = sum_dice_1 + o
            print("")
            print("Total:",sum_dice_1)
            print("")
            print("Dice 2:")
            for o in dice_2:
                print (o, end = " | ")
                sum_dice_2 = sum_dice_2 + o
            print("")
            print("Total:",sum_dice_2)
            print("")
            print("Dice 3:")
            for o in dice_3:
                print (o, end = " | ")
                sum_dice_3 = sum_dice_3 + o
            print("")
            print("Total:",sum_dice_3)
            print("")
            print("Dice 4:")
            for o in dice_4:
                print (o, end = " | ")
                sum_dice_4 = sum_dice_4 + o
            print("")
            print("Total:",sum_dice_4)
            print("")
            print("Dice 5:")
            for o in dice_5:
                print (o, end = " | ")
                sum_dice_5 = sum_dice_5 + o
            print("")
            print("Total:",sum_dice_5)
            print("")
            print("Total of 5 dice:", sum_dice_1 + sum_dice_2 + sum_dice_3 + sum_dice_4 + sum_dice_5)
            print("----------")