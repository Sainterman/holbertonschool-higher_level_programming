-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- states contains one name = California, sorted ASC by cities.id, not using JOIN
SELECT id, name FROM cities WHERE (SELECT name FROM states WHERE name IS LIKE California) ORDER BY id ASC;
