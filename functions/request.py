import json

def handling_requests(request):
    decodeRequest = request.decode()
    jsonRequest = json.loads(decodeRequest)
    return jsonRequest