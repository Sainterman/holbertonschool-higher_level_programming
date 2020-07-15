-- script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- lagge
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month BETWEEN 7 and 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;