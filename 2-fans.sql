-- create to rank country of origin
-- order by non-unique fans
SELECT  origin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY origin
ORDER BY sum(fans) DESC;
