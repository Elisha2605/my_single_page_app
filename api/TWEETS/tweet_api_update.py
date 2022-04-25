from bottle import put, response, request
import json
import data
import uuid
import os
import imghdr
import re

##############  TWEETS/<ID> / PUT  ################
@put('/api-tweets/<tweet_id>')
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

        print('#'*100)
        print(tweet_id)
        print(tweet_text)
        
        if len(tweet_text) < data.TWEET_MIN_LEN:
            response.status = 400
            return {'info': f"tweet text must be minimun {data.TWEET_MIN_LEN}"}

        if len(tweet_text) > data.TWEET_MAX_LEN:
            response.status = 400
            return {'info': f"tweet text must be maximum {data.TWEET_MAX_LEN}"}
        
        # Update the tweet

        image = request.files.get('tweet_image')

        if not image:
            data.TWEETS[tweet_id]['tweet_text'] =  tweet_text

        else:
            file_name, file_extension = os.path.splitext(image.filename)
            print(file_name)
            print(file_extension)

            if file_extension not in ('.png', '.jpeg', '.jpg'):
                return 'Image not allowed!'
                
            if file_extension == ".jpg": file_extension = ".jpeg"

            image_id = str(uuid.uuid4())

            image_name = f'{image_id}{file_extension}'

            image_path = f'./static/images/user_content_images/{image_name}'
            image.save(image_path)

            json.dumps(str(image_name))

            imghdr_extension = imghdr.what(image_path)

            if file_extension != f".{imghdr_extension}":
                os.remove(image_path)
                response.status = 400
                return {"info: Invalid image format"}
     
            data.TWEETS[tweet_id]['tweet_text'] =  tweet_text
            data.TWEETS[tweet_id]['tweet_image'] = image_name

    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

    response.content_type = 'application/json; charset=UTF-8'
    return json.dumps(dict(tweet=data.TWEETS[tweet_id], tweet_text=data.TWEETS[tweet_id]['tweet_text']))