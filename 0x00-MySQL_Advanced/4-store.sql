-- trigger that decrease quantity of an item
-- after adding new order
-- quantity in table item can be negative
DELIMITER |

CREATE TRIGGER decrease_qty AFTER INSERT  ON orders
FOR EACH ROW
BEGIN
	UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
END; 
| 

DELIMITER ;
