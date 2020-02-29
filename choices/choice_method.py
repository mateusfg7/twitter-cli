from pprint import pprint

from functions.response import handling_response

from api_requests.api_request import status_update
from api_requests.api_request import home_timeline

from functions.text import clear
from functions.text import banner
from functions.text import update_status_response_text
from functions.text import home_timelin_response_text

def status_update_function():
    clear()
    print(banner())
    
    tweet = input('\nTweet: ')
    
    updateStatusRequest = status_update(tweet)
    responseObject = handling_response(updateStatusRequest[1])
    
    print(update_status_response_text(responseObject))

def home_timeline_function():
    clear()
    print(banner())

    homeTimelineRequest = home_timeline()
    responseObject = handling_response(homeTimelineRequest[1])

    print(home_timelin_response_text(responseObject[1]))
    # pprint(responseObject[1])