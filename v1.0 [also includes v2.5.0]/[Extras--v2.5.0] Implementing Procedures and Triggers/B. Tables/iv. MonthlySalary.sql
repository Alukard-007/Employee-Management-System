CREATE TABLE MonthlySalary (
  employee_id INT NOT NULL,
  year INT NOT NULL,
  january_final_salary INT NOT NULL DEFAULT 0,
  february_final_salary INT NOT NULL DEFAULT 0,
  march_final_salary INT NOT NULL DEFAULT 0,
  april_final_salary INT NOT NULL DEFAULT 0,
  may_final_salary INT NOT NULL DEFAULT 0,
  june_final_salary INT NOT NULL DEFAULT 0,
  july_final_salary INT NOT NULL DEFAULT 0,
  august_final_salary INT NOT NULL DEFAULT 0,
  september_final_salary INT NOT NULL DEFAULT 0,
  october_final_salary INT NOT NULL DEFAULT 0,
  november_final_salary INT NOT NULL DEFAULT 0,
  december_final_salary INT NOT NULL DEFAULT 0,
  PRIMARY KEY (employee_id, year),
  FOREIGN KEY (employee_id) REFERENCES EMSemployee(EID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
