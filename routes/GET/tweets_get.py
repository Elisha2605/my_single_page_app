
from bottle import get, response, view, request
import data
import json
import re


##############  TWEETS / GET  #################### 
@get('/tweets')
#@view('index')
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
@get('/user-account/<user_id>')
@view('user-account')
def _(user_id):

    try:
        user_first_name=data.USERS[user_id]['user_first_name']
        user_last_name=data.USERS[user_id]['user_last_name']
        user_name=data.USERS[user_id]['user_name']
        user_profile_picture=data.USERS[user_id]['user_profile_picture']
        
        user_tweets = []
        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}


        # get user_tweet by ID           
        for key in reversed(list(data.TWEETS.keys())): 
            if user_id in data.TWEETS[key]['user_id']:
                user_tweets.append(data.TWEETS[key])
       
        #response.content_type = 'application/json; charset=UTF-8'
        return dict(
                    user_id=user_id,

                    user_tweets=user_tweets,

                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_name=user_name,
                    user_profile_picture=user_profile_picture,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
    


############## USER TWEETS / GET ##############
@get('/user-profile/<user_id>')
@view('user-profile')
def _(user_id):

    try:
        user_first_name=data.USERS[user_id]['user_first_name']
        user_last_name=data.USERS[user_id]['user_last_name']
        user_name=data.USERS[user_id]['user_name']
        user_profile_picture=data.USERS[user_id]['user_profile_picture']
       
        
        user_tweets = []
        
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}


        # get user_tweet by ID           
        for key in reversed(list(data.TWEETS.keys())): 
            if user_id in data.TWEETS[key]['user_id']:
                user_tweets.append(data.TWEETS[key])
       
        #response.content_type = 'application/json; charset=UTF-8'
        return dict(
                    user_id=user_id,

                    user_tweets=user_tweets,

                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_name=user_name,
                    user_profile_picture=user_profile_picture,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}


############## ADMIN PAGE / GET ##############
@get('/admin-page')
@view('admin')
def _():

    try:
        tweets = []
        if data.TWEETS == {}:
            return {'info': 'No tweets found yet!'}
        
        # tweets
        for key in reversed(list(data.TWEETS.keys())):
            tweets.append(data.TWEETS[key])

        #response.content_type = 'application/json; charset=UTF-8'
        return dict(tweets=tweets)

        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
    