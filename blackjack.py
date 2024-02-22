import random

def define_cards():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)
def user_hit():
    my_cards.append(define_cards())
def dealer_hit():
    dealer_cards.append(define_cards())
def dealer_pop():
    dealer_cards.pop(-1)
def dealer_continuous_hit(value):
    flag=False
    while not flag:
        if sum(value)<=15:
            dealer_hit()

        elif sum(value)>15:
            if sum(value)>21:
                dealer_pop()
            flag=True

def user_choice():
    flag=False
    while not flag:
        choice = input("What you want to do 'Hit' or 'Stay' ?")
        if choice.lower()=="hit":
            user_hit()
            print(f"Your cards :{my_cards} Dealer cards :{dealer_cards} ")
            if sum(my_cards)>21:
                dealer_continuous_hit(dealer_cards)
                print(f"Dealer Wins -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                flag=True
            
        elif choice.lower()=="stay":
            if sum(dealer_cards)>15 and sum(dealer_cards)<22:
                if sum(my_cards)==sum(dealer_cards):
                    print(f"Its a break even -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
                elif sum(my_cards)>sum(dealer_cards):
                    print(f"You Won -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
                else:
                    print(f"Dealer Wins-- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
            elif sum(dealer_cards)<=15:
                dealer_continuous_hit(dealer_cards)
                """print(f"Your cards :{my_cards} Dealer cards :{dealer_cards} ")"""
                if sum(my_cards)==sum(dealer_cards):
                    print(f"Its a break even -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
                elif sum(my_cards)>sum(dealer_cards):
                    print(f"You Won -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
                else:
                    print(f"Dealer Wins-- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                    flag=True
                flag=True
            else:
                print(f"You Won -- Your cards :{my_cards} Dealer cards :{dealer_cards} ")
                flag=True
my_cards=[]
dealer_cards=[]
for x in range(0,2):
    user_hit()
    if len(my_cards)>=2:
        break
    dealer_hit()
print(f"Your cards :{my_cards} Dealer cards :{dealer_cards}")
user_choice()
