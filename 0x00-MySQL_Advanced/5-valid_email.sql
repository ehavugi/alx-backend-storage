-- trigger resets attribute valid_email only when email has been changed
-- so it is after and affects same row?
DELIMITER |

CREATE TRIGGER validateemailv2 AFTER UPDATE on users
FOR EACH ROW
BEGIN
	UPDATE users set valid_email = 0 where users.email!= NEW.email AND users.id = NEW.id;
END;
|
DELIMITER ;
