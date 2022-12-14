-- creates a trigger that resets the attribute valid_email only when the email has been changed.
DELIMITER $$
CREATE
    TRIGGER my_trigger1 AFTER UPDATE
    ON users
    FOR EACH ROW BEGIN
        IF OLD.email <> NEW.email THEN
            IF OLD.valid_email = 0 THEN
            SET NEW.valid_email = 1;
            ELSEIF OLD.valid_email = 1 THEN
            SET NEW.valid_email = 0;
            END IF;
        END IF;
    END$$
DELIMITER ;
