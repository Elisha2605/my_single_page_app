import imp
from bottle import get, request, redirect
import data


##############  Logout  ################
@get('/logout')
def _():

    user_session_jwt = request.get_cookie('user')
    data.SESSIONS.remove(user_session_jwt)

    return redirect("/login")