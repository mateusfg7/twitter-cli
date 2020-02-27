from functions.text import clear
from functions.text import banner
from functions.text import choice_menu

from choices.choice import choice_request

clear()
print(banner())

while True:
    print(choice_menu())
    query = input('> ')
    choice_request(query)
