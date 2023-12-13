-- This script lists all records of the table second_table of the database
-- Do not list rows without a name value
-- Records should be listed in decending order

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
