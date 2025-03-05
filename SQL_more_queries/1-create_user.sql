-- Script to create the MySQL user if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the MySQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Reload privileges to apply the changes
FLUSH PRIVILEGES;
