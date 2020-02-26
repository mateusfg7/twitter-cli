import oauth2

from auth.keys.load import get_keys

def validade():
    keys = get_keys()

    consumer = oauth2.Consumer(
        keys['api_key'],
        keys['api_secret_key']
    )
    token = oauth2.Token(
        keys['access_token'],
        keys['access_token_secret']
    )
    client = oauth2.Client(consumer, token)
    
    return client