-- List all cities with their corresponding state names
-- Each record shows cities.id - cities.name - states.name
-- Sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
