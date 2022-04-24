from bottle import get, view, request, response



@get('/user_cover_image_upload')
@view('user-cover-image')
def _():
    try:

        is_fetch = True if request.headers.get('From-Fetch') else False
        page_title = "upload-cover"
        return dict(
            title=page_title,
            is_fetch=is_fetch,
        )
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}