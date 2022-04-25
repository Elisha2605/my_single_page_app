from bottle import get, request, response, redirect
import data


####################  Logout User / GET  ######################
@get('/logout')
def _():

    user_session_jwt = request.get_cookie("jwt_user")
    data.SESSION.remove(user_session_jwt)
    return redirect('/login')

####################  Logout Admin / GET  ######################
@get('/logout-admin')
def _():

    admin_session_jwt = request.get_cookie("jwt_admin")
    data.SESSION.remove(admin_session_jwt)

    return redirect('/login')