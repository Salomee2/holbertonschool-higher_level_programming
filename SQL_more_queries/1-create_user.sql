-- 1. Création de l'utilisateur si il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2. Attribution de tous les privilèges à cet utilisateur
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 3. Appliquer les privilèges
FLUSH PRIVILEGES;
