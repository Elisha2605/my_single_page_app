from bottle import get, view, request


@get('/login')
@view('login')
def _():
    
    error = request.params.get('error')
    user_email = request.params.get('user_email')
    user_password = request.params.get('user_password')
    
    return dict(
        error=error,
        user_email=user_email,
        user_password=user_password
    )