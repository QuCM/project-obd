-- geo_shape_coordinates: longitude, latitude

CREATE OR REPLACE FUNCTION is_near(coordinates POINT[], place POINT, epsilon FLOAT)
    RETURNS BOOLEAN LANGUAGE plpgsql AS $$

    DECLARE
        DEG_TO_RAD FLOAT;

    BEGIN
        IF CARDINALITY(coordinates) IS NULL THEN
            RETURN false;
        END IF;
        
        DEG_TO_RAD := PI()/180;

        FOR i IN 0..CARDINALITY(coordinates) LOOP
            IF ACOS(SIN((coordinates[i])[1]*DEG_TO_RAD) * SIN(place[1]*DEG_TO_RAD) + COS((coordinates[i])[1]*DEG_TO_RAD) * COS(place[1]*DEG_TO_RAD) * COS((coordinates[i])[0]*DEG_TO_RAD - place[0]*DEG_TO_RAD)) * 6378137 < epsilon THEN
                RETURN true;
            END IF;
        END LOOP;
        RETURN false;
    END $$
;


SELECT 
    COUNT(*)
FROM 
    reseau
WHERE 
    is_near(geo_shape_coordinates_1, '(1.471564, 43.570297)'::POINT, 100) OR
    is_near(geo_shape_coordinates_2, '(1.471564, 43.570297)'::POINT, 100) OR
    is_near(geo_shape_coordinates_3, '(1.471564, 43.570297)'::POINT, 100)
;
