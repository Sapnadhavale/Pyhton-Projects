import random

#  Game variable
Deck=10
p_won_score= (Deck/2) +1

class players:
  def __init__(self,name):
    self.name=name
    self.points=0
    self.cards=list(range(1,Deck + 1 ,1))

    random.shuffle(self.cards)

  def pick_card(self):
    picked_card=self.cards[0] 
    self.cards.remove(picked_card)
    print(f"{self.name} card is {picked_card}")
    return picked_card

  def add_points(self):
    self.points += 1
    print(f"The points added to {self.name}") 

  def is_game_over(self):
    return len(self.cards) == 0 or self.points == p_won_score


p1=players("Player 1") 
p2=players("Player 2") 

print("Game Starts..........")
while True:
  input("Enter to pick a card!")
  p1_card=p1.pick_card()
  p2_card=p2.pick_card()

  if p1_card > p2_card:
    p1.add_points()
  elif p2_card > p1_card:
    p2.add_points()  
  else:
    print("TIE!") 

  if p1.is_game_over() or p2.is_game_over():
    print("Game Over !") 

    if p1.points > p2.points:
      print(f"{p1.name} Wins!")
    elif p2.points > p1.points:
      print(f"{p2.name} Wins!")
    else:
      print("Score is TIE !")

    print(f"Final Score :{p1.points} - {p2.points}")  

    break


  print(f"SCORE :{p1.points} - {p2.points}")  

  


