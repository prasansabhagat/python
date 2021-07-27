#26/07/21
#print(random.randint(1,100))
import random
player = input("What do you choose? 0 for Rock, 1 for paper and 2 for scissor.. \n")
print("You Choose: \n")
if player == 0:
    print("""
            _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
        """)
elif player == 1:
    print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
        """)
else:
    print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
        """)
computer = print("Computer choose " + random.randint(0, 2))

