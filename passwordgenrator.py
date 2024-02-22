import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Meathod Order not randomised:
"""
for x in range (nr_letters):
    print(random.choice(letters), end="")
for x in range (nr_symbols):    
    print(random.choice(symbols), end="")
for x in range (nr_numbers):    
    print(random.choice(numbers), end="")
print("\n")"""

# Hard Meathod Order randomised:
main=[letters,symbols,numbers]
count=nr_numbers+nr_letters+nr_symbols
for x in range (count+1):
    value = random.choice(main)
    if value is letters and nr_letters is not 0:
        print(random.choice(value),end="")
        nr_letters-=1
    elif value is numbers and nr_numbers is not 0:
        print(random.choice(value),end="")
        nr_numbers-=1
    elif value is symbols and nr_symbols is not 0:
        print(random.choice(value),end="")
        nr_symbols-=1
    else:
        count+=1
print("\n")