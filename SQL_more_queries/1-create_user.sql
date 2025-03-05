-- 1. Vérification si l'utilisateur 'user_0d_1' existe déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2. Création de l'utilisateur 'user_0d_1' avec le mot de passe
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 3. Attribution de tous les privilèges à l'utilisateur 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 4. Appliquer les privilèges
FLUSH PRIVILEGES;
