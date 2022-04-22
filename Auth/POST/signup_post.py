from bottle import post, request, redirect, response
import uuid
import data
import re
import os
import imghdr
import json

@post('/signup')
def _():
    # VALIDATION
    if not request.forms.get('user_first_name'):
        return redirect('/signup?error=user_first_name')

    if not request.forms.get('user_last_name'):
        return redirect('/signup?error=user_last_name')

    if not re.match(data.REGEX_EMAIL, request.forms.get('user_email')): 
        return redirect('/signup?error=user_email') 

    if not request.forms.get('user_password'):
        return redirect('/signup?error=user_password')

    user_id =  str(uuid.uuid4())
    user_first_name = request.forms.get('user_first_name')
    user_last_name = request.forms.get('user_last_name')
    user_email = request.forms.get('user_email')
    user_password = request.forms.get('user_password')

    # check if email alredy exists    
    for id in data.USERS:
        if data.USERS[id]['user_email'] == request.forms.get('user_email'):
            return redirect(f'/signup?error=user_email_exists&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}') 
        
    # check the password max and min and put back values into fields if error
    if len(request.forms.get('user_password')) < 2:
        return redirect(f'/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}')
    
    if len(request.forms.get('user_password')) > 50:
        return redirect(f'/signup?error=user_password&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}') 

 ##################################################  IMAGE ######################################################
     # Tweet without image
    image = request.files.get('user_profile_picture')
    if not image:
       data.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": f'{user_first_name}{user_last_name}',
            "user_email": user_email, 
            "user_password":user_password,
            "user_profile_picture": "",
            "user_signup_date": data.SIGNUP_DATE
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
        image_path = f'./static/images/user_profile_pictures/{image_name}'
        image.save(image_path)

        # Converting the image to json object - str
        json.dumps(str(image_name))

        imghdr_extension = imghdr.what(image_path)

        if file_extension != f".{imghdr_extension}":
            os.remove(image_path)
            response.status = 400
            return {"info: Invalid image format"}
            

        # Converting the image to json object - str
        

########################################################################################################
        # Tweet with image
        data.USERS[user_id] = {
            "user_id": user_id,
            "user_first_name": user_first_name,
            "user_last_name": user_last_name,
            "user_name": f'{user_first_name}{user_last_name}',
            "user_email": user_email, 
            "user_password":user_password,
            "user_profile_picture": image_name,
            "user_signup_date": data.SIGNUP_DATE
        }

    response.status = 200
    return redirect('/login')