import datetime
from pathlib import Path
import os.path 
import os

FILE_DIR = os.getcwd() + "/expense_dir"

class CostFunction():

    def current_balanace(self):
        with open(FILE_DIR+"/TOTAL_EXPENSE.txt") as file:
            balance = file.read()
            return balance
    
    def say_hello(self):
        current_date = datetime.datetime.now()
        local_date_time = current_date.strftime("%c")
        print("Welcome Mr. Nazmul Hasan")
        print(local_date_time)
        print("Current balanace: {0}".format(self.current_balanace()))