from bottle import delete, response
import data
import re




##############  TWEETS/<ID> / DELETE  ################
@delete('/tweets/<tweet_id>')
def _(tweet_id):
    try:
        if not re.match(data.REGEX_UUID4, tweet_id):
            response.status = 204
            return
        if tweet_id not in data.TWEETS:
            response.status = 204
            return
        
        data.TWEETS.pop(tweet_id)
        return {'info': "tweet deleted"}
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}