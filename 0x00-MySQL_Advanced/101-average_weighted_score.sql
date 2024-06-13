-- Create stored procedure ComputeAverageWeightedScoreForUsers
-- Computes and stores the average weighted score for all students

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE userId INT;
    DECLARE userCursor CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN userCursor;

    read_loop: LOOP
        FETCH userCursor INTO userId;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate total weighted score and total weight for each user
        UPDATE users u
        SET u.average_score = (
            SELECT 
                IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
            FROM 
                corrections c
            JOIN 
                projects p ON c.project_id = p.id
            WHERE 
                c.user_id = u.id
        )
        WHERE u.id = userId;

    END LOOP;

    CLOSE userCursor;
END $$

DELIMITER ;
