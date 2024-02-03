Program Name: Employee Management System [v1.0 and v2.5.0]
Author: Buland Jayeshkumar Shah (Alukard.007)
Country: India
-------------------------------------------------------------------------------------------

<version 1.0>------------------------------------------------------------------------------
Program Description:
The program is a simple non-GUI Employee Management System that makes use of two key concepts:
- Python Interfacing through MySQL
- File Handling

The primary component of MySQL is required since the main "EmployeeDB" table is stored inside the one of the MySQL databases. Through the interfacing into Python, basic essential operations like:
- Viewing the employee table
- Adding a new row
- Update an existing row
- Delete an existing row
are implemented via SQL queries. 

The secondary component of File-Handling comes into picture for secondary saving of the employee records. A file called "EmployeeDB.txt" is created(on the first execution of the program) and maintained(after every data-manipulation session) in the same directory as that of the main program python file, "EmployeeManagementSystem[MySQL-Based Storage].py".

The logical component of the program is based on a menu-driven approach. Furthermore, I was fascinated by the terminal output display of SQL tables and was therfore very keen on trying to replicate that display structure into this simple program. 

A simple addition of separator strings of the form "-------" around rows and " | " around columns werent enough since each column had data values with differing lengths, therefore destroying a fixed table layout. To fix this, every data value (dataType: String) from each column is added with additional blanks on either sides of the string in order to make them appear centre-aligned. This number of blanks is decided based on the longest string in each column. 

This way, each column had data values (strings, from each row) of the same length. I know there are built-in string functions now that can centre-align a string but even if I knew that fact back then, I would still implement it this way since I was interested in developing functions my way and would look at the built-in Python functions from the libraries to get to know how the functions work behind-the-scenes. 

However, one drawback (discovered during testings) of this centre-alignment is that it only works on specific fonts. And I figured out the reason, which was simple: each font has differing character size in terms of the pixels(in width; horizontally) they occupy. For example, the number of horizontal pixels of the character 'M' and 't" may differ in some fonts while may be of the same pixels in other font. 

At the moment, it works perfectly fine with the native Python IDLE default font, Courier.

This program is of version 1.0 since this was developed in 2021 (as far as I remember), when I was in Grade 12 and had learnt the concepts of SQL and File-Handling.

Softwares used for development include:

[Windows OS]
- Native Python IDLE (for programming and testing)
- MySQL Workbench

[Android OS]
Since I did not had a computer system at home, and the school PCs were unavailable due to the COVID lockdown, I wrote my code on paper and then ran on my Android smartphone. Several apps like DCoder were handy to run program files while YouTube tutorials did the same for installing SQL into Android through Terminal apps like Termux. It was fun:)



<v2.5.0>------------------------------------------------------------------------------
Cut to 2nd Year, 4th Semester of BTech CSE in 2023, I was studying Database Management Systems in further details from where I got to learn about Procedures, Functions and Triggers and PL-SQL.


I made further additions and improvements in the Employee Database:
- Further added 9 more tables related to employees' data
- Established an Entity-Relationship between the existing tables
- Implemented Triggers, Functions and Procedures

The previous basic operations of data manipulation like adding, updating and deleting rows where now carried out by procedures in itself. The previous logic of the Python code was changed on many levels. Unfortunately, I lost the program file in an unwanted data cleanup of my SSD. However, I could manage to regain the project file I had submitted from my University LMS Platform. It contained screenshots and some SQL codes which are placed in the folder, "[Extras--v2.5.0]". I was unable to give the developed program a GUI feature as I was more focused on the backend MySQL counterparts.

A GUI version of my Employee Management System also exists, developed as v2.0, after developing v1.0

Recycling, updation and adaptation according to the newly learnt techniques was one of the key experiental learnings throughout these 3 versions.


~Sic Parvis Magna~
-Alukard.007