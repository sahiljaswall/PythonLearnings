import random
listt = ["Stone","Paper", "Scissors"]
human="ak"
robotcount = 0
humancount = 0
while human!="q":
    robot = random.choice(listt)
    print(f"You can choose out of these there {listt[0]}, {listt[1]}, {listt[2]} ")
    human = input("What is your choice ? OR 'q' for quit ")
    print(f"Robot choice was {robot}")
    if robot == human.capitalize():
        print("Its a DRAW ")
    elif robot is listt[0] and human.capitalize is listt[1] or robot is listt[1] and human.capitalize is listt[2] or robot is listt[2] and human.capitalize is listt[0]:
        print("You WONNNNN ")
        humancount+=1
    else:
        print("Robot WIN")
        robotcount+=1
