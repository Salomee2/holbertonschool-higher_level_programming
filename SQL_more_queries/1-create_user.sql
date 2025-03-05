CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;

