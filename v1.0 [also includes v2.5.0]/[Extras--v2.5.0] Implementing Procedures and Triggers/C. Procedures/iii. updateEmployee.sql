DELIMITER $$
CREATE PROCEDURE updateEmployee(eid int, in dob date, in fname varchar(30), in lname varchar(30), in gen char(1), in dept varchar(20), in sal int)
BEGIN
    UPDATE EMSemployee
    SET DOB = dob, FirstName = fname, LastName = lname, Gender = gen, Department = dept, Salary = sal
    WHERE EID = eid;
END $$
DELIMITER ;
