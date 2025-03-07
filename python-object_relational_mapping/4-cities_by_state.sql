-- Création de la base de données si elle n'existe pas
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;

-- Création de la table states
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insertion de quelques états
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

-- Création de la table cities
CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);

-- Insertion de quelques villes
INSERT INTO cities (state_id, name) VALUES 
(1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore"),
(2, "Page"), (2, "Phoenix"),
(3, "Dallas"), (3, "Houston"), (3, "Austin"),
(4, "New York"),
(5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
