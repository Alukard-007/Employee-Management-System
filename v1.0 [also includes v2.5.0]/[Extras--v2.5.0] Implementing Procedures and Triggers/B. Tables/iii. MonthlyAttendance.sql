CREATE TABLE Attendance (
  employee_id INT NOT NULL,
  year INT NOT NULL,
  january_attendance INT NOT NULL DEFAULT 0,
  february_attendance INT NOT NULL DEFAULT 0,
  march_attendance INT NOT NULL DEFAULT 0,
  april_attendance INT NOT NULL DEFAULT 0,
  may_attendance INT NOT NULL DEFAULT 0,
  june_attendance INT NOT NULL DEFAULT 0,
  july_attendance INT NOT NULL DEFAULT 0,
  august_attendance INT NOT NULL DEFAULT 0,
  september_attendance INT NOT NULL DEFAULT 0,
  october_attendance INT NOT NULL DEFAULT 0,
  november_attendance INT NOT NULL DEFAULT 0,
  december_attendance INT NOT NULL DEFAULT 0,
  total_working_days INT NOT NULL DEFAULT 365,
  PRIMARY KEY (employee_id, year),
  FOREIGN KEY (employee_id) REFERENCES EMSemployee(EID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
