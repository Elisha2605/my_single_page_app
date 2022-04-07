from turtle import title
from bottle import error, get, post, request, response, run, static_file, view

##############################
@error(404)
def _(error):
  return "Page Not fount"
##############################
@get('/app.css')
def _():
    return static_file('app.css', root='.')
##############################
@get('/app.js')
def _():
    return static_file('app.js', root='.')
##############################
@get('/test.js')
def _():
    return static_file('test.js', root='.')
##############################
@get('/spa.js')
def _():
    return static_file('spa.js', root='.')
##############################
@get("/validator.js")
def _():
  return static_file("validator.js", root=".")
##############################
@get("/images/user_profile_pictures/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images/user_profile_pictures")
##############################
@get("/images/user_content_images/<image_name>")
def _(image_name):
  return static_file(image_name, root="./images/user_content_images")




##############################
@get('/')
@view('index')
def _():
    is_xhr = True if request.headers.get('spa') else False
    return dict(title="APP", is_xhr=is_xhr)

##############################

########  GET  ########
from routes.GET import  index_get
from routes.GET import tweets_get
from routes.GET import user_get
########  POST  #######


########  UPDATE  #######
from routes.PUT import tweet_update
from routes.POST import tweet_post


########  DELETE  #######
from routes.DELETE import tweet_delete




########  AUTH  #######
# GET
from Auth.GET import signup_get
from Auth.GET import login_get
# POST
from Auth.POST import signup_post
from Auth.POST import login_post



##########################################################################################
run(host='127.0.0.1', port=8080, reloader=True, debug=True, server='paste')