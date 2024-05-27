2

import random
user_choice=int(input("Enter your choice: Type 0 for Rock. 1 for Paper. 2 for  Scissor"))
computer_choice=random.randint(0,2)
print("Computer chose:")
print(computer_choice)
if computer_choice==user_choice:
    print("it is a draw")
elif computer_choice== 0 and user_choice==2:
    print("You lose")
elif user_choice== 0 and computer_choice==2:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
