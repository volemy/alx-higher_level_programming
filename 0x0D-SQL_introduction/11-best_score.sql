-- this script lists all records with a score >= 10 in second_table
-- in  database

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
