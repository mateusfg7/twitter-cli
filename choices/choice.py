from pprint import pprint

from functions.request import handling_requests

from api_requests.api_request import status_update

def choice_menu(choice):
    
    if choice == '1':
        tweet = input('text: ')
        updateStatusRequest = status_update(tweet)
        requestObject = handling_requests(updateStatusRequest[1])
        print(
            f'''
Tweet created at {requestObject['created_at']}
Hashtags: {requestObject['entities']['hashtags']}
Urls: {requestObject['entities']['urls']}
User Mentions: {requestObject['entities']['user_mentions']}

Tweet: {requestObject['text']}
User: {requestObject['user']['name']}
            '''
        )