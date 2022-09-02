-- Creates a stored procedure that computes and
-- store the average score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE average FLOAT;

	SET average = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id = user_id);

	UPDATE users SET users.average_score = average WHERE id = user_id;
END
$$

DELIMITER ;
