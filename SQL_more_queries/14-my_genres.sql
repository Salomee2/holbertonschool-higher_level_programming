-- 14. My Genres
-- Create the 'my_genres' table with columns 'id' and 'name'.
CREATE TABLE IF NOT EXISTS my_genres (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
