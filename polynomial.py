# Python Math Box

# Polynomial
# polyn(a,b,c) outputs results directly and can be combined with other calculations and formulas
# In case there are two possible solutions for the equation, those two will be mixed into one result via addition
def polyn(a,b,c):
    if a <=0:
        return None
    else:
        delta = b**2-4*a*c
        if delta > 0:
            x_1 = (-b+sqrt(delta))/(2*a)
            x_2 = (-b-sqrt(delta))/(2*a)
            return x_1+x_2
        elif delta == 0:
            x = -b/2*a
            return x
        elif delta < 0:
            return None
        else:
            return None

# polyn_d(a,b,c) gives details about the polynomial results, including the Delta value
def polyn_d(a,b,c):
    if a <= 0:
        print("----------")
        print("a must be larger than 0.")
        print("----------")
    else:    
        delta = b**2-4*a*c
        if delta > 0:
            x_1 = (-b+sqrt(delta))/(2*a)
            x_2 = (-b-sqrt(delta))/(2*a)
            print("----------")
            print(a,"x**2 +",b,"* x +",c,"= 0")
            print("Delta = b**2 + 4*a*c =",delta)
            print("→ x_1 =",x_1,"; x_2 =",x_2)
            print("----------")
        elif delta == 0:
            x = -b/2*a
            print("----------")
            print(a,"x**2 +",b,"x +",c,"= 0")
            print("Delta = b**2 + 4*a*c =",delta)
            print("→ x =",x)
            print("----------")
        elif delta < 0:
            print("----------")
            print("No solutions found.")
            print("----------")
        else:
            print("----------")
            print("Something is off, and the calculations cannot continue.")
            print("----------")