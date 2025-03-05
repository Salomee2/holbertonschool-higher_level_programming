-- 9. Cities by State Join
-- List cities along with their corresponding state names using a JOIN.
SELECT cities.name AS city, states.name AS state
FROM cities
JOIN states ON cities.state_id = states.id;
