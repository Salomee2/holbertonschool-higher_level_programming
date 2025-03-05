-- 1. Suppression de l'utilisateur s'il existe
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- 2. Création de l'utilisateur avec un mot de passe
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 3. Attribution de tous les privilèges à l'utilisateur 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 4. Appliquer les privilèges
FLUSH PRIVILEGES;
