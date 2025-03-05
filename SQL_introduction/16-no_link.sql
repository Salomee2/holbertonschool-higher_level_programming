-- This script lists records where the name column contains a value
-- The results are ordered by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
