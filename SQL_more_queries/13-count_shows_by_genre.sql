-- List all genres and the number of shows linked to each genre
-- Display: genre - number_of_shows
SELECT genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY genre
HAVING COUNT(tv_show_genres.tv_show_id) > 0
ORDER BY number_of_shows DESC;
