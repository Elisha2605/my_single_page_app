from bottle import post, response, request, put, redirect
import data
import os
import uuid
import json
import imghdr
import jwt

##############  User upload cover image/ POST  ################
@put('/api-user-upload-cover/<user_id>')
def _(user_id):

    user_session_jwt = request.get_cookie("jwt_user")
    if user_session_jwt not in data.SESSION:
        return redirect("/login") 
        
    for session in data.SESSION:
        if session == user_session_jwt:
            jwt_user = jwt.decode(session, data.JWT_USER_SECRET, algorithms=["HS256"])

    image = request.files.get('user_cover_image')
    file_name, file_extension = os.path.splitext(image.filename)
    print(file_name)
    print(file_extension)

    if file_extension not in ('.png', '.jpeg', '.jpg'):
        return 'Image not allowed!'
        
    if file_extension == ".jpg": file_extension = ".jpeg"

    image_id = str(uuid.uuid4())
    image_name = f'{image_id}{file_extension}'

    image_path = f'./static/images/user_cover_image/{image_name}'
    image.save(image_path)

    json.dumps(str(image_name))
    imghdr_extension = imghdr.what(image_path)

    if file_extension != f".{imghdr_extension}":
        os.remove(image_path)
        response.status = 400
        return {"info: Invalid image format"}


    data.USERS[user_id]['user_cover_image'] = image_name

    user_id = jwt_user['jwt_user_id']

    response.status = 200
    return dict(
                image_cover_image=image_name,
                user_id=user_id,
                jwt_user=jwt_user
            )