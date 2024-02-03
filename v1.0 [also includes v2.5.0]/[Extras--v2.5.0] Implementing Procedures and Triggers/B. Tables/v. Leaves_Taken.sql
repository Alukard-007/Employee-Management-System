CREATE TABLE Leaves_Taken (
  leave_id INT NOT NULL AUTO_INCREMENT,
  employee_id INT NOT NULL,
  leave_type VARCHAR(50) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  reason VARCHAR(255),
  approval_status VARCHAR(20),
  approving_authority VARCHAR(50),
  PRIMARY KEY (leave_id, employee_id),
  CONSTRAINT fk_employee_id FOREIGN KEY (employee_id)
    REFERENCES EMSemployee(EID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
