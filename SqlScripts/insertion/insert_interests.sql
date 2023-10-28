DELETE FROM interests;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME= 'interests';
INSERT INTO interests (interest_name)
VALUES ('Consulting'), ('Computer Science'), ('Business'), ('Robotics'), ('Sports'), ('Martial Arts'), 
('Motorcycle'), ('Gaming'), ('Music'), ('Engineering');
