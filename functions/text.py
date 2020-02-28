import os

def clear():
    os.system('clear')

def banner():
    return (
        '''
████████╗██╗    ██╗██╗████████╗████████╗███████╗██████╗      ██████╗██╗     ██╗
╚══██╔══╝██║    ██║██║╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗    ██╔════╝██║     ██║
   ██║   ██║ █╗ ██║██║   ██║      ██║   █████╗  ██████╔╝    ██║     ██║     ██║
   ██║   ██║███╗██║██║   ██║      ██║   ██╔══╝  ██╔══██╗    ██║     ██║     ██║
   ██║   ╚███╔███╔╝██║   ██║      ██║   ███████╗██║  ██║    ╚██████╗███████╗██║
   ╚═╝    ╚══╝╚══╝ ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝
                                                                               
        '''
    )

def choice_menu():
    return (
        '''
1 - Post on twitter
2 - Home Timeline
0 - Exit
        '''
    )


def update_status_response_text(requestObject):
    return (
        f'''
Tweet created at {requestObject['created_at']}
Hashtags: {requestObject['entities']['hashtags']}
Urls: {requestObject['entities']['urls']}
User Mentions: {requestObject['entities']['user_mentions']}

Tweet: {requestObject['text']}
User: {requestObject['user']['name']}
            '''
    )