from bottle import get, request, response, view
import data
import json
import re



@get('/users/<tweet_id>')
@view('user-account')
def _(tweet_id):

    try:
        
        return dict(tweets=data.TWEETS[tweet_id])
        
            
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
    