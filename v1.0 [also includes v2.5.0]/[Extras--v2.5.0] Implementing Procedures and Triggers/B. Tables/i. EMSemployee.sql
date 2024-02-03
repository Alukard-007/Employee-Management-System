CREATE TABLE EMSemployee (
  EID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  DOB DATE NOT NULL,
  FirstName VARCHAR(20) NOT NULL,
  LastName VARCHAR(20) NOT NULL,
  Gender CHAR(1) CHECK (Gender='M' OR Gender='F' OR Gender='m' OR Gender='f'),
  Department VARCHAR(20) NOT NULL,
  Salary INT NOT NULL
);
