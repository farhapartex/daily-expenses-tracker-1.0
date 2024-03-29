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
        print("Current balance: {:.2f}".format(float(self.current_balanace())))
    
    def command(self, cmd):
        cmd = cmd.split()
        main_cmd = cmd[0]
        if main_cmd == 'expense':
            # amounts = cmd[1].strip()
            amounts = cmd[1].split(",")
            try:
                amounts = [float(x) for x in amounts]
                current_date = datetime.datetime.now()
                local_date_time = current_date.strftime("%c")
                total_amount = sum(amounts)

                if Path(FILE_DIR + "/daily_expenses.txt").is_file() and Path(FILE_DIR + "/total_balance.txt").is_file():
                    with open(FILE_DIR + "/daily_expenses.txt", "a") as daily_expense:
                        daily_expense.write(local_date_time + " -----> " + str(total_amount) + "\n")
                        daily_expense.close()
                        with open(FILE_DIR + "/total_balance.txt", "r+") as total_expense:
                            balance = total_expense.read()
                            balance = float(balance)
                            balance -= total_amount
                            if balance < 0.0:
                                print("You have crossed balance!! Please add")
                            total_expense.seek(0)
                            total_expense.write(str(balance))
                            total_expense.truncate()
                            total_expense.close()
            except:
                print("Wrong input. type help to see commands")
            

            return True

        elif main_cmd == "balance":
            if Path(FILE_DIR + "/total_balance.txt").is_file():
                with open(FILE_DIR + "/total_balance.txt", "r") as total_balance:
                    balance = total_balance.read()
                    balance = float(balance.strip("\n"))
                    print("%.2f" % balance)
                    if balance < 0.0:
                        print("Your balance is negative!! Please add")
                    total_balance.close()
            return True

        elif main_cmd == "add":
            if Path(FILE_DIR + "/total_balance.txt").is_file():
                with open(FILE_DIR + "/total_balance.txt", "r+") as total_balance:
                    balance = total_balance.read()
                    balance = float(balance)
                    amounts = cmd[1].replace(",","")
                    amounts = float(amounts)
                    balance += amounts

                    total_balance.seek(0)
                    total_balance.write(str(balance))
                    total_balance.truncate()
                    total_balance.close()
                    print("Balance Updated! Current balance: {0}".format(balance))
            return True

        elif main_cmd == "delete":
            if Path(FILE_DIR + "/total_balance.txt").is_file():
                with open(FILE_DIR + "/total_balance.txt", "r+") as total_balance:
                    total_balance.write(str(0))
                    total_balance.truncate()
                    total_balance.close()

                    print("Balance deleted!")
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
                    # for expense in daily_expenses:
                    #         print(expense.strip("\n"))
                    first_line = daily_expenses.readline().strip("\n")
                    if first_line == None or len(first_line)==0:
                        print("No history found!")
                    else:
                        print(first_line)
                        for expense in daily_expenses:
                            print(expense.strip("\n"))
                    daily_expenses.close()
            return True

        elif main_cmd == 'stop':
            return False
        
        else:
            print("Command not found! Type help to get commands")
            return True


