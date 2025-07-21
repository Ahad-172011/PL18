import random
playing = True
number = str(random.randint(10,30))
print("I will generate a number from 10 to 30, and you have to guess the number one digit at a time.")
print("The game ends when you get 1 point")
while playing:
  guess = input("give me your best guess : ")
  if number == guess:
    print("you win the game")
    print("the number was", number)
    break
  else:
    print("your guess isn't quite right, try again. \n")