import datetime
from initial import InitialComponent
from cost import CostFunction

# current_date = datetime.datetime.now()
# local_date_time = current_date.strftime("%c")
# print(local_date_time)
# f = open("demo.txt","a")
# dummy_text = input()
# dummy_text += '\n'
# f.write(dummy_text)
# f.close()

if __name__ == "__main__":

    initial = InitialComponent()
    cost = CostFunction()

    if not initial.check_initial():
        initial.create_initial_setup()
    
    if not initial.check_user():
        initial.create_user()
    elif not initial.check_user_exist():
        initial.create_user()
        
    cost.say_hello()

    # while True:
    #     usr_cmd = input("command: ")
    #     response = cost.command(usr_cmd)

    #     if response == False:
    #         break
              
        
