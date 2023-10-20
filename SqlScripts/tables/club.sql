CREATE TABLE IF NOT EXISTS club (
    club_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    club_name varchar(255),
    interest_id int,

    FOREIGN KEY (interest_id) REFERENCES interests(interest_id)
)