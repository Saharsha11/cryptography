def module(a,b,n):
    if (a%n) == (b%n):
        print(f"{a} and {b} are the congurence module of {n}")
    else:
        print(f"{a} and {b} are not the congurence module of {n}")
    
f = int(input("Enter the first number = "))
s = int(input("Enter the second number = "))
m = int(input("Enter the number for module = "))

module(f,s,m)