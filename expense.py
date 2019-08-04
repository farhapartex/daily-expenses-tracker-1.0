import datetime
from initial import InitialComponent

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
    if not initial.check_initial():
        initial.create_initial_setup()
    else:
        current_date = datetime.datetime.now()
        local_date_time = current_date.strftime("%c")
        print(local_date_time)
        
