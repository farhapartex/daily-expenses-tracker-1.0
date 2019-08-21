from pathlib import Path
import os
import os.path 

CURRENT_DIR = os.getcwd()
EXPENSE_DIR = CURRENT_DIR + '/expense_dir'

class InitialComponent():

    def check_initial(self):
        if Path(EXPENSE_DIR).is_dir():
            return True
        else:
            return False
            
    def create_initial_setup(self):
        os.mkdir(EXPENSE_DIR)
        if Path(EXPENSE_DIR).is_dir():
            with open(EXPENSE_DIR+"/total_balance.txt","a") as total_expense_file:
                current_amount = input("Type your current amount: ")
                total_expense_file.write(current_amount)
                total_expense_file.close()
            with open(EXPENSE_DIR + "/daily_expenses.txt", "a") as  daily_expense_file:
                daily_expense_file.close()
            
            if Path(EXPENSE_DIR+"/total_balance.txt").is_file() and Path(EXPENSE_DIR + "/daily_expenses.txt").is_file():
                print("Your initial balance is created. Thanks you!")
            else:
                print("Do Something..")
            return True
        else:
            return False