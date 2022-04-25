from bottle import get, request, response, view
import data
import random


##############  USERS / GET  #################### 
@get('/api-users-tweets/<tweet_id>')
def _(tweet_id):

    try:
        return dict(tweets=data.TWEETS[tweet_id])
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

##############  USERS/you may like / GET  #################### 
@get('/api-users-you-might-like')
def _():

    try:
        for key in data.USERS:
            keys = random.sample(list(data.USERS), 3)

        return dict(random_users=keys)   

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}
