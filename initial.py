from pathlib import Path
import os
import os.path 

CURRENT_DIR = os.getcwd()
USER_DIR = CURRENT_DIR + "/files/user"
EXPENSE_DIR = CURRENT_DIR + '/files/expense_dir'

class InitialComponent():

    def check_initial(self):
        if Path(EXPENSE_DIR).is_dir():
            return True
        else:
            return False

    def check_user(self):
        if not os.path.exists(USER_DIR):
            return False
        else:
            return True


    def check_user_exist(self):
        if Path(USER_DIR + "/user.txt").is_file():
            with open(USER_DIR + "/user.txt", "r") as user_file:
                if len(user_file.readline().strip("\n")) == 0:
                    return False
                else:
                    return True


    def create_user(self):
        if not os.path.exists(USER_DIR):
            os.makedirs(USER_DIR)
        with open(USER_DIR + "/user.txt", "a") as user_file:
            user_name = input("User Name: ")
            user_file.write(user_name)
            user_file.close()
    
    def update_user(self):
        if Path(USER_DIR + "/user.txt").is_file():
            user_name = input("User Name: ")
            with open(USER_DIR + "/user.txt", "r+") as user_file:
                user = user_file.read()
                user.seek(0)
                user_file.write(user_name)
                user_file.truncate()
                user_file.close()

            
    def create_initial_setup(self,current_amount):
        if not os.path.exists(EXPENSE_DIR):
            os.makedirs(EXPENSE_DIR)

        # current_amount = input("Type your current amount: ")
        # print(len(current_amount))
        
        if Path(EXPENSE_DIR).is_dir():
            with open(EXPENSE_DIR+"/total_balance.txt","a") as total_expense_file:
                #current_amount = input("Type your current amount: ")
                total_expense_file.write(current_amount)
                total_expense_file.close()
            with open(EXPENSE_DIR + "/daily_expenses.txt", "a") as  daily_expense_file:
                daily_expense_file.close()
            
            if Path(EXPENSE_DIR+"/total_balance.txt").is_file() and Path(EXPENSE_DIR + "/daily_expenses.txt").is_file():
                print("Your initial balance is created. Thanks you!")
            return True
        else:
            return False