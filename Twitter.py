from functions.text import banner
from functions.text import choice_menu

from choices.choice import choice_request

print(banner())

while True:
    print(choice_menu())
    query = input('> ')
    choice_request(query)
