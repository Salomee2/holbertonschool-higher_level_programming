-- 15. Comedy Only
-- List only comedy shows.
SELECT title FROM tv_shows WHERE genre_id = (SELECT id FROM tv_genres WHERE name = 'Comedy');

