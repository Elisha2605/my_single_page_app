from bottle import get, view, request, response


@get('/login')
@view('login')
def _():
    try:
        error = request.params.get('error')
        user_email = request.params.get('user_email')
        user_password = request.params.get('user_password')
        
        is_fetch = True if request.headers.get('From-Fetch') else False
        page_title = "login"


        return dict(
            title=page_title,
            is_fetch=is_fetch,

            error=error,
            user_email=user_email,
            user_password=user_password
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}