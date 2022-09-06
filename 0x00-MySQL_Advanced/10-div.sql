-- creates a function that divides the first by the second number or returns 0 if the second number is equal to 0.
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT
BEGIN
IF b = 0 THEN
RETURN 0
ELSE
DECLARE result FLOAT;
SET result = a / b;
RETURN result;
END IF;
END$$

DELIMITER ;