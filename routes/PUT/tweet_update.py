from bottle import put, response, request
import data
import re
import json


##############  TWEETS/<ID> / PUT  ################
@put('/tweets/<tweet_id>')
def _(tweet_id):
    try: 
        # Validate id
        if not re.match(data.REGEX_UUID4, tweet_id):
            response.status = 204
            return
        if  tweet_id not in data.TWEETS:
            response.status = 204
            return 

        # validate tweet_text
        if not request.forms.get('tweet_text'):
            response.status = 400
            return {"info": "tweet_text missing"}
        
        tweet_text = request.forms.get('tweet_text').strip()
        tweet_image = request.forms.get('tweet_image')
        
        if len(tweet_text) < data.TWEET_MIN_LEN:
            response.status = 400
            return {'info': f"tweet text must be minimun {data.TWEET_MIN_LEN}"}

        if len(tweet_text) > data.TWEET_MAX_LEN:
            response.status = 400
            return {'info': f"tweet text must be maximum {data.TWEET_MAX_LEN}"}
        
        # Update the tweet
        
        if request.forms.get('tweet_image'):
            data.TWEETS[tweet_id]['tweet_text'] = tweet_text
            data.TWEETS[tweet_id]['tweet_image'] = tweet_image
        else:
            data.TWEETS[tweet_id]['tweet_text'] = tweet_text


    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

    response.content_type = 'application/json; charset=UTF-8'
    return json.dumps(dict(tweet=data.TWEETS[tweet_id], tweet_text=data.TWEETS[tweet_id]['tweet_text']))