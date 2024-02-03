DELIMITER $$
CREATE TRIGGER update_leave_eligibility
AFTER INSERT ON leaves_taken
FOR EACH ROW
BEGIN
    DECLARE max_leaves INT;
    DECLARE taken_leaves INT;
    DECLARE remaining_leaves INT;
    DECLARE curr_leave_duration INT;

    SELECT max_leave_capacity INTO max_leaves FROM leave_eligibility WHERE employee_id = NEW.employee_id;
    SELECT COALESCE(SUM(DATEDIFF(end_date, start_date)), 0) INTO taken_leaves
    FROM leaves_taken
    WHERE employee_id = NEW.employee_id AND YEAR(start_date) = YEAR(NEW.start_date) AND approval_status = 'Approved';

    SELECT DATEDIFF(NEW.end_date, NEW.start_date) INTO curr_leave_duration;

    SET remaining_leaves = max_leaves - (taken_leaves + curr_leave_duration);

    IF remaining_leaves < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No remaining leaves left';
        IF EXISTS (SELECT * FROM leave_eligibility WHERE employee_id = NEW.employee_id) THEN
            UPDATE leave_eligibility SET remaining_leaves = GREATEST(0, remaining_leaves) WHERE employee_id = NEW.employee_id;
        ELSE
            INSERT INTO leave_eligibility (employee_id, remaining_leaves) VALUES (NEW.employee_id, GREATEST(0, remaining_leaves));
        END IF;
    ELSEIF EXISTS (SELECT * FROM leave_eligibility WHERE employee_id = NEW.employee_id) THEN
        UPDATE leave_eligibility SET remaining_leaves = remaining_leaves WHERE employee_id = NEW.employee_id;
    ELSE
        INSERT INTO leave_eligibility (employee_id, remaining_leaves) VALUES (NEW.employee_id, remaining_leaves);
    END IF;
END $$
DELIMITER ;
