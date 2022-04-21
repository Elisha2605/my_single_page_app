
from bottle import get, response, view, request
import data
import json
import re


##############  TWEETS / GET  #################### 
@get('/tweets')
@view('home')
def _():
    try:
        tweets = []
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        # tweets
        for key in reversed(list(data.TWEETS.keys())):
            tweets.append(data.TWEETS[key])

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))

        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}



    