import random 

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
  if guess>answer:
    print("Too high!!!! Slow it Down")
    return turns - 1
  elif guess<answer:
    print("Too low!!!")
    return turns - 1
  else:
    print(f"correct answer! You guessed it right, the answer was {answer}")

def set_difficulty():
  difficulty_level = input("Choose level 'easy' or 'hard': ")
  if difficulty_level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



def game():
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")
  answer= random.randint(1,100)  
  turns= set_difficulty()


  guess=0
  while guess!=answer:
    print(f"You) have {turns} attempts remaining to guess the number")
    guess=int(input("Guess the number: "))
    turns=check_answer(guess,answer,turns)
    if turns==0:
      print("You have lost, You are bad at this")
      return

game()

