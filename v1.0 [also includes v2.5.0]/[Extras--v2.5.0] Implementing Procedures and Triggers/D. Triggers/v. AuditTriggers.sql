DROP TRIGGER IF EXISTS auditTriggerUpdate; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdate after  update on EMSemployee for each row  begin 
insert into audits(tableName,transactionName,userName,transactionDate) 
values('EMSemployee','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateAttendance after  update  on attendance for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Attendance','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateDepartment after  update on department for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Department','UPDATE',user(),now()); end $$ 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateLeave_eligibility after  update on leave_eligibility for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leave_Eligibility','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateLeavesTaken after  update on leaves_taken for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leaves_Taken','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateMonthlySalary after  update on monthlysalary for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('MonthlySalary','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerUpdateSalary after  update on salary for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Salary','UPDATE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerInsert after  insert 
on EMSemployee for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('EMSemployee','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerINSERTAttendance after  
INSERT 
on attendance for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Attendance','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerINSERTDepartment 
after  
INSERT 
on department for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Department','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerINSERTLeave_eligibility after  
INSERT 
on leave_eligibility for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leave_Eligibility','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerINSERTLeavesTaken after  
INSERT 
on leaves_taken for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leaves_Taken','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerInsertMonthlySalary after  insert on monthlysalary for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('MonthlySalary','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerInsertSalary after  insert on salary 
for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Salary','INSERT',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
CREATE TRIGGER auditTriggerDELETE after  
DELETE on EMSemployee for each row  begin 
 insert into audits(tableName,transactionName,userName,transactionDate) values('EMSemployee','DELETE',user(),now()) ; end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDELETEAttendance after  
DELETE 
on attendance for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Attendance','DELETE',user(),now()); 
end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDELETEDepartment after  
DELETE 
on department for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Department','DELETE',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDELETELeave_eligibility after  
DELETE 
on leave_eligibility for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leave_Eligibility','DELETE',user(),now()); end $$ 
 
DELIMITER ; 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDELETELeavesTaken after  
DELETE 
on leaves_taken for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Leaves_Taken','DELETE',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDELETEMonthlySalary after  
DELETE 
on monthlysalary for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('MonthlySalary','DELETE',user(),now()); end $$ 
 
DELIMITER ; 
 
 
DELIMITER $$ 
 
CREATE TRIGGER auditTriggerDeleteSalary after  delete on salary for each row  begin 
 	insert into audits(tableName,transactionName,userName,transactionDate) values('Salary','DELETE',user(),now()); end $$ 
 
DELIMITER ; 
select*from leave_eligibility; insert into leaves_taken values(); 
