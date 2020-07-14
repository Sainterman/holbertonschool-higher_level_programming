-- script that lists the number of records with the same score in the table second_table
-- should display the score, number of records for this score in descending
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number  DESC;
