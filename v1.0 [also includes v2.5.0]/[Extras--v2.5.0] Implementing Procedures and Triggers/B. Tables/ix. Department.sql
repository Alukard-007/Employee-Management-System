CREATE TABLE department (
  id INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  status VARCHAR(50),
  description VARCHAR(500),
  head_of_department INT,
  total_employees INT,
  budget DECIMAL(10, 2),
  date_created DATE,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
