l1=[" ", " ", " "]
l2=[" ", " ", " "]
l3=[" ", " ", " "]
tresure = [l1,l2,l3]
location = input("where you want to dug the treasure ? ")
letter=location[0].lower()
num=int(location[1])-1
compare = ["a","b","c"]
letter_index = compare.index(letter)
tresure[letter_index][num]="x"
print(f"{l1}\n{l2}\n{l3}")

