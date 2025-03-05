-- 7. Cities
-- Create a table 'cities' with columns 'id', 'name', and 'state_id'.
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    state_id INT,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
