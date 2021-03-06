from auth.validate import validade
client = validade()
    
def status_update(tweet):
    updateStatusRequest = client.request(
        f'https://api.twitter.com/1.1/statuses/update.json?status={tweet}', 
        method='POST'
    )
    return updateStatusRequest

def home_timeline():
    homeTimelineRequest = client.request(
        'https://api.twitter.com/1.1/statuses/home_timeline.json'
    )
    return homeTimelineRequest
