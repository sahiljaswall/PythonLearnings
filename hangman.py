import random
word_list = ["aardvark", "baboon", "camel", "wavelength", "hello", "cartoon"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word = random.choice(word_list)
final=["_"]*len(word)
lives=6
game= False
while not game:
    guess = input("Write your guess ? ").lower()
    for l in range(0,len(word)):
        if word[l] == guess:
            final[l]=word[l]
    if guess not in word:
        print(stages[lives])
        lives-=1
    if lives==0:
        game=True
        print("You lost")
    for l in range(0,len(word)):
        print(final[l],end="")
    if "_" not in final:
        print("You Won")
        game=True
    

        
    
