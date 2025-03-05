-- List all the cities of California from the database hbtn_0d_usa
-- Results are sorted by cities.id in ascending order
-- Using a subquery to filter by the state name "California"
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
