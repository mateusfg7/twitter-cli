import json

def handling_response(response):
    decodeRequest = response.decode()
    jsonRequest = json.loads(decodeRequest)
    return jsonRequest