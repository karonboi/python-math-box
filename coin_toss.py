# Python Math Box

# Coin Toss            
# mb_coins(n,i) Tosses n coins, each coin for i times
# Can only toss 5 coins at maximum, just like the dice
def coin_toss(n,i):
    coins_1 = []
    coins_2 = []
    coins_3 = []
    coins_4 = []
    coins_5 = []
    if n > 5:
        print("----------")
        print("Only accept 5 coins at maximum.")
        print("----------")
    elif n <= 5:
        # Tosses and displays the faces of 1 coin
        if n == 1:
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_1.append(coins_face)
            m = 0
            print("----------")
            print("Coin 1:")
            for o in coins_1:
                print (o, end = " | ")
            print("")
            print("----------")
        # Tosses and displays the faces of 2 coins
        elif n == 2:
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_1.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_2.append(coins_face)
            m = 0
            print("----------")
            print("Coin 1:")
            for o in coins_1:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 2:")
            for o in coins_2:
                print (o, end = " | ")
            print("")
            print("----------")
        # Tosses and displays the faces of 3 coins
        elif n == 3:
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_1.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_2.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_3.append(coins_face)
            m = 0
            print("----------")
            print("Coin 1:")
            for o in coins_1:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 2:")
            for o in coins_2:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 3:")
            for o in coins_3:
                print (o, end = " | ")
            print("")
            print("----------")
        # Tosses and displays the faces of 4 coins
        elif n == 4:
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_1.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_2.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_3.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_4.append(coins_face)
            m = 0
            print("----------")
            print("Coin 1:")
            for o in coins_1:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 2:")
            for o in coins_2:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 3:")
            for o in coins_3:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 4:")
            for o in coins_4:
                print (o, end = " | ")
            print("")
            print("----------")
        # Tosses and displays the faces of 5 coins
        elif n == 5:
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_1.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_2.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_3.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_4.append(coins_face)
            m = 0
            for m in range(1,i+1):
                coins_face = random.choice(['█','░'])
                coins_5.append(coins_face)
            m = 0
            print("----------")
            print("Coin 1:")
            for o in coins_1:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 2:")
            for o in coins_2:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 3:")
            for o in coins_3:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 4:")
            for o in coins_4:
                print (o, end = " | ")
            print("")
            print("")
            print("Coin 5:")
            for o in coins_5:
                print (o, end = " | ")
            print("")
            print("----------")