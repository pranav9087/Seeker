CREATE TABLE IF NOT EXISTS club (
    club_id int AUTO_INCREMENT PRIMARY KEY, 
    club_name varchar(255),
    interest_id int,

    FOREIGN KEY (interest_id) REFERENCES interests(interest_id)
)