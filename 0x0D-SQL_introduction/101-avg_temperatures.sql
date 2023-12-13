--This script displays the average temperature(Fahrenheit) by city ordered by
-- temperature

USE hbtn_0c_0;
SELECT city, AVG(value) AS `avg_temp` FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
