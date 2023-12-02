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
    takes structure like this: [(e1, ), (e2, ), (e3, ), ......]
    returns {e1, e2, e3, ...}
"""
def parse_db_return_tuple(lst_tuples, currentUserEmail):
    return_set = set()
    for i in range(len(lst_tuples)):
        if lst_tuples[i][0] != currentUserEmail:
            return_set.add(lst_tuples[i][0])
    return return_set


@app.route("/findSimilarUsers", methods = ['POST'])
def findSimilarUsers():
    status_code = 200
    email_set = set()
    try:
        email = request.get_json()['email']
        with sql.connect('./instance/seeker.db') as con:
            cur = con.cursor()
            res = cur.execute("SELECT interest_1, interest_2, interest_3 FROM user_interest WHERE email = ?", (email, ))
            interest_id1, interest_id2, interest_id3 = res.fetchone() # could be null in there
            if interest_id1 != None:
                res = cur.execute("SELECT email FROM user_interest WHERE interest_1 = ? OR interest_2 = ? OR interest_3 = ?", (interest_id1, interest_id1, interest_id1))
                if res is not None:
                    email_set.update(parse_db_return_tuple(res.fetchall(), email))
            if interest_id2 != None:
                res = cur.execute("SELECT email FROM user_interest WHERE interest_1 = ? OR interest_2 = ? OR interest_3 = ?", (interest_id2, interest_id2, interest_id2))
                if res is not None:
                    email_set.update(parse_db_return_tuple(res.fetchall(), email))
            if interest_id3 != None:
                res = cur.execute("SELECT email FROM user_interest WHERE interest_1 = ? OR interest_2 = ? OR interest_3 = ?", (interest_id3, interest_id3, interest_id3))
                if res is not None:
                    email_set.update(parse_db_return_tuple(res.fetchall(), email))

    except:
        status_code = 500
    finally:
        con.close()
        return {"user_list": list(email_set)}, status_code

@app.route('/updateClubs', methods=['POST'])
def update_clubs():
    status_code = 200
    try:
        email = request.get_json()['email']
        clubs_in_json = request.get_json()['clubs']
        club1 = clubs_in_json['club1']
        club2 = clubs_in_json['club2']
        club3 = clubs_in_json['club3']
        with sql.connect('./instance/seeker.db') as con:
            cur = con.cursor()
            cur.execute("UPDATE user_interest SET club_1 = ?, club_2 = ?, club_3 = ? WHERE email = ?", (club1, club2, club3, email))
            con.commit()
    except Exception as e:
        con.rollback()
        status_code = 500  # Internal Server Error
    finally:
        con.close()
        return "updated successful", status_code
       


@app.route("/pickInterests", methods = ['POST'])
def pickInterests():
    status_code = 200
    msg = "OK"
    try:
        interests_in_json = request.get_json()['interests'] # ideally got 3 from dropdowns
        email_in_json = request.get_json()['currentUser']
        interest1 = interests_in_json['interest1']
        interest2 = interests_in_json['interest2']
        interest3 = interests_in_json['interest3']
        email = email_in_json['email']
        with sql.connect('./instance/seeker.db') as con:
            cur = con.cursor()
            res = cur.execute("SELECT interest_id FROM interests WHERE interest_name = ? OR interest_name = ? OR interest_name = ?", (interest1, interest2, interest3))
            interest_id_list = [interest_ids[0] for interest_ids in res.fetchall()]
            for i in range(len(interest_id_list)):
                id = i + 1
                res = cur.execute(f"UPDATE user_interest SET interest_{id} = ? WHERE email = ?", (interest_id_list[i], email))
            con.commit()
    except:
        con.rollback()
        status_code = 500
        msg = "DB Error"

    finally:
        con.close()
        return msg, status_code

"""
    route for selecting 3 interests and find a list of relevant clubs
"""
@app.route('/home', methods = ['POST'])
def home():
    status_code = 200
    return_dict={"clubname1": "", "clubname2": "", "clubname3": ""}
    try:
        interests_in_json = request.get_json() 
        interest1 = interests_in_json['interest1']
        interest2 = interests_in_json['interest2']
        interest3 = interests_in_json['interest3']
        with sql.connect('./instance/seeker.db') as con:
            cur = con.cursor()
            res = cur.execute("SELECT club_name FROM club INNER JOIN interests ON club.interest_id = interests.interest_id WHERE interest_name = ? OR interest_name = ? OR interest_name = ?", (interest1, interest2, interest3))
            club_list = [clubs[0] for clubs in res.fetchall()]
    except:
        status_code = 500 # db error
    finally:
        con.close()
        for i in range(len(club_list)):
            return_dict["clubname" + str(i+1)] = club_list[i]
        return return_dict, status_code
    
"""
    route for selecting 3 interests and find a list of similar users
"""
@app.route('/findSimilarUsersWithInterests', methods = ['POST'])
def findSimilarUsersWithInterests():
    status_code = 200
    user_email_set = set()
    try:
        interests_in_json = request.get_json()['interests']
        interest1 = interests_in_json['interest1']
        interest2 = interests_in_json['interest2']
        interest3 = interests_in_json['interest3']
        email = request.get_json()['currentUser']['email']
        with sql.connect('./instance/seeker.db') as con:
            cur = con.cursor()
            interest_id_res = cur.execute("SELECT interest_id FROM interests WHERE interest_name = ? OR interest_name = ? OR interest_name = ?", (interest1, interest2, interest3))
            interest_id_lst  = [iid[0] for iid in interest_id_res.fetchall()]
            for i in range(len(interest_id_lst)):
                cur_iid = interest_id_lst[i]
                user_res = cur.execute("SELECT email FROM user_interest WHERE interest_1 = ? OR interest_2 = ? OR interest_3 = ?", (cur_iid, cur_iid, cur_iid))
                if user_res is not None:
                    lst_of_tuples = user_res.fetchall()
                    return_set = parse_db_return_tuple(lst_of_tuples, email)
                    user_email_set.update(return_set)
                    
    except:
        status_code = 500 # db error
    finally:
        con.close()
        return {"user_list": list(user_email_set)}, status_code

"""
    route for registering new users; responsible for adding user information into the database
"""
@app.route('/register', methods = ['POST'])
def register():
    status_code = 200
    return_dict = {}
    try:
        username = request.form.get("username")
        email_address = request.form.get("email_address")
        user_input_password = request.form.get("password")
        password = hash_password(user_input_password)
        return_dict["username"] = username
        return_dict["email"] = email_address
        try:
            emailinfo = validate_email(email_address, check_deliverability=True)
            email = emailinfo.normalized

        except EmailNotValidError as e:
            status_code = 400 # status code for invalid email

        with sql.connect("./instance/seeker.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users (email,user_name,password) VALUES (?,?,?)",(email,username,password))
            con.commit()
            cur.execute("INSERT INTO user_interest (email,interest_1, interest_2, interest_3, club_1, club_2, club_3) VALUES (?,?,?,?,?,?,?)", (email, None, None, None, None, None, None))
            con.commit()
    except:
        if status_code != 400: # if status code is not 400 but it gives an exception, then that means it is an error related to DB mostly on insertion
            con.rollback()
            status_code = 500
    
    finally:
        con.close()
        return return_dict, status_code
   

@app.route('/login', methods=['POST'])
def login():
    status_code = 200
    email_address = request.form.get("email_address")
    user_input_password = request.form.get("password")
    username = ""
    try:
        with sql.connect("./instance/seeker.db") as con:
            cur = con.cursor()
            res = cur.execute("SELECT user_name, password FROM users WHERE email = ?", (email_address, ))
            if res is not None:
                username, query_pw = res.fetchone()
                if not check_password_hash(query_pw, user_input_password):
                    status_code = 401
    except:
        status_code = 500
    finally:
        con.close()
        return {"username": username, "email": email_address}, status_code