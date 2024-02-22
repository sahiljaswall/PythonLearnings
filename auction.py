auctioner = {}
dictt={}
flag = True
updated_price=0
updated_name =""
print("<------Wecome to Secert Aution------>")
while flag is not False:
    name = input("Write your name : ")
    cost = int(input("Write your Bid : "))
    dictt[name]=cost
    auctioner.update(dictt)
    choice=input("Enter 'yes' to add more or 'no' to find winner : ")
    if choice.lower() == "yes":
        flag=True
    elif choice.lower() == "no":
        for people in auctioner:
            if auctioner[people]>updated_price:
                updated_price=auctioner[people]
                updated_name=people
        print(f"Winner of auction is {updated_name}")
        flag=False   