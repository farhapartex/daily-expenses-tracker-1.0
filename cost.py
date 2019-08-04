import datetime

class CostFunction():
    
    def say_hello(self):
        print("Welcome Mr. Nazmul Hasan")
        current_date = datetime.datetime.now()
        local_date_time = current_date.strftime("%c")
        print(local_date_time)