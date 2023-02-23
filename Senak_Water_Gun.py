import random

def gamewin(you,comp):
    if you==comp:
        return None
    elif comp=="w":
        if you =="s":
            return True
        elif you =="g":
            return False  
    elif comp=="s":
        if you =="g":
            return True
        elif you =="w":
            return False  

    elif comp=="g":
        if you =="w":
            return True
        elif you =="s":
            return False  

print("Computer turn: water(w) sneak(s), gun(g)")
RanDom=random.randint(1,3)
if RanDom==1:
    comp="s"
elif RanDom==2:    
    comp="w"
elif RanDom==3:    
    comp="g"

you=input("Your turn: water(w) sneak(s), gun(g)")
print("You chose", you)
print("Comp chose",comp)

a=gamewin(you,comp)   
if a==None:
    print("Game is tie")
elif a:
    print("You win")    
else:
    print("You loss")    
    

