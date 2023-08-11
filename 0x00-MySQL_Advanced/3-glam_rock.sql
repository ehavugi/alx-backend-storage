-- list bands with Glam rock style 
-- ranked their longitivity
SELECT band_name, (IFNULL(split, 2022) -formed) AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
