-- This script lists all records from second_table where score >= 10, ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
