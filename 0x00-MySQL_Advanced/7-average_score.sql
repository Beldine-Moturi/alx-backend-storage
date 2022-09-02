-- created a stored procedure that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
DECLARE avg FLOAT;
SET avg = (SELECT AVG(score) FROM corrections AS c WHERE c.user_id = user_id GROUP BY c.user_id);
UPDATE users SET users.average_score = avg;
END$$
DELIMITER ;