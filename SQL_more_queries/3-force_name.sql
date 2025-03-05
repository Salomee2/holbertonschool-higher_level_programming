-- 1. Creation de la table force_name si elle n'existe pas deja
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
