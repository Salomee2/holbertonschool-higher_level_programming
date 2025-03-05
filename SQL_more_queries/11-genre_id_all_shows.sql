-- 11. Genre ID for All Shows
-- List all shows with their genre IDs.
SELECT tv_shows.title, tv_genres.id AS genre_id
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
ORDER BY tv_shows.title;
