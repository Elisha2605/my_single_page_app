from bottle import error, default_app, get, run, static_file, view


########  AUTH  #######
from Auth.GET import (
    signup_get,
    login_get,
    logout_get
)

from Auth.POST import (
    signup_post,
    login_post
)

########  ROUTES  #######
from routes import (
    home,
    index,
    tweets_get,
    user_account,
    user_profile,
    admin,
    user_cover_image
)
########  APIs  #######
from api.TWEETS import (
    tweets_api_get,
    tweet_api_delete,
    tweet_api_post,
    tweet_api_update,
)
from api.USERS import (
    user_api_get,
    user_api_upload_cover_img
)



#######  STATIC FILES  #######
@get('/app.css')
def _():
    return static_file('app.css', root='.')

@get('/static/<file_name:path>')
def _(file_name):
    return static_file(file_name, root="./static")

#######  404  #######
@error(404)
@view('404')
def _(error):
    print(error)
    return 





##########################################################################################
try:
  # Production
  import production

  application = default_app
except:
  # Developement
  run(host='127.0.0.1', port=8080, reloader=True, debug=True, server='paste')