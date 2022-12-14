import random
#For Rock=1 Or (r)
#   Paper=2 Or (p)
#  Sissor=3 Or (s)

def game(c,p):
    if(c==p):
        print("Match Draw")
    elif(c=="r"):
        if(p=="p"):
            print("You Win!")
        elif(p=="s"):
            print("You Loose!")
    elif(c=="p"):
        if(p=="s"):
            print("You Win!")
        elif(p=="r"):
            print("You Loose!")
    elif(c=="s"):
        if(p=="r"):
            print("You Win!")
        elif(p=="p"):
            print("You Loose!")

comp=""
randomNo=random.randint(1,3)
if(randomNo==1):
    comp="r";
elif(randomNo==2):
    comp="p"
elif(randomNo==3):
    comp="s"
print("It's Computer Turn Rock(r) or Paper(p) or Scissor(s)")
player=input("It's your turn Rock(r) Or Paper(p) Or Scissor(s): ")

print("Computer Choosen: ",comp)
print("You Choosen: ",player,end="\n")

game(comp,player)