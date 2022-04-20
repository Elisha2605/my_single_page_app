from bottle import get, view, request



@get('/')
@view('index')
def _():

    is_fetch = True if request.headers.get('From-Fetch') else False
    return dict(
        title="Welcome to Twitter",
        is_fetch=is_fetch,
        )