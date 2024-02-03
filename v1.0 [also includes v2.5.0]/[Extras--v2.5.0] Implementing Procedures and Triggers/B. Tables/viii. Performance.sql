CREATE TABLE Performance (
  employee_id INT NOT NULL,
  project_id INT NOT NULL,
  on_time_completion INT NOT NULL,
  quality_of_work INT NOT NULL,
  team_contribution INT NOT NULL,
  PRIMARY KEY (employee_id, project_id),
  FOREIGN KEY (employee_id) REFERENCES EMSemployee(EID) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE ON UPDATE CASCADE
);
