import random
Randon_Num=random.randint(1,100)
print(Randon_Num)
User_Guess=None
guesse=0

while (User_Guess != Randon_Num):
    User_Guess=int(input('Enter a number\n'))
    guesse+=1
    if User_Guess==Randon_Num:
        print("Your guess is correct!")
    else:
        if (User_Guess>Randon_Num):
            print("Your guess is wrong! Enter a Small number")
        else:
            print("Your guess is wrong! Enter a large number")
            
print(f'you guessed number in {guesse} guesses')
with open('userguess.txt','r') as f:
    data=int(f.read())
    print(data)
if (guesse<data):
    print("you have just broken the high score!")
    with open ("userguess.txt",'w')as f:
        f.write(str(guesse))

