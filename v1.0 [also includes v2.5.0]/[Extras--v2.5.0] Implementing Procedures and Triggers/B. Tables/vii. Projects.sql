CREATE TABLE Projects (
  project_id INT NOT NULL AUTO_INCREMENT,
  project_name VARCHAR(50) NOT NULL,
  project_manager VARCHAR(50) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  status_ VARCHAR(20) NOT NULL,
  kpi_rating DECIMAL(5,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (project_id)
);
