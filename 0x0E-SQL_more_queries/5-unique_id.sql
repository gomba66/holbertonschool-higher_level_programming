-- Script that creates a table unique_id with a specific structure.
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256)
);
