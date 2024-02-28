-- This script creates the database hbtn_0d_usa and the table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- cd/use the database created
USE hbtn_0d_usa;

-- creating the table 'states'andd set id as primary key
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT, name VARCHAR(256), PRIMARY KEY (id));
