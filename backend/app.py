from flask import Flask,render_template, flash, request
import sqlite3 as sql
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

user_connection = sql.connect('./instance/user.db')
with open('../SqlScripts/users.sql') as f:
    user_connection.executescript(f.read()) # execute the SQL scripts

club_connection = sql.connect('./instance/club.db')
with open('../SqlScripts/club.sql') as f:
    club_connection.executescript(f.read()) # execute the SQL scripts

interest_connection = sql.connect('./instance/interests.db')
with open('../SqlScripts/interests.sql') as f:
    interest_connection.executescript(f.read()) # execute the SQL scripts

user_info_connection = sql.connect('./instance/user_info.db')
with open('../SqlScripts/user_info.sql') as f:
    user_info_connection.executescript(f.read()) # execute the SQL scripts


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
@app.route('/register', methods = ['POST'])
def register():
    status_code = 200
    msg = "success"
    try:
        username = request.form.get("username")
        email_address = request.form.get("email_address")
        user_input_password = request.form.get("password")
        password = hash_password(user_input_password)

        try:
            emailinfo = validate_email(email_address, check_deliverability=True)
            email = emailinfo.normalized
        except EmailNotValidError as e:
            status_code = 400 # status code for invalid email
            msg = "invalid email"

        with sql.connect("./instance/user.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (email,user_name,password) VALUES (?,?,?)",(email,username,password) )
            con.commit()
    except:
        if status_code != 400: # if status code is not 400 but it gives an exception, then that means it is an error related to DB mostly on insertion
            con.rollback()
            status_code = 500
            msg = "Email already used"
    
    finally:
        con.close()
        return msg, status_code
   

@app.route('/login', methods=['GET', 'POST'])
def login():  
    return render_template('login.html', form=form)