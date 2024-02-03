CREATE TABLE Leave_Eligibility (
  employee_id INT NOT NULL,
  max_leave_capacity INT DEFAULT 13,
  remaining_leaves INT DEFAULT 13,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (employee_id) REFERENCES EMSemployee(EID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
