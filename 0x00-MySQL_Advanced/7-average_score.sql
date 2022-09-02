-- created a stored procedure that computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
-- declare variables
DECLARE @a INT;
DECLARE @b FLOAT;

--declare and use cursor
DECLARE my_cursor CURSOR FOR
    SELECT user_id, AVG(score) AS avg_score
    FROM corrections
    GROUP BY user_id;

OPEN my_cursor;

FETCH NEXT FROM my_cursor INTO @a, @b;

WHILE @@FETCH_STATUS = 0
BEGIN
    UPDATE users
    SET average_score = @b
    WHERE id = @a;

    FETCH NEXT FROM my_cursor INTO @a, @b;
END;
END$$
DELIMITER ;