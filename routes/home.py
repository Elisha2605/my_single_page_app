from bottle import get, view, request, response
import data



##############  Home  ################
@get('/<user_id>')
@view('home')
def _(user_id):

    try:

        ## info for the home (index)
        user_first_name=data.USERS[user_id]['user_first_name']
        user_last_name=data.USERS[user_id]['user_last_name']
        user_name=data.USERS[user_id]['user_name']
        user_profile_picture=data.USERS[user_id]['user_profile_picture']

        tweets=[]
        for key in reversed(list(data.TWEETS.keys())): 
            tweets.append(data.TWEETS[key])    
            tweet_id=data.TWEETS[key]
        # profile_picture_login

            
        is_fetch = True if request.headers.get('From-Fetch') else False
        return dict(
            title="Twitter",
            is_fetch=is_fetch,
            tweet_id=tweet_id,

            user_id=user_id,

            user_first_name=user_first_name,
            user_last_name=user_last_name,  
            user_name=user_name,
            user_profile_picture=user_profile_picture,

            tweets=tweets,

            tabs=data.tabs, 
            trends=data.trends,
            items=data.items, 
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}