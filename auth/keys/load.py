import json

def get_keys():
    with open('auth/keys/keys.temp.json', 'r') as keys:
        keysObject = json.loads(keys.read())
    
    return keysObject