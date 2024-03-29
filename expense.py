import datetime
from initial import InitialComponent
from cost import CostFunction
import sys

if __name__ == "__main__":

    initial = InitialComponent()
    cost = CostFunction()

    if not initial.check_initial():
        current_amount = input("Type your current amount: ")
        if len(current_amount) == 0:
            print("Please Enter a valid amount")
            sys.exit()
        else:
            initial.create_initial_setup(current_amount)
    
    if not initial.check_user():
        initial.create_user()
    elif not initial.check_user_exist():
        initial.create_user()
        
    cost.say_hello()

    while True:
        usr_cmd = input("command: ")
        response = cost.command(usr_cmd)

        if response == False:
            break
              
        
