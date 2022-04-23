from bottle import post, response, request
import json
import data
import uuid
from datetime import datetime
import os
import imghdr
import re


##############  TWEETS with and without image / POST  ################
@post('/api-tweets/<user_id>')
def _(user_id):

    try:
        tweet_id = str(uuid.uuid4())
        # Validate uuid
        if not re.match(data.REGEX_UUID4, tweet_id):
            response.status = 204
            return

        # Validate tweet
        if not request.forms.get('tweet_text'):
            response.status = 400
            return {"info": "tweet_text missing"}
        
        tweet_text = request.forms.get('tweet_text').strip()
        
        if len(tweet_text) < data.TWEET_MIN_LEN:
            response.status = 400
            return {'info': f"tweet description must be minimun {data.TWEET_MIN_LEN}"}

        if len(tweet_text) > data.TWEET_MAX_LEN:
            response.status = 400
            return {'info': f"tweet description must be maximum {data.TWEET_MAX_LEN}"}

       # upload
        ##################################################  IMAGE  ######################################################
        # Upload image
        image = request.files.get('tweet_image')

        # tweet without image
        if not image:
            data.TWEETS[tweet_id] = {
                    "tweet_id": tweet_id,
                    'user_id': user_id,
                    'user_first_name': data.USERS[user_id]['user_first_name'],
                    'user_last_name': data.USERS[user_id]['user_last_name'],
                    'user_name': data.USERS[user_id]['user_name'],
                    'user_profile_picture': data.USERS[user_id]['user_profile_picture'],
                    'tweet_text': tweet_text,
                    'tweet_time': data.TWEET_TIME
                    }
        else:
            file_name, file_extension = os.path.splitext(image.filename)  # .pn .jpeg .zip .mp4
            print(file_name)
            print(file_extension)

            # Validation
            if file_extension not in ('.png', '.jpeg', '.jpg'):
                return 'Image not allowed!'

            # overwrite jpg to jpeg so imghdr will pass validation
            if file_extension == ".jpg": file_extension = ".jpeg"

            image_id = str(uuid.uuid4())
            # Create new image name
            image_name = f'{image_id}{file_extension}'

            # Save the image
            image_path = f'./static/images/user_content_images/{image_name}'
            image.save(image_path)

            # Converting the image to json object - str
            json.dumps(str(image_name))

            # Make sure that the image is actually a valid image
            # by reading its mime type
            print("imghdr.what", imghdr.what(image_path))   # imghdr.what png
            print("file_extension", file_extension)                     # file_extension .png
            imghdr_extension = imghdr.what(image_path)
            
            if file_extension != f".{imghdr_extension}":
                print("mmm... suspicious ... it is not really an image")
                # remove the invalid image from the folder
                os.remove(image_path)
                return "mmm... got you! It was not an image"

            ########################################################################################################

            # tweet with image
            if user_id in data.USERS:
                data.TWEETS[tweet_id] = {
                    "tweet_id": tweet_id,
                    'user_id': user_id,
                    'user_first_name': data.USERS[user_id]['user_first_name'],
                    'user_last_name': data.USERS[user_id]['user_last_name'],
                    'user_name': data.USERS[user_id]['user_name'],
                    'user_profile_picture': data.USERS[user_id]['user_profile_picture'],
                    'tweet_text': tweet_text,
                    'tweet_image': image_name,
                    'tweet_time': data.TWEET_TIME
                    }
                response.status = 201
                
            else:
                return "Wrong user ID"        
        
    except Exception as ex:
        print(ex)
        response.status = 500
        return {'info': 'Upps... something went wrong'}

    return json.dumps(dict(tweet=data.TWEETS[tweet_id]))