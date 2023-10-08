-- table to store user information
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    -- user profile fields (e.g., Name, Bio, etc.)
);

-- table to store interest tags
CREATE TABLE InterestTags (
    TagID INT AUTO_INCREMENT PRIMARY KEY,
    TagName VARCHAR(255) NOT NULL,
    -- tag-related fields (e.g., Description, Category, etc.)
);

-- table to associate users with interest tags (many-to-many relationship)
CREATE TABLE UserInterestTags (
    UserID INT,
    TagID INT,
    PRIMARY KEY (UserID, TagID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (TagID) REFERENCES InterestTags(TagID)
);

-- table to store club information
CREATE TABLE Clubs (
    ClubID INT AUTO_INCREMENT PRIMARY KEY,
    ClubName VARCHAR(255) NOT NULL,
    Description TEXT,
    -- Other club-related fields (e.g., Location, Membership Fee, etc.)
);

-- table to associate clubs with interest tags (many-to-many relationship)
CREATE TABLE ClubInterestTags (
    ClubID INT,
    TagID INT,
    PRIMARY KEY (ClubID, TagID),
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID),
    FOREIGN KEY (TagID) REFERENCES InterestTags(TagID)
);

-- table to associate users with clubs (many-to-many relationship, for club memberships)
CREATE TABLE UserClubMemberships (
    UserID INT,
    ClubID INT,
    PRIMARY KEY (UserID, ClubID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ClubID) REFERENCES Clubs(ClubID)
);

