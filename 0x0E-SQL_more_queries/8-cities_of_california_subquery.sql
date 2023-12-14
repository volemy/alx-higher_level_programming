-- script that lists all the cities of California that can be
-- found in the database hbtn_0d_usa.

FROM cities
SELECT id, name
WHERE state_id = (SELECT id FROM states WHERE name = "california") GROUP BY id ORDER BY id ASC;
