from functions.text import clear
from functions.text import banner
from functions.text import choice_menu

from choices.choice_switch import choice_switch

clear()
print(banner())

while True:
    print(choice_menu())
    query = input('> ')
    choice_switch(query)
