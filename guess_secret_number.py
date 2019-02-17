# Guess the Secret Number

# Try to find guess the secret number which is between 1 and 100
# Eliminate half ever time, like below
# 50
# 25
# ..
# In 7 turns, you need to find the secret number.

import random as rnd
secret = rnd.randint(1,100)

for x in range(7): # or range(1,8) 
  guess = int(input("Enter a guess:"))
  check = False
  if guess == secret:
    print("Congrats, you've found the secret number :)")
    check = True
    break
  elif guess < secret:
    print("Enter a greater value")
  else:
    print("Enter a smaller value")

if not check: # check == False
  print(":( you have been failed, the number was", secret)