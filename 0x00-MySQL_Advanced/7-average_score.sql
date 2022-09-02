-- created a stored procedure that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
UPDATE users
SET average_score = (
    SELECT AVG(score)
    FROM corrections
    WHERE id = user_id
);
END$$
DELIMITER ;