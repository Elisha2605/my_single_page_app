from bottle import get, response, request, redirect
import data
import os
import uuid
import json
import imghdr
import jwt


@get('/api-jwt-user')
def _():
    try:
         # SESSSION
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

        response.status = 200
        return dict(jwt_user=jwt_user) 
                

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}