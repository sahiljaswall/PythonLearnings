value = int(input("How long is fizz buzz count : "))
for x in range(1,value+1):
    if x % 3 is 0 and x % 5 is 0:
        print("Fizzbuzz")
    elif x % 3 is 0:
        print("fizz")
    elif x % 5 is 0:
        print("buzz")
    else:
        print(x)