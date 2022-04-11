from bottle import get, view, request, response, redirect
import data
import jwt


##############  Home  ################
@get('/<user_id>')
@view('index')
def _(user_id):

    try: 
        
        # decode session
        user_session_jwt = request.get_cookie('user')

        if user_session_jwt not in data.SESSIONS:
            return redirect("/login")

        for session in data.SESSIONS:
            if session == user_session_jwt:
                user = jwt.decode(session, "secret", algorithms=["HS256"])
            
        if not user_id in user['user_id']:
            return 


        ## info for the home (index)
        user_first_name=data.USERS[user_id]['user_first_name']
        user_last_name=data.USERS[user_id]['user_last_name']
        user_name=data.USERS[user_id]['user_name']
        user_profile_picture=data.USERS[user_id]['user_profile_picture']

        

        # profile_picture_login

            
        is_xhr = True if request.headers.get('spa') else False
        return dict(
            is_xhr=is_xhr,
            title="Twitter",
            user_id=user_id,
            users=data.USERS[user_id],

            user_first_name=user_first_name,
            user_last_name=user_last_name,  
            user_name=user_name,
            user_profile_picture=user_profile_picture,

            tabs=data.tabs, 
            trends=data.trends,
            items=data.items, 


            user=user
            )

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

