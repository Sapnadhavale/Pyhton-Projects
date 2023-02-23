from datetime import datetime

def GetTime():
    return datetime.now()

def Take_Data(n):
    if n==1:
      ch=int(input("1 For exercise and 2 for food"))
    if (ch==1):
        val=input("Type your input here.\n")
        with open("har.txt","a") as f:
            f.write(str(GetTime()) + ":" + val +"\n")
        print("Saved sucessfully")    

    elif (ch==2):
        val=input("Type your input here.\n")
        with open("har2.txt","a") as f:
            f.write(str(GetTime()) + " :" + val + "\n")
        print("sucessfully")    

def Get_Data(n):
    if (n==2):
        obj=int(input("1 For get food and 2 for get exercise."))
        if (obj==1):
            with open ("har.txt") as f:
                data=f.read()
            print(data)

        elif(obj==2):
            with open ("har2.txt") as f:
               data=f.read()
            print(data)

Userinput=int(input("enter 1 for Take_data and 2 for Get_data"))
if Userinput == 1:
    Take_Data(Userinput)
elif Userinput == 2:
    Get_Data(Userinput)    
