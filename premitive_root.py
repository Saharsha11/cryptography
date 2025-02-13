def primitive(n,p):
    array = []
    for i in range(1,p):
        val = (n**i) % p
        if val not in array:
            array.append(val)
        else:
            print(f"{n} is not a primitive root of {p}")
            break
    else:
        print(f"{n} is a primitive root of {p}")
    

num = int(input("Enter the number = "))
prime = int(input("Enter a prime number = "))
primitive(num,prime)