CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    email_address TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL
);