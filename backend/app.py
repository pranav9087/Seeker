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

"""
    route for selecting 3 interests and find a list of relevant clubs
"""
@app.route('/home', methods = ['GET'])
def home():
    return_json  = {}
    try:
        interests_in_json = request.form.get('interests') # 'interest1': "", ....
        interest1 = interests_in_json['interest1']
        interest2 = interests_in_json['interest2']
        interest3 = interests_in_json['interest3']
        with sql.connect("./instance/database.db") as con:
           cur = con.cursor()
           res = cur.execute("SELECT club_name FROM club INNER JOIN interests ON interest_id WHERE interest_name = ? OR interest_name = ? OR interest_name = ?", (interest1, interest2, interest3))
           [(clubname1, ), (clubname2, ), (clubname3, )] = res.fetchall()
        return_json["clubname1"] = clubname1
        return_json["clubname2"] = clubname2
        return_json["clubname3"] = clubname3
    except sql.Error as err:
        print(err)
    finally:
       con.close()
       return return_json
  
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
            cur.execute("INSERT INTO users (email,user_name,password) VALUES (?,?,?)",(email,username,password) )
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