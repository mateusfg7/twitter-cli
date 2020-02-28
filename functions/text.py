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


def update_status_response_text(responseObject):
    return (
        f'''
Tweet created at {responseObject['created_at']}
Hashtags: {responseObject['entities']['hashtags']}
Urls: {responseObject['entities']['urls']}
User Mentions: {responseObject['entities']['user_mentions']}

Tweet: {responseObject['text']}
User: {responseObject['user']['name']}
            '''
    )