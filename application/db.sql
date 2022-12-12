CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    email_address VARCHAR(50) NOT NULL,
    password_hash VARCHAR(60) NOT NULL,
    outstanding_questions VARCHAR(1024),
    completed_questions VARCHAR(1024),
    log MEDIUMTEXT NOT NULL
);
