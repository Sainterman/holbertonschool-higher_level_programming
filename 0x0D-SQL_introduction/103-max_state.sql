-- script that displays the max temperature of each state (ordered by State name).
-- select state, temp group by state order byi
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;
