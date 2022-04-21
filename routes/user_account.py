from bottle import get, response, view, request
import data



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
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
                    is_fetch=is_fetch,
                    title="User Account",

                    user_id=user_id,

                    user_tweets=user_tweets,

                    user_first_name=user_first_name,
                    user_last_name=user_last_name,
                    user_name=user_name,
                    user_profile_picture=user_profile_picture,

                    tabs=data.tabs, 
                    trends=data.trends, 
                    items=data.items,

                    count=count
                    ) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}