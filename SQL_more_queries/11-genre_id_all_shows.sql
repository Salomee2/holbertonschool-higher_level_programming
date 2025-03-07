-- List all shows and their genre_id (if any)
-- Display: tv_shows.title - tv_show_genres.genre_id
-- Shows with no genre will display NULL for genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
