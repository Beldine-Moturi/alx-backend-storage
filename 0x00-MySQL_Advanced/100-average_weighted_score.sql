-- creates a stored procedure that computes and store the average weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN

    DECLARE average FLOAT;

    CREATE TABLE project_weight AS
    SELECT C.user_id, C.project_id, C.score, P.weight
    FROM corrections AS C
    INNER JOIN projects AS P ON P.id = C.project_id;

    SET average = WITH weights AS
    (
        SELECT user_id, project_id, (score * weight) AS score_weight
        FROM project_weight
    )
    SELECT SUM(score_weight)
    FROM weights AS W
    WHERE W.user_id = user_id;

    UPDATE users SET users.average_score = average WHERE users.id = user_id;

END$$
DELIMITER ;