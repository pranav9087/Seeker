from flask import Flask,render_template, flash, request
import sqlite3 as sql
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError



app = Flask(__name__)

connection = sql.connect('./instance/database.db')
with open('schema.sql') as f:
    connection.executescript(f.read()) # execute the SQL scripts

"""
a function that hashes the password
"""
def hash_password(password):
    return generate_password_hash(password)
    
"""
a function that checks if the hashed_password matches with the input password
"""
def check_password(password):
    hashed_password = hash_password(password)
    return check_password_hash(hashed_password, password)


@app.route('/')
def index():
    return render_template('index.html')

"""
    route for registering new users; responsible for adding user information into the database
"""
@app.route('/register', methods = ['POST','GET'])
def register():
    if request.method == 'POST':
      try:
         username = request.form['username']
         email_address = request.form['email_address']
         user_input_password = request.form['password']
         password = hash_password(user_input_password)

         try:
            emailinfo = validate_email(email_address, check_deliverability=True)
            email = emailinfo.normalized
         except EmailNotValidError as e:
            msg = "Email is Invalid"

         with sql.connect("./instance/database.db") as con:
            cur = con.cursor()
            msg = "email_address already used, Please try another email"
            cur.execute("INSERT INTO users (username,email_address,password) VALUES (?,?,?)",(username,email,password) )
            con.commit()
            msg = "Registration Successful! You can login now"
      except:
         con.rollback()
      
      finally:
         return render_template("index.html", msg = msg)
         con.close()
    else:
       return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():  
    return render_template('login.html', form=form)