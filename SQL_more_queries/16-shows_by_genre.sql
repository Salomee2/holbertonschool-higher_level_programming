-- 16. Shows by Genre
-- List shows and their genres, with NULL if no genre is associated.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_genres ON tv_shows.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
