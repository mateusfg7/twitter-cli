from pprint import pprint

from functions.response import handling_response

from functions.text import clear
from functions.text import banner
from functions.text import update_status_response_text

from api_requests.api_request import status_update

def choice_request(choice):
    
    if choice == '1':

        clear()
        print(banner())
        
        tweet = input('\nTweet: ')
        
        updateStatusRequest = status_update(tweet)
        requestObject = handling_response(updateStatusRequest[1])
        
        print(update_status_response_text(requestObject))
    
    elif choice == '0':
        print('exiting...')
        exit()