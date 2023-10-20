CREATE TABLE IF NOT EXISTS user_interest (
    email varchar(255),
    interest_1 int, 
    interest_2 int,
    interest_3 int, 
    club_1 int,
    club_2 int,
    club_3 int,

    FOREIGN KEY (email) REFERENCES users(email),
    FOREIGN KEY (interest_1) REFERENCES interests(interest_id),
    FOREIGN KEY (interest_2) REFERENCES interests(interest_id),
    FOREIGN KEY (interest_3) REFERENCES interests(interest_id),
    FOREIGN KEY (club_1) REFERENCES club(club_id),
    FOREIGN KEY (club_2) REFERENCES club(club_id),
    FOREIGN KEY (club_3) REFERENCES club(club_id)
)