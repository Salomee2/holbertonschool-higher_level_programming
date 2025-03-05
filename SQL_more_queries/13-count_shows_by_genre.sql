-- 13. Count Shows by Genre
-- Count the number of shows for each genre.
SELECT tv_genres.name, COUNT(tv_shows.id) AS show_count
FROM tv_genres
LEFT JOIN tv_shows ON tv_genres.id = tv_shows.genre_id
GROUP BY tv_genres.name;
