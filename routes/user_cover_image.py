from bottle import get, view, request, response, redirect
import data
import jwt


@get('/user_cover_image_upload')
@view('user-cover-image')
def _():

    try:
        user_session_jwt = request.get_cookie("jwt_user")
        if user_session_jwt not in data.SESSION:
            return redirect("/login") 
        
        for session in data.SESSION:
            if session == user_session_jwt:
                jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])
        
        user_id = jwt_user['jwt_user_id']

        is_fetch = True if request.headers.get('From-Fetch') else False
        page_title = "upload-cover"
        return dict(
            title=page_title,
            is_fetch=is_fetch,

            jwt_user=jwt_user,
            user_id=user_id
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}