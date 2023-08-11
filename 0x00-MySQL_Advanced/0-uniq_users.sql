-- Drop a table users if exists to allow to create new table
-- create new table users;
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users(id INTEGER NOT NULL AUTO_INCREMENT,email CHAR(255) NOT NULL UNIQUE,name CHAR(255), PRIMARY KEY(ID));

