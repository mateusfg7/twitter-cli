from pprint import pprint

from functions.response import handling_response
from functions.resTXT import update_status_response_text

from api_requests.api_request import status_update

def choice_menu(choice):
    
    if choice == '1':
        
        tweet = input('text: ')
        
        updateStatusRequest = status_update(tweet)
        requestObject = handling_response(updateStatusRequest[1])
        
        print(update_status_response_text(requestObject))