DELIMITER $$
CREATE PROCEDURE addEmployee (in dob date, in fname varchar(30), in lname varchar(30), in gen char(1), in dept varchar(20), in sal int)
BEGIN
    INSERT INTO EMSemployee (DOB, FirstName, LastName, Gender, Department, Salary)
    VALUES(dob, fname, lname, gen, dept, sal);
END $$
DELIMITER ;
