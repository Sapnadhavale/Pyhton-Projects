new=[]
def Hind_card(card_number):
    for i in card_number:
      last_four_latter=i[-4:]
      formatted_card=f"************{last_four_latter}"
      new.append(formatted_card)
    return new
     
my_card=Hind_card(["1234432156788765","0987789065433456"])    
print(my_card[0])

