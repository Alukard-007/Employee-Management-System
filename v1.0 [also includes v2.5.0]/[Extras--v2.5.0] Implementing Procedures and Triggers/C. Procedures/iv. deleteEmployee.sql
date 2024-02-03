DELIMITER $$
CREATE PROCEDURE deleteEmployee (eid int)
BEGIN
    DELETE FROM EMSemployee WHERE EID = eid;
END $$
DELIMITER ;
