#rock paper scissors or snake water gun
import random
def gameWin(comp,you):
    #if two values are equal, declare a tie!
    if comp==you:
        return None

          #check for all the posibilities when computer choose s

    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True

            #check for all the posibilities when computer choose w
    elif comp=='w':
        if you=='g':
            return False
        elif you =='s':
            return True

            #check for all the posibilities when computer choose g
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True    
print("comp Turn: snake(s) water(w) or gun(g)?")            
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g' 
    pass
# randNo=random.randint(1,3)
# print(randNo)
you=input("your Turn: snake(s) water(w) or gun(g)?")
a = gameWin(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")
if a==None:
    print("the game is tie")
elif a:
    print("you win!")
else:
    print("you lose!")
