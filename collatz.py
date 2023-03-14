# Python Math Box

# Collatz conjecture
# Pick a random interger. If the number is even, it will be divided by 2; in reverse, if the number is odd, multiply by 3 then add 1
def collatz(n):
    n_dupes = []
    n_set = []
    i = 0
    print("----------")
    print("Starting number:",n)
    print("")
    # The conjecture ends when the final result is 1, if the starting number is positive
    if n > 0:
        while n > 1:
            if n % 2 == 0:
                i = i + 1
                print(i,". ",n,"is even, so:",n,"/ 2 =",int(n/2))
                n = int(n / 2)
            elif n % 2 != 0:
                i = i + 1
                print(i,". ",n,"is odd, so: 3*",n,"+ 1 =",3*n+1)
                n = 3*n + 1
        print("")
        print("In total,",i,"steps were done to bring the starting number back to 1.")
    # The conjecture ends when the final result is a loop between several numbers, if the starting number is negative
    elif n < 0:
        n_start = n
        if n % 2 == 0:
            i = i + 1
            print(i,". ",n,"is even, so:",n,"/ 2 =",int(n/2))
            n = int(n / 2)
        elif n % 2 != 0:
            i = i + 1
            print(i,". ",n,"is odd, so: 3*",n,"+ 1 =",3*n+1)
            n = 3*n + 1
        while n != n_start:
            if n % 2 == 0:
                i = i + 1
                print(i,". ",n,"is even, so:",n,"/ 2 =",int(n/2))
                n = int(n / 2)
                n_set.append(n)
                n_dupes = set(n_set)
                if len(n_dupes) != len(n_set):
                    break
            elif n % 2 != 0:
                i = i + 1
                print(i,". ",n,"is odd, so: 3*",n,"+ 1 =",3*n+1)
                n = 3*n + 1
                n_set.append(n)
                n_dupes = set(n_set)
                if len(n_dupes) != len(n_set):
                    print("A loop has been detected, so this step will not be counted.")
                    break
        print("")
        print("In total,",i-1,"steps were done to bring the starting number to a loop.")
    print("----------")