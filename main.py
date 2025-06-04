import random

diceRolling = True

while diceRolling:
    print(random.randrange(1 , 6))
    plaAgain = input("Do you want to Roll Againg [y/n]").lower()
    if plaAgain == "y" :
        continue
    else:
        print('game over')
        break

