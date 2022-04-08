from turtle import title
from bottle import get, view, request, response
import data



##############  Home  ################
@get('/<user_id>')
@view('index')
def _(user_id):

    tweets=[]
    user_first_name=data.USERS[user_id]['user_first_name']
    user_last_name=data.USERS[user_id]['user_last_name']
    user_name=data.USERS[user_id]['user_name']
    user_profile_picture=data.USERS[user_id]['user_profile_picture']

    # users
    for user_id in data.USERS:
        users = data.USERS[user_id]
        print('#'*100)
        print(users)
    
    # tweets
    for key in data.TWEETS:
        tweets.append(data.TWEETS[key])


        
    is_xhr = True if request.headers.get('spa') else False
    return dict(
        is_xhr=is_xhr,
        title="Twitter",
        user_id=user_id,

        users=users,
        tweets=tweets,

        user_first_name=user_first_name,
        user_last_name=user_last_name,
        user_name=user_name,
        user_profile_picture=user_profile_picture,

        tabs=data.tabs, 
        trends=data.trends,
        items=data.items, 
        )


