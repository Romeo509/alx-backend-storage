-- 3-glam_rock.sql
-- This script lists all bands with Glam rock as their main style, ranked by their longevity.

SELECT 
    name AS band_name,
    CASE
        WHEN split IS NOT NULL THEN YEAR(split) - YEAR(formed)
        ELSE 2022 - YEAR(formed)
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
