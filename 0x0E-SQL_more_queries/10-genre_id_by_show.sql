-- This script lists all shows that have at least one genre linked.

-- Apply join to dsplay data and order based on title and genre id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
