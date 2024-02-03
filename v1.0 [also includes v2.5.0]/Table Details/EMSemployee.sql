show databases;
use python;
show tables;

create table EMSemployee (
EID int                    NOT NULL UNIQUE PRIMARY KEY,
DOB date                   NOT NULL,
FirstName varchar(20)      NOT NULL,
LastName varchar(20)       NOT NULL,
Gender char(1)             NOT NULL,
Department varchar(20)     NOT NULL DEFAULT "MANAGEMENT",
Salary int                 NOT NULL);

desc emsemployee;


