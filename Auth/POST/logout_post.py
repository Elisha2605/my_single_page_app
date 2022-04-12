from bottle import get, request, redirect, response
import data


##############  Logout  ################
@get('/logout')
def _():

    print('#before'*30)
    print(data.SESSIONS)

    user_session_jwt = request.get_cookie('user')
    data.SESSIONS.remove(user_session_jwt)

    print('#after'*30)
    print(data.SESSIONS)
    
    return redirect("/login")



