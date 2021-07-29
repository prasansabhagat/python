#28/07/21
#print(random.randint(1,100))
import random
player = int(input("What do you choose? 0 for Rock, 1 for paper and 2 for scissor.. \n"))
print(f"You Choose: {player}")
computer = random.randint(0, 2)
print(f"Computer choose: {computer}")
if player == 0 and computer == 2:
    print("You win!")
elif computer > player:
    print("You lose")
elif player == computer:
    print("It's a draw!")
elif player == 2 and computer == 0:
    print("You lose.")
else:
    print("You choose an invalid number, you lose.")



#done