-- This script lists the number of records with same score in second_table
--of database

SELECT score,  COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
