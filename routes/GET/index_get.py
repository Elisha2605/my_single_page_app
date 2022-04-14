from bottle import get, view, request, response
import data



##############  Home  ################
@get('/<user_id>')
@view('index')
def _(user_id):

    ## info for the home (index)
    user_first_name=data.USERS[user_id]['user_first_name']
    user_last_name=data.USERS[user_id]['user_last_name']
    user_name=data.USERS[user_id]['user_name']
    user_profile_picture=data.USERS[user_id]['user_profile_picture']

    

    # profile_picture_login

        
    is_fetch = True if request.headers.get('From-Fetch') else False
    return dict(
        title="Twitter",
        is_fetch=is_fetch,

        user_id=user_id,

        user_first_name=user_first_name,
        user_last_name=user_last_name,  
        user_name=user_name,
        user_profile_picture=user_profile_picture,

        tabs=data.tabs, 
        trends=data.trends,
        items=data.items, 
        )

