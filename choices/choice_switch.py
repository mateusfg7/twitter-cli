from choices.choice_method import status_update_function
from choices.choice_method import home_timeline_function

def choice_switch(choice):
    if choice == '1':
        status_update_function()
    
    if choice == '2':
        home_timeline_function()
    
    elif choice == '0':
        print('exiting...')
        exit()