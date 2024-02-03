==============|GENERAL INFORMATION|===============
---------------------------------------------------------------------------
A) LOGIN
---------------------------------------------------------------------------
Login with an Admin User ID will open access to all data manipulation
functions.

Login with an Employee User ID will only allow viewing and searching 
of data.

Guest User ID and Password [Admin Mode] :
ID: guest@admin
Pass: admin@123

Guest User ID and Password [Employee Mode] :
ID: guest@employee
Pass: emp@123
---------------------------------------------------------------------------
B) FILES 
---------------------------------------------------------------------------
There are 3 files that are being used by the program:

1. IdPass.txt
This file contains a list of all supported USER IDs and Passwords.
The format is as follows:

<username1>,<password1>
<username2>,<password2>
           .             ,          .
           .             ,          .
           .             ,          . 
<usernameN>,<passwordN>

2. EncryptedDB.txt
This file contains the employee data in encrypted format. Every line 
represents a separate encrypted row. The main module of the program 
opens this file first and creates a list of all employee data rows after 
decrypting the data.

3. EmployeeDB.txt
This file also contains the employee data but the data is not encrypted
so as to demonstrate that the file handling concepts are saving the data.

---------------------------------------------------------------------------
C) General Queries
---------------------------------------------------------------------------
Q) How do I create a new User ID for login ?

Ans) 
On the login screen, press the "Create New User ID" button and 
create a new username and password. Note that the username should
be a new one and not an already existing username stored in "IdPass.txt".
 
Also, the username should end with either "@admin" or "@employee"
to specify which mode will be accessible to that ID.
__________________________________________________________________________

Q) How to operate the system ?

Ans)
The main interface of the Employee Management System has a 
Main Menu list on the extreme left side. This contains the buttons for
all supported functionalities. 

On the extreme right side, there are input entries for all the fields of the 
employee table.

The center screen displays the employee table with real-time changes.

Just below the center display, there is a small display that occasionally
displays some Help Message based on what you are performing.

The Main Menu provides access to 4 main functionalities:

1. Search 
To search for a row/s having a specific field value, press on Search button
and select the column from which your search value belongs. 

Then, enter the search value and hit search. If present, the result rows 
will be displayed. 

2. Add Row
Click on "Add A New Row" and then enter all field values according
to the prescribed format. Hit Submit once all values are entered. The 
Submit button will stay disabled until all the field values are entered
according the correct format.

3. Update Row
Click on "Update A Row" and then enter the EID of that row which needs
to be updated. Then enter the remaining field values. If you do not
wish to change a specific value, then enter '*s' to retain its original value.

4. Delete Row
Click on "Delete Row" and then enter the EID of that row which needs to 
be deleted.
________________________________________________________________________

Q) In the Delete Row option, I can only delete one row at a time. How to
delete the entire table ?

Ans)
You can delete the contents of "EncryptedDB.txt" file to delete all data.
Just do not delete the entire file. 
Alternative:
You can also delete the entire file but make sure that you create an
empty text file with name "EncryptedDB.txt" as it is.
-------------------------------------------------------------------------
===================|CREDITS|====================

Employee Management System project made in Python language,
implemeting File-Handling, Encryption/Decryption and GUI-Design through Tkinter.

Project made as a part of CSE100: Fundamentals of Computer
Programming [Section-3] course, under the School of Engineering
And Science, Ahmedabad University.

Made by:
AU2140088 Buland Jayeshkumar Shah
