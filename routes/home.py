from bottle import get, view, request, response, redirect
import data
import random
import jwt

##############  Home  ################
@get('/<user_id>')
@view('home')
def _(user_id):

    try:
        # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])
        

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

        # random users
        users = []
        for key in data.USERS:
            users_dict = data.USERS
            users.append(users_dict[key])
            random_users = [random.choice(list(users)) for i in range(4)]
            
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

            random_users=random_users,
            jwt_user=jwt_user
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}