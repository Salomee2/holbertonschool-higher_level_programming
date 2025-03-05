-- List all shows with at least one genre linked
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres 
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
