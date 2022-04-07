from turtle import title
from bottle import get, view, request, response
import data



##############  Home  ################
@get('/<user_id>')
@view('index')
def _(user_id):

    # users
    for user_id in data.USERS:
        users = data.USERS[user_id]
        print('#'*100)
        print(users)
    
    # tweets
    for key in data.TWEETS:
        tweets = data.TWEETS[key]


        
    is_xhr = True if request.headers.get('spa') else False
    return dict(
        is_xhr=is_xhr,
        title="Twitter",

        users=users,
        tweets=tweets,

        tabs=data.tabs, 
        trends=data.trends,
        items=data.items, 
        )
