CREATE TABLE salary (
  salary_id INT NOT NULL AUTO_INCREMENT,
  employee_id INT NOT NULL,
  date DATE NOT NULL,
  basic_salary INT NOT NULL UNIQUE,
  provident_fund DECIMAL(10,2) NOT NULL,
  overtime INT(4) NOT NULL,
  other_allowances INT(4) NOT NULL,
  deductions INT NOT NULL,
  net_salary INT NOT NULL,
  PRIMARY KEY (salary_id, basic_salary),
  FOREIGN KEY (employee_id) REFERENCES EMSemployee(EID),
  FOREIGN KEY (basic_salary) REFERENCES EMSemployee(Salary)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
