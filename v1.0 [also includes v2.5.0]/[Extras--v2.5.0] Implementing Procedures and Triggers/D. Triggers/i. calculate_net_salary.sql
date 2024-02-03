DELIMITER $$
CREATE TRIGGER calculate_net_salary
BEFORE INSERT ON salary
FOR EACH ROW
BEGIN
    DECLARE provident_fund_amount DECIMAL(18, 2);
    SET provident_fund_amount = (NEW.basic_salary * NEW.provident_fund) / 100;
    SET NEW.net_salary = NEW.basic_salary + NEW.overtime + NEW.other_allowances - provident_fund_amount - NEW.deductions;
END $$
DELIMITER ;
