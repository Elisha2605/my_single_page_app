import imp
from bottle import get, request, response, view
import json
import data

@get('/signup')
@view('signup')
def _():
    
    error = request.params.get('error')
    user_first_name = request.params.get('user_first_name')
    user_last_name = request.params.get('user_last_name')
    user_email = request.params.get('user_email')
    user_email_exists = request.params.get('user_email_exists')
    user_password = request.params.get('user_password')

    is_fetch = True if request.headers.get('From-Fetch') else False
    page_title = "signup"
    return dict(
        title=page_title,
        is_fetch=is_fetch,

        error = error,
        user_first_name=user_first_name,
        user_last_name=user_last_name,
        user_email=user_email,
        user_email_exists=user_email_exists,
        user_password=user_password
    )

#### test router ###
@get('/users')
def _():

    response.content_type = 'application/json; charset=UTF-8'
    return(json.dumps(dict(users=data.USERS)))