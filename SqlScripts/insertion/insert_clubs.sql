DELETE FROM club;
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME= 'club';
INSERT INTO club (club_name, interest_id)
VALUES ('Illinois Business Consulting', 1), ('Illinois Consulting Group', 1), 
('Students Consulting for Non-Profit Organizations', 1), ('Champaign-Urbana Business and Engineering Consulting', 1),
('Founders', 2), 
('ACM', 2),
('ZeroToOne', 2),
('D-Lab', 3),
('Illini Solar Car', 4),
('Illinois Business Council', 3),
('IlliniEV', 4), 
('Alpha Kappa Psi', 3),
('Phi Gamma Nu', 3), 
('Delta Sigma Pi', 3), 
('OTCR', 1),
('Badminton For Fun', 5),
('Illini Wushu', 6), 
('Illini Motorcycle Club', 7),
('Social Gaming Club', 8), 
('Hip-Hop Collective', 9),
('Engineering Council', 10);
