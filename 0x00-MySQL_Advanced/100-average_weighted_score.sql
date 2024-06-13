-- Create stored procedure ComputeAverageWeightedScoreForUser
-- Computes and stores the average weighted score for a student
-- Takes 1 input: user_id, a users.id value

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_weighted_score FLOAT;

    -- Calculate total weighted score and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate average weighted score
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update users table with the computed average weighted score
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = user_id;

END $$

DELIMITER ;
