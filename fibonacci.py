# Python Math Box

# Fibonacci sequence
# The Fibonacci sequence is an infinite sequence of natural numbers starting with two elements 0 or 1 and 1, the elements are then set up according to the rule that each element is always equal to the sum of the two preceding it
# fibonacci(n) works te same here. The n represents the recurrence relation, which is something that looks like this: F_0 = 0, F_1 = 1, and F_n = F_(n-1) + F(n-2)
def fibonacci(n):
    F = [0,1]
    if n < 2:
        print("----------")
        print("Recurrence relation must be larger or equal to 2.")
        print("----------")
    elif n >= 2:
        print("----------")
        print("0 |  0")
        print("1 |  0 + 1 = 1")
        for i in range(2,n+1):
            F.append(F[i-1]+F[i-2])
            print(i," | ",F[i-1],"+",F[i-2],"=",F[i])
        print("----------")