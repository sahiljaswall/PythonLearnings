choice = int(input(" For encryption press 1 or For decrypt press 0 ? "))
if choice == 1:
    message = input("Write your message for encryption here : ")
elif choice == 0:
    message = input("Write your encrypted message here : ")
else:
    print("invalid choice")
key = int(input("What is the Key : "))
exitt=False
while exitt is not True:
    encrypt = ""
    decrypt = ""
    if choice == 1: 
        for letter in message:
            encrypt = encrypt+chr(ord(letter)+key)
        print(f"Encrypted message is {encrypt}",end="\n")
        exitt = True
    elif choice == 0:
        for letter in message:
            decrypt = decrypt+chr(ord(letter)-key)
        print(f"Encrypted message is {decrypt}",end="\n")
        exitt = True