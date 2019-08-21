import datetime
from pathlib import Path
import os.path 
import os

FILE_DIR = os.getcwd() + "/files/expense_dir"
USER_DIR = os.getcwd() + "/files/user"

class CostFunction():

    def current_balanace(self):
        with open(FILE_DIR+"/total_balance.txt") as file:
            balance = file.read()
            return balance
    
    def say_hello(self):
        current_date = datetime.datetime.now()
        local_date_time = current_date.strftime("%c")
        user = "User"
        if Path(USER_DIR + "/user.txt").is_file():
            with open(USER_DIR + "/user.txt", "r") as user_flle:
                user = user_flle.readline().strip("\n")
        print("Welcome Mr. {0}".format(user))
        print(local_date_time)
        print("Current balance: {0}".format(self.current_balanace()))
    
    def command(self, cmd):
        cmd = cmd.split()
        main_cmd = cmd[0]
        if main_cmd == 'expense':
            amounts = cmd[1].split(",")
            amounts = [int(x) for x in amounts]
            current_date = datetime.datetime.now()
            local_date_time = current_date.strftime("%c")
            total_amount = sum(amounts)

            if Path(FILE_DIR + "/daily_expenses.txt").is_file() and Path(FILE_DIR + "/total_balance.txt").is_file():
                with open(FILE_DIR + "/daily_expenses.txt", "a") as daily_expense:
                    daily_expense.write(local_date_time + " -----> " + str(total_amount) + "\n")
                    daily_expense.close()
                with open(FILE_DIR + "/total_balance.txt", "r+") as total_expense:
                    balance = total_expense.read()
                    balance = int(balance)
                    balance -= total_amount
                    total_expense.seek(0)
                    total_expense.write(str(balance))
                    total_expense.truncate()
                    total_expense.close()

            return True

        elif main_cmd == "balance":
            if Path(FILE_DIR + "/total_balance.txt").is_file():
                with open(FILE_DIR + "/total_balance.txt", "r") as total_expense:
                    balance = total_expense.read()
                    print(balance.strip("\n"))
                    total_expense.close()
            return True

        elif main_cmd == 'help':
            with open(os.getcwd() + "/commands/command.txt", "r") as cmd_file:
                for command in cmd_file:
                    print(command.strip("\n"))
                cmd_file.close()
            return True
        
        elif main_cmd == "history":
            if Path(FILE_DIR + "/daily_expenses.txt").is_file():
                with open(FILE_DIR + "/daily_expenses.txt", "r") as daily_expenses:
                    if len(daily_expenses.readline().strip("\n")) == 0:
                        print("No history found!")
                    else:
                        for expense in daily_expenses:
                            print(expense.strip("\n"))
                    daily_expenses.close()
            return True

        elif main_cmd == 'stop':
            return False
        
        else:
            print("Command not found! Type help to get commands")
            return True


