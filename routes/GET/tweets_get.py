from bottle import get, response, view, request
import data
import json
import re



##############  TWEETS / GET  #################### 
@get('/tweets')
@view('index')
def _():
    try:
        tweets = []
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        # tweets
        for key in data.TWEETS:
            tweets.append(data.TWEETS[key])
            print('#'*100)
            print(tweets)

        #response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=tweets))

        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}



##############  TWEETS/<ID> / GET  ################
@get('/tweets/<tweet_id>')
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
        # Succes
        tweet=data.TWEETS[tweet_id]
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweet=tweet))
        
            
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}



############## User tweets / GET - ID ##############
@get('/user-tweets/<user_id>')
# @view('user-account')
def _(user_id):

    try:

        user_tweets = []
        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}


        # get user_tweet by ID           
        for key in data.TWEETS: 
            if user_id in data.TWEETS[key]['user_id']:
                user_tweets.append(data.TWEETS[key])
       
        #response.content_type = 'application/json; charset=UTF-8'
        is_xhr = True if request.headers.get('spa') else False
        return dict(
                    title="user-account",
                    is_xhr=is_xhr,

                    user_tweets=user_tweets,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
    
  
    