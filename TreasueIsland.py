print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")
first_choice = input("Which one, left or right?")
if first_choice == "left":
    second_choice = input("swim or wait?")
    if second_choice == "wait":
        third_choice = input("red, blue or yellow ")
        if third_choice == "yellow":
            print("YOU WIN!!!")
        else:
            print("Game Over :(")
    else:
        print("Game Over :(")
else:
    print("Game Over :(")
#27/07/21
#done
