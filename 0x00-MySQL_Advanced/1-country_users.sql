-- 1-country_users.sql
-- This script creates a table named `users` with the following attributes:
-- - id: integer, never null, auto increment, primary key
-- - email: string (255 characters), never null, unique
-- - name: string (255 characters)
-- - country: enumeration of countries (US, CO, TN), never null with default value 'US'
-- The script ensures the table is created only if it does not already exist.

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY (id)
);
