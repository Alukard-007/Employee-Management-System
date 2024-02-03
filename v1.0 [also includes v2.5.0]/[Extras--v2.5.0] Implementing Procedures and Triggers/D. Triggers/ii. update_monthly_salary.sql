DELIMITER $$
CREATE TRIGGER update_monthly_salary AFTER INSERT ON `attendance`
FOR EACH ROW
BEGIN
    DECLARE daily_salary FLOAT;
    DECLARE workingDays INT;
    DECLARE annualSal INT;

    SELECT total_working_days INTO workingDays FROM attendance
    WHERE employee_id = NEW.employee_id AND year = NEW.year;

    SELECT net_salary INTO annualSal
    FROM salary
    WHERE employee_id = NEW.employee_id;

    SELECT annualSal / workingDays INTO daily_salary;

    INSERT INTO monthlysalary VALUES (
        NEW.employee_id,
        NEW.year,
        NEW.january_attendance * daily_salary,
        NEW.february_attendance * daily_salary,
        NEW.march_attendance * daily_salary,
        NEW.april_attendance * daily_salary,
        NEW.may_attendance * daily_salary,
        NEW.june_attendance * daily_salary,
        NEW.july_attendance * daily_salary,
        NEW.august_attendance * daily_salary,
        NEW.september_attendance * daily_salary,
        NEW.october_attendance * daily_salary,
        NEW.november_attendance * daily_salary,
        NEW.december_attendance * daily_salary
    );
END $$
DELIMITER ;
