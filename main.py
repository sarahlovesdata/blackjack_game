############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

from art import logo 
import random
from replit import clear

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return("You both went over 21. You both lose!")
  
  if user_score == computer_score:
    return("It's a draw!")  
  elif user_score == 0:
    return("You got a Blackjack. You win!")
  elif computer_score == 0:
    return("The computer got a Blackjack. You lose!")
  elif user_score > 21:
    return("You went over 21. You lose! Game over")
  elif computer_score > 21:
    return("The computer went over 21. You Win!")
  elif user_score > computer_score:
    return("You win")
  else:
   return("You lose")

def play_game():    

  print(logo)
  print("Welcome! Let's play Blackjack!")

  user_cards = []
  computer_cards = []
  game_ended = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not game_ended:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_ended = True 
    else:
      should_continue = input("Would you like to draw another card? Type 'yes' or 'no':\n ")
      if should_continue == "yes":
        user_cards.append(deal_card())
      else:
        game_ended = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, final score {user_score}")
  print(f"The computers final hand: {computer_cards}, final score {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play Blackjack? Type 'yes' or 'no': ") == "yes":
  clear()
  play_game()


