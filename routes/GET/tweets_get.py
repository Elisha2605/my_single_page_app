from bottle import get, response, view, request
import data
import json
import re



##############  TWEETS / GET  #################### 
@get('/tweets')
@view('index')
def _():
    try:
        tweet_id = []
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        for key in data.TWEETS:
            tweet_id.append(key)
        

        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweets=data.TWEETS, tweet_id=tweet_id))

        
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
        response.content_type = 'application/json; charset=UTF-8'
        return json.dumps(dict(tweet=data.TWEETS[tweet_id], tweet_id=tweet_id))
        
            
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}



############## User tweets / GET - ID ##############
@get('/user-tweets/<user_id>')
@view('user-account')
def _(user_id):
    user_tweets = []
    tweet_keys = []
    user = []
    try:

        user_first_name=data.USERS[user_id]['user_first_name']
        user_last_name=data.USERS[user_id]['user_last_name']
        user_name=data.USERS[user_id]['user_name']
        user_profile_picture=data.USERS[user_id]['user_profile_picture']
        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}

        
        # get user info      
        if user_id in data.USERS:
            user_info = data.USERS[user_id]

        # get user_tweet by ID           
        for key in data.TWEETS: 
            if user_id in data.TWEETS[key]['user_id']:
                tweet_id = key
                user_tweets.append(data.TWEETS[key])
       
        #response.content_type = 'application/json; charset=UTF-8'
        is_xhr = True if request.headers.get('spa') else False
        return dict(
                    title="user-account",
                    is_xhr=is_xhr,
                    
                    tweet_id=tweet_id,

                    user_id=user_id, 
                    user_tweets=user_tweets,
                    user_profile_picture=user_profile_picture, 
                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_name=user_name,
                    
                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
    
  
    