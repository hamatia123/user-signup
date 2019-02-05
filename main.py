from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('user_signup.html')

@app.route('/add', methods=['POST'])
def welcome_message():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

  
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    
    if username == "":
        username_error = "Please enter a username."
    else:
        if " " in username: # Username has a space error
            username_error = "Username cannot contain a space."
            username = ""
        else:
            if len(username) < 3: # Username shorter than 3 characters error
                username_error = "Username must be longer than 3 characters."
                username = ""
            else:
                if len(username) > 20: # Username longer than 20 characters error
                    username_error = "Username must be shorter than 20 characters."
                    username = ""

    # Password empty error
    if password == "":
        password_error = "Please enter a password."
    else:
        if " " in password: # Password has a space error
            password_error = "Password cannot contain a space."
        else:
            if len(password) < 3: # Password shorter than 3 characters error
                password_error = "Password must be longer than 3 characters."
            else:
                if len(password) > 20 : # Password longer than 20 characters error
                    password_error = "Password must be shorter than 20 characters."
                else:
                    if password != verify:  # Passwords Matching
                        password_error = "Passwords must match."
                        verify_error = "Passwords must match."

    # Valid Email
    if not email:
        email = ""
    else:
        if "@" not in email:
            email_error = "Please enter a valid email address."
            email = ""
        else:
            if "." not in email:
                email_error = "Please enter a valid email address."
                email = ""
            else:
                if " " in email:
                    email_error = "Valid email addresses cannot have a space."
                    email = ""
                else:
                    if len(email) < 7:
                        email_error = "Valid email addresses must be longer than 7 characters."
                        email = ""
                    else:
                        if len(email) > 20:
                            email_error = "Valid email addresses must be shorter than 20 characters."
                            email = ""

    
    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username, password = password, verify = verify, email = email)
    else:
        return render_template('user_signup.html', username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error, username = username, email = email)

app.run()