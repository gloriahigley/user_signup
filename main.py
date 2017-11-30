from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True
        

@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or ' ' in username: 
        username_error = "Please enter a valid username with no spaces"
    else:
        if len(username) < 3 or len(username) > 20:
            username_error = "Please enter a username > than 3 characters and < 20 characters"

    if password == "" or ' ' in password:
        password_error = "Please enter a valid password with no spaces"
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = "Please enter a password > 3 characters and < than 20 characters"  

    if verify == "" or verify != password:
        verify_error = "Passwords must match"
    
    while email == "":
        break    
    else:
        if (' ' in email) or (email.count("@") < 1 or email.count("@") > 1) or (email.count(".") < 1 or email.count(".") > 1):
            email_error = "Please enter a valid email with one '@', ',' and no spaces"
        if len(email) < 3 or len(email) > 20:
                email_error = "Please enter an email with > 3 characters and < than 20 characters" 

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('greeting.html', username=username) 
    else:
        return render_template('form.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/welcome")  
def welcome():
    return render_template('greeting.html')        
     
@app.route("/")
def index():
    return render_template('form.html')
   

app.run()
