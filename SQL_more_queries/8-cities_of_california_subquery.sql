-- 8. Cities of California Subquery
-- List all the cities from California (state_id = 1) using a subquery.
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California');
