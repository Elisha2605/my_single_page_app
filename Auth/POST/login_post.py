from bottle import post, request, redirect
import data
import uuid
import re


@post('/login')
def _():
   
    # VALIDATION
    if not request.forms.get("user_email"):
        return redirect("/login?error=user_email")
    if not re.match(data.REGEX_EMAIL, request.forms.get("user_email")):
        return redirect("/login?error=user_email")

    user_email = request.forms.get("user_email")
    user_password = request.forms.get("user_password")

    if not request.forms.get("user_password"):
        return redirect(f"/login?error=user_passowrd&user_email={user_email}")
    if not 2 <= len(user_password) <= 30:
        return redirect(f"/login?error=user_password&user_email={user_email}")

    # Connect to the db
    # Login User
    for key in data.USERS:
        user_id = key
        if request.forms.get("user_email") in data.USERS[key]['user_email']:
            if request.forms.get("user_password") in data.USERS[key]['user_password']:
                
                return redirect(f'/{user_id}')
            else: 
                return redirect(f"/login?error=user_password&user_email={user_email}")

    # Login Admin
    if request.forms.get("user_email") == data.ADMIN['admin_email']:
        if request.forms.get('user_password') == data.ADMIN['admin_password']:

            return redirect('/admin-page')
        else:
            return redirect(f"/login?error=user_password&user_email={user_email}")

    # response.status = 200
    
    return redirect("/login?error=user_email")