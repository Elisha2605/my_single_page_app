from bottle import get, request, response, redirect
import data


####################  Logout / GET  ######################
@get('/logout')
def _():
    try:
        user_session_jwt = request.get_cookie("jwt")
        data.SESSION.remove(user_session_jwt)
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}