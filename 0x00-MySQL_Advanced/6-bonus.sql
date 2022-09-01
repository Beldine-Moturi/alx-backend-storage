-- creates a stored procedure that adds a new correction for a student
DELIMITER $$
CREATE
    PROCEDURE my_proc (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
    BEGIN
        CASE WHEN project_name NOT IN (SELECT name FROM projects) THEN
            INSERT INTO projects (name) VALUES (project_name);
        END CASE;
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
    END$$
DELIMITER ;