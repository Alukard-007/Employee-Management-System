CREATE TABLE audits (
  auditID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  tableName VARCHAR(200),
  transactionName VARCHAR(10),
  userName VARCHAR(30),
  transactionDate DATE
);
