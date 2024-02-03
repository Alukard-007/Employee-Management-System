DELIMITER $$
CREATE PROCEDURE viewEmployee()
BEGIN
    DECLARE EID int;
    DECLARE DOB date;
    DECLARE FirstName varchar(20);
    DECLARE LastName varchar(20);
    DECLARE Gender char(1);
    DECLARE Department varchar(20);
    DECLARE Salary int;
    DECLARE done INT DEFAULT FALSE;
    DECLARE c_emp cursor for SELECT * FROM EMSemployee;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    open c_emp;
    
    my_loop: loop
        fetch c_emp into EID, DOB, FirstName, LastName, Gender, Department, Salary;
        IF done THEN
            LEAVE my_loop;
        END IF;
        
        -- select EID, DOB, FirstName, LastName, Gender, Department, Salary;
        SELECT CONCAT(EID, ', ', DOB, ', ', FirstName, ', ', LastName, ', ', Gender, ', ', Department, ', ', Salary);
    end loop;
    
    close c_emp;
END $$
DELIMITER;
