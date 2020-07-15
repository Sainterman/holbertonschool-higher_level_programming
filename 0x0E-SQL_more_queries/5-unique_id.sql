-- script that creates the table unique_id on your MySQL server.
-- unique_id: int with default value 1 must be unique
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
