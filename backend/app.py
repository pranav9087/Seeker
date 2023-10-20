from flask import Flask,render_template, flash, request
import sqlite3 as sql
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from email_validator import validate_email, EmailNotValidError
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db_connection = sql.connect('./instance/seeker.db')
tables_scripts_directory = "../SqlScripts/tables"
insertion_scripts_directory = "../SqlScripts/insertion"

"""
    reads all sql scripts and populate the database
"""
for filename in os.listdir(tables_scripts_directory):
    with open(os.path.join(tables_scripts_directory, filename)) as f:
        db_connection.executescript(f.read())
for filename in os.listdir(insertion_scripts_directory):
    with open(os.path.join(insertion_scripts_directory, filename)) as f:
        db_connection.executescript(f.read())

db_connection.close() # close db connection for each use for safety

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
    return_dict  = {}
    status_code = 200
    msg = "Success"
    try:
        interests_in_json = request.form.get('interests') # 'interest1': "", ....
        interest1 = interests_in_json['interest1']
        interest2 = interests_in_json['interest2']
        interest3 = interests_in_json['interest3']
        with sql.connect("./instance/seeker.db") as con:
           cur = con.cursor()
           res = cur.execute("SELECT club_name FROM club INNER JOIN interests ON interest_id WHERE interest_name = ? OR interest_name = ? OR interest_name = ?", (interest1, interest2, interest3))
           [(clubname1, ), (clubname2, ), (clubname3, )] = res.fetchall()
        return_dict["clubname1"] = clubname1
        return_dict["clubname2"] = clubname2
        return_dict["clubname3"] = clubname3
    except:
        status_code = 500 # db error
    finally:
       con.close()
       return return_dict, status_code
  
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

        with sql.connect("./instance/seeker.db") as con:
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