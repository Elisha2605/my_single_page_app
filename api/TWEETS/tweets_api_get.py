from bottle import get, response, request
import data
import json
import re

##############  TWEETS / GET  #################### 
@get('/api-tweets')
def _():
    try:
        tweets = []
        if data.TWEETS == {}:
            response.status = 204
            return {'info': 'No tweets found yet!'}
        
        for key in reversed(list(data.TWEETS.keys())):
            tweets.append(data.TWEETS[key])
        
        response.status = 200
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}


##############  TWEETS/<ID> / GET  ################
@get('/api-tweets/<tweet_id>')
def _(tweet_id):
    try:
        # Validate uuid
        if not re.match(data.REGEX_UUID4, tweet_id):
            response.status = 204
            return
        # Tweet not found
        if tweet_id not in data.TWEETS:
            response.status = 204
            return

        tweet=data.TWEETS[tweet_id]

        response.status = 200
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweet=tweet))

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}