from turtle import title
from bottle import get, view, request, response
import data



##############  Home  ################
@get('/<user_id>')
@view('index')
def _(user_id):



    user_first_name=data.USERS[user_id]['user_first_name']
    user_last_name=data.USERS[user_id]['user_last_name']
    user_name=data.USERS[user_id]['user_name']
    user_profile_picture=data.USERS[user_id]['user_profile_picture']
    
    for key in data.TWEETS:
        tweet_id = key
        print('#'*100)
        print(tweet_id)

        
    is_xhr = True if request.headers.get('spa') else False
    return dict(
        is_xhr=is_xhr,
        title="Twitter",

        user_id=user_id, 
        user_first_name=user_first_name,
        user_last_name=user_last_name,
        user_name=user_name,
        user_profile_picture=user_profile_picture,

        users=data.USERS,
        tabs=data.tabs, 
        trends=data.trends,
        items=data.items,
        
        tweet_id=tweet_id,
        tweets=data.TWEETS, 
        )
