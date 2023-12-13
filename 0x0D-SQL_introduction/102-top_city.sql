-- this script displays top 3 cities temperatures during july and august
-- Ordered by temperature(descending order)

SELECT city, AVG(value) as 'avg_temp' FROM temperatures WHERE `month`=7 OR `month`=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
