from bottle import post, request, redirect, response
import data
import uuid
import re


@post('/login')
def _():

    # VALIDATION
    if not request.forms.get("user_email"):
        response.statis = 400
        return redirect("/login?error=user_email")
    if not re.match(data.REGEX_EMAIL, request.forms.get("user_email")):
        response.statis = 400
        return redirect("/login?error=user_email")  
    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")  
    if not request.forms.get("user_password"):
        response.statis = 400
        return redirect(f"/login?error=user_passowrd&user_email={user_email}")
    if not 2 <= len(user_password) <= 30:
        response.statis = 400
        return redirect(f"/login?error=user_password&user_email={user_email}")  

    # Login User
    for key in data.USERS:
        user_id = key
        if request.forms.get("user_email") in data.USERS[key]['user_email']:
            if request.forms.get("user_password") in data.USERS[key]['user_password']:
                response.statis = 200
                return redirect(f'/{user_id}')
            else: 
                response.statis = 400
                return redirect(f"/login?error=user_password&user_email={user_email}")  
    # Login Admin
    if request.forms.get("user_email") == data.ADMIN['admin_email']:
        if request.forms.get('user_password') == data.ADMIN['admin_password']:
            response.statis = 200
            return redirect('/admin-page')
        else:
            response.statis = 400
            return redirect(f"/login?error=user_password&user_email={user_email}")  
    

    return redirect("/login?error=user_email")  