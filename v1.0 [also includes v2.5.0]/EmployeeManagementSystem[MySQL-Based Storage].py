#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 1 : FOR ADDING BLANKS SO THAT EVERY PRINTED COLUMN VALUES ARE CENTRE ALIGNED
def addblanks(l):

    n=len(l)
    newl=list()

    for i in range(n):
        b=len(l[i])

        if(i==0):
            maxv=b
        elif(b>=maxv):
            maxv=b

    for f in l:

        g=len(f)
        res=maxv-g
        cont=0

        for h in range(res):
            if(res%2==0):
                res_n=res
            else:
                res_n=res-1

            if(cont==(res_n/2)):
                f=" "+f
            else:
                f=f+" "
                cont=cont+1
        newl.append(f)
        
    return tuple(newl)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 2 : CONVERTS ALL TABLE DATA INTO STRING AND SENDS TO addblanks() METHOD FOR CENTRAL ALIGNMENT AND THEN FINALLY RETURNS A LIST OF ALL COLUMNS AND THEIR VALUES
def resize():
    global r

    
    cursor1=mycon.cursor()
    cursor1.execute("SELECT*FROM EMSemployee")
    vdb=(cursor1.fetchall())
    r=cursor1.rowcount

    eidl=list()
    dobl=list()
    fnl=list()
    lnl=list()
    genl=list()
    depl=list()
    sall=list()

    eidl.append("EID")
    dobl.append("DOB")
    fnl.append("FirstName")
    lnl.append("LastName")
    genl.append("Gender")
    depl.append("Department")
    sall.append("Salary")

    for g in range(r):
        eidl.append(str(vdb[g][0]))

   # for s in range(r):
        dobl.append(str(vdb[g][1]))

 #   for o in range(r):
        fnl.append(str(vdb[g][2]))

  #  for p in range(r):
        lnl.append(str(vdb[g][3]))

  #  for d in range(r):
        genl.append(str(vdb[g][4]))

#    for f in range(r):
        depl.append(str(vdb[g][5]))
    
#    for k in range(r):
        sall.append(str(vdb[g][6]))



    eidr=addblanks(eidl)
    dobr=addblanks(dobl)
    fnr=addblanks(fnl)
    lnr=addblanks(lnl)
    genr=addblanks(genl)
    depr=addblanks(depl)
    salr=addblanks(sall)
                    
    vdbc=list()
    vdbl=list()

    for t in range(r+1):

        vdbc=list()

        vdbc.append(eidr[t])
        vdbc.append(dobr[t])
        vdbc.append(fnr[t])
        vdbc.append(lnr[t])
        vdbc.append(genr[t])
        vdbc.append(depr[t])
        vdbc.append(salr[t])
        vdbl.append(vdbc)

    return vdbl
#------------------------------------------------------------------------------------------------------------------------------------
#METHOD 3 : PRINTS THE EMPLOYEE TABLE FROM DATABASE IN TABULAR FORM
def viewDB():
    data=resize()
    m=len(data)
    
    l1=data[0]
    #m1=len(l1)
    n1=0
    for i in l1:
    	n1=n1+(len(i))
    n1=n1+(7*(len('    |    ')))-(((len('    |    ')+0)//2))
    
    str=""
    m1=0
    #print(n1)
    
    while(m1<n1):
    	str=str+'-'
    	m1=len(str)
    #print(m1)
    
    #str="-----------------------------------------------------------------------------------------------------------------"
 
    print(str)
    a="    |    "

    for i in range(m):
        print(a.join(data[i]),end=a)
        print("")
        print(str)
        if(i==0):
        	print(str)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 4 : FOR INSERTION OF NEW VALUES INTO THE EMPLOYEE TABLE 

def Add():
    cursor2=mycon.cursor()

    cursor2.execute("SELECT COUNT(*) FROM EMSemployee")
    rowCount=int(cursor2.fetchone()[0])
    #print(rowCount)

    if(rowCount!=0):
        cursor2.execute("SELECT MAX(EID) FROM EMSemployee")
        eid=cursor2.fetchall()
        idnew=int(eid[0][0])+1
    else:
        idnew=1

    print("Please enter the following details for the new employee : ")
    print("")

    dob=input("Enter DOB in YYYY-MM-DD format ")
    print("")
    fn=input("Enter the first name of the employee ")
    print("")
    ln=input("Enter the last name of the employee ")
    print("")
    gen=input("Enter Gender of employee as either 'M' or 'F' ")
    print("")
    dept=input("Enter the current working department of the employee ")
    print("")
    sal=int(input("Enter Enter the annual salary of employee "))
    print("")

    st1="INSERT INTO EMSemployee(EID,DOB,FirstName,LastName,Gender,Department,Salary) VALUES({},'{}','{}','{}','{}','{}',{})".format(idnew,dob,fn,ln,gen,dept,sal)

    cursor2.execute(st1)
    mycon.commit()

    print("")
    print("New row added successfully :)")
    viewDB()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 5 : FOR UPDATION OF SPECIFIED ROWS FROM THE EMPLOYEE TABLE

def Update():
    viewDB()
    print("")
    cursor3=mycon.cursor()

    cursor3.execute("SELECT EID FROM EMSemployee")
    eidList=cursor3.fetchall()
    eidListed=list()
    for i in eidList:
        eidListed.append(int(i[0]))
    #print(eidListed)

    uid=int(input("Enter EID of that employee whose details are to be updated : "))
    print("")

    if(uid not in eidListed):
        print("EMPLOYEE WITH THE EID ",uid," DOES NOT EXIST !")
    else:
        print("Enter new values for each column you want to update ")
        print("")

        print("If a value does not need to be updated , then input *s only")
        print("")

        udob=input("Enter DOB in YYYY-MM-DD format ")
        print("")

        if(udob=="*s"):
            cursor3.execute("SELECT DOB FROM EMSemployee WHERE EID = {}".format(uid))
            udob=str(cursor3.fetchone()[0])
        
        ufn=input("Enter the first name of the employee ")
        print("")

        if(ufn=="*s"):
            cursor3.execute("SELECT FirstName FROM EMSemployee WHERE EID = {}".format(uid))
            ufn=str(cursor3.fetchone()[0])
            
        uln=input("Enter the last name of the employee ")
        print("")

        if(uln=="*s"):
            cursor3.execute("SELECT LastName FROM EMSemployee WHERE EID = {}".format(uid))
            uln=str(cursor3.fetchone()[0])
            
        ugen=input("Enter Gender of employee as either 'M' or 'F' ")
        print("")

        if(ugen=="*s"):
            cursor3.execute("SELECT Gender FROM EMSemployee WHERE EID = {}".format(uid))
            ugen=str(cursor3.fetchone()[0])
            
        udept=input("Enter the current working department of the employee ")
        print("")

        if(udept=="*s"):
            cursor3.execute("SELECT Department FROM EMSemployee WHERE EID = {}".format(uid))
            udept=str(cursor3.fetchone()[0])
            
        usal=input("Enter Enter the annual salary of employee ")
        print("")

        if(usal=="*s"):
            cursor3.execute("SELECT Salary FROM EMSemployee WHERE EID = {}".format(uid))
            usal=str(cursor3.fetchone()[0])

        st2="UPDATE EMSemployee SET DOB = '{}',FirstName = '{}',LastName = '{}',Gender = '{}',Department = '{}',Salary = {} WHERE EID={}".format(udob,ufn,uln,ugen,udept,int(usal),uid)

        cursor3.execute(st2)    
        mycon.commit()

        print("")
        print("Successfully Updated the Required Details :) ")
        viewDB()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 6 : FOR DELETION OF SPECIFIED ROW FROM THE EMPLOYEE TABLE

def Delete():
    viewDB()
    print("")
    cursor4=mycon.cursor()

    did=int(input("Enter EID of that employee whose details are to be deleted "))

    cursor4.execute("SELECT EID FROM EMSemployee")
    didList=cursor4.fetchall()
    didListed=list()
    for i in didList:
        didListed.append(int(i[0]))

    if(did not in didListed):
        print("EMPLOYEE WITH THE EID ",did," DOES NOT EXIST !")
    else:
        
        st3="DELETE FROM EMSemployee WHERE EID={}".format(did)

        print("")
        print("-------------------WARNING!-----------------")
        print("THIS OPERATION IS PERMANENT!")
        print("")
        print("ARE YOU SURE YOU WANT TO DELETE ?")
        print("")

        ask=input("Enter Y for YES or N for NO : ")

        if(ask=='Y'):
            cursor4.execute(st3)
            mycon.commit()
            print("Successfully Deleted Specified Value")

        elif(ask=='N'):
            pass

        else:
            print("---INVALID INPUT!---")
            print("Operation Incomplete")
            print("Starting again......")
            Delete()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 7 : FOR APPLYING THE FINAL CHANGES TO THE EMPLOYEE TABLE AND SAVING IT AS TEXT FILE

def Save():
    
    fileobj=open("EmployeeDB.txt","w")
    
    data=resize()
    m=len(data)
    
    a="   |   "

    for i in range(m):
        fileobj.write(a.join(data[i])+a+'\n')
        if(i==0):
        	fileobj.write('\n')
    fileobj.flush()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#MAIN
#PROGRAM FOR MENU OF CHOICES TO PERFORM CERTAIN OPERATIONS ON THE EMPLOYEE TABLE

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="2140088",database="python")

if(mycon.is_connected()):
    print("")
    print("SUCCESFULLY CONNECTED TO THE InfoTech Company DATABASE")

else:
    print("ERROR CONNECTING TO DATABASE!")
    print(" PLEASE RESTART THE PROGRAM  ")

"""cursor9=mycon.cursor()
cursor9.execute("INSERT INTO EMSemployee VALUES(4,'2003-09-12','Rahul','Kumar','M','IT',200000)")
mycon.commit()"""
    
print("")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")

print("WELCOME TO THE EMPLOYEE MANAGEMENT SYSTEM OF InfoTech Company Pvt Ltd")
print("")

print("Enter your input according to the operation you want to perform :")
print("")

z=1
while(z!=0):
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")

    print("Enter 1 to view the Employee table")
    print("")
    print("Enter 2 to add a new row in the table")
    print("")
    print("Enter 3 to update existing records in the table")
    print("")
    print("Enter 4 to delete an existing record")
    print("")
    print("Enter 0 to exit the program and save the table in a text file")
    
    print("")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("")

    z=int(input("Enter your choice: "))
    print("")

    if(z==1):
        viewDB()
    elif(z==2):
        Add()
    elif(z==3):
        Update()
    elif(z==4):
        Delete()
    elif(z==0):
        pass
    else:
        print("  INVALID CHOICE!  ")
        print("PLEASE SELECT AGAIN")

print("Closing the table and exitting the program..........")
print("")
print("PLEASE WAIT WHILE CHANGES ARE BEING SAVED...........")
print("")

Save()
print("-----------SUCCESSFULLY SAVED AS TXT FILE-----------")



