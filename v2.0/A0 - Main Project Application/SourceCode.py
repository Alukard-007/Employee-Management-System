#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def viewScreen():
    global emp_data
    empL=resize(emp_data)
    mylist.delete(0,END)

    for line in range(len(empL)):
        row="|".join(empL[line])
        mylist.insert(END,row)
        if(line==0):
            mylist.insert(END,"========================================================================")

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
        newl.append(f.center(maxv))
    return tuple(newl)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 2 : CONVERTS ALL TABLE DATA INTO STRING AND SENDS TO addblanks() METHOD FOR CENTRAL ALIGNMENT AND THEN FINALLY RETURNS A LIST OF ALL COLUMNS AND THEIR VALUES
def resize(dataList):
    #global r
    r=len(dataList)

    eidl=list()
    dobl=list()
    fnl=list()
    lnl=list()
    genl=list()
    depl=list()
    sall=list()

    eidl.append(" EID ")
    dobl.append("DOB")
    fnl.append(" FirstName ")
    lnl.append(" LastName ")
    genl.append(" Gender ")
    depl.append(" Department ")
    sall.append("  Salary  ")

    for g in range(r):
        eidl.append(str(dataList[g][0]))
        dobl.append(str(dataList[g][1]))
        fnl.append(str(dataList[g][2]))
        lnl.append(str(dataList[g][3]))
        genl.append(str(dataList[g][4]))
        depl.append(str(dataList[g][5]))
        sall.append(str(dataList[g][6]))

    eidr=addblanks(eidl)
    dobr=addblanks(dobl)
    fnr=addblanks(fnl)
    lnr=addblanks(lnl)
    genr=addblanks(genl)
    depr=addblanks(depl)
    salr=addblanks(sall)
                    
    final_data=list()

    for t in range(r+1):

        row=list()

        row.append(eidr[t])
        row.append(dobr[t])
        row.append(fnr[t])
        row.append(lnr[t])
        row.append(genr[t])
        row.append(depr[t])
        row.append(salr[t])
        
        final_data.append(row)

    return final_data
#------------------------------------------------------------------------------------------------------------------------------------
#METHOD 3 : PRINTS THE EMPLOYEE TABLE FROM DATABASE IN TABULAR FORM
def viewDB(dataList):
    data=resize(dataList)
    m=len(data)
    
    l1=data[0]
    n1=0
    for i in l1:
    	n1=n1+(len(i))
    n1=n1+(7*(len('    |    ')))-(((len('    |    ')+0)//2))+(5)
    
    divider="-"*n1  	
    print(divider)
    
    a="    |    "

    for i in range(m):
        print(a[4:],end='')
        print(a.join(data[i]),end=a)
        print("")
        print(divider)
        if(i==0):
        	print(divider)

#--------------------------------------------------------------------------------------------------------------------------------------
#METHOD : To Provide Seaching Functionality Within The Employee DataBase
def Search(entry):
    if(srcBtn["state"]=="normal"):
        viewScreen()
        srcBtn["state"]="disabled"
        addBtn["state"]="disabled"
        updBtn["state"]="disabled"
        delBtn["state"]="disabled"
        sch1=Label(root,text="Please select the ",font=("Franklin Gothic Book","16"),bg="#263D42",fg="white")
        sch1.place(x=7,y=318)
        sch2=Label(root,text="Field of Search :",font=("Franklin Gothic Book","18"),bg="#263D42",fg="white",bd=.01)
        sch2.place(x=7,y=343)

        r=StringVar()
        def searchHit(entry):
            viewScreen()
            global emp_data
            global mode
            item=schEnt.get()
            fields=list()
            result=list()
            for j in resize(emp_data)[0]:
                fields.append(j.strip())
            
            cont=0
            for i in range(len(emp_data)):
                val=emp_data[i][fields.index(column)]
                if(val.casefold()==item.casefold()):
                    result.append(emp_data[i])
                    cont=cont+1
            if(cont>0):
                text="Found "+str(cont)+" value/s ↑"
                info.delete(0)
                info.insert(END,text)
                result=resize(result)
                mylist.delete(0,END)

                for line in range(len(result)):
                    row="|".join(result[line])
                    mylist.insert(END,row)
                    if(line==0):
                        mylist.insert(END,"========================================================================")
            else:
                info.delete(0)
                info.insert(END,"No Such Values Found In The Table !")
            schEnt.destroy()
            schBtn.destroy()
            sch3.destroy()
            sch4.destroy()
            #print(mode)
            if(mode[0]=="admin"):
                srcBtn["state"]="normal"
                addBtn["state"]="normal"
                updBtn["state"]="normal"
                delBtn["state"]="normal"

        def srch(field):
            eidRB.destroy()
            dobRB.destroy()
            fnRB.destroy()
            lnRB.destroy()
            genRB.destroy()
            deptRB.destroy()
            salRB.destroy()
            sch1.destroy()
            sch2.destroy()
            text="for",field,":"
            global sch3,sch4

            info.delete(0)
            info.insert(END,"←Enter The Value That Needs To Be Searched")
            
            sch3=Label(root, text ='Enter the search term',font = ("Franklin Gothic Book","14"),fg="white",bg="#263D42")
            sch3.place(x=10,y=320)
            sch4=Label(root, text =text,font = ("Franklin Gothic Book","14"),fg="white",bg="#263D42")
            sch4.place(x=10,y=343)

            global schEnt,schBtn,column
            column=field

            schEnt=Entry(root,state='normal',width=30)
            schEnt.place(x=10,y=383)
            item=schEnt.get()

            schBtn=Button(root,text="Search",font=("Helvetica",13),state="normal")
            schBtn.place(x=60,y=417)
            schBtn.bind("<Button-1>",searchHit)

        #root.create_rectangle(10,355,20,365,fill="Black")
        eidRB=Radiobutton(root,text="EID",variable=r,value="EID",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        eidRB.place(x=10,y=373)
        dobRB=Radiobutton(root,text="DOB",variable=r,value="DOB",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        dobRB.place(x=10,y=393)
        fnRB=Radiobutton(root,text="FirstName",variable=r,value="FirstName",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        fnRB.place(x=10,y=413)
        lnRB=Radiobutton(root,text="LastName",variable=r,value="LastName",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        lnRB.place(x=10,y=433)
        genRB=Radiobutton(root,text="Gender",variable=r,value="Gender",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        genRB.place(x=10,y=453)
        deptRB=Radiobutton(root,text="Department",variable=r,value="Department",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        deptRB.place(x=10,y=473)
        salRB=Radiobutton(root,text="Salary",variable=r,value="Salary",font=("Helvetica","13"),bg="#263D42",fg="white",activeforeground="cyan",activebackground="#263D42",command=lambda:srch(r.get()))
        salRB.place(x=10,y=493)
        info.delete(0)
        info.insert(END,"←Select The Field For Searching")
        
        	
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 4 : FOR INSERTION OF NEW VALUES INTO THE EMPLOYEE TABLE
def submit(entry):
    if(sbmitbtn["state"]=="normal"):
        global emp_data
        global rowID
        global fkey
        global mode
        sbmitbtn["state"]="disabled"

        if(fkey=="Delete"):
            emp_data.pop(rowID)
            e1.delete(0,END)
            viewScreen()
            Save()
            e1.config(state="disabled")
            srcBtn["state"]="normal"
            addBtn["state"]="normal"
            updBtn["state"]="normal"
            delBtn["state"]="normal"
            empTestList=resize(emp_data)
            if(len(empTestList)==1):
                updBtn["state"]="disabled"
                delBtn["state"]="disabled"
            err1.config(fg='#263D42')
            e1H.config(fg='grey')
            return
        
        row=list()
        row.append(e1.get().strip())
        e1.delete(0,END)
        row.append(e2.get().strip())
        e2.delete(0,END)
        row.append(e3.get().strip())
        e3.delete(0,END)
        row.append(e4.get().strip())
        e4.delete(0,END)
        row.append(e5.get().strip())
        e5.delete(0,END)
        row.append(e6.get().strip())
        e6.delete(0,END)
        row.append(e7.get().strip())
        e7.delete(0,END)

        if(rowID!=-1):
            for i in range(1,7,1):
                if(row[i]!="*s"):
                    #original_row.append(emp_data[row_index][i])
                    emp_data[rowID][i]=row[i]
        else:
            emp_data.append(row)

        
        Save()
        viewScreen()
        #print(emp_data)

        e1.config(state="disabled")
        e2.config(state="disabled")
        e3.config(state="disabled")
        e4.config(state="disabled")
        e5.config(state="disabled")
        e6.config(state="disabled")
        e7.config(state="disabled")

        srcBtn["state"]="normal"
        addBtn["state"]="normal"
        updBtn["state"]="normal"
        delBtn["state"]="normal"

        empTestList=resize(emp_data)
        if(len(empTestList)==1):
            updBtn["state"]="disabled"
            delBtn["state"]="disabled"

        err1.config(fg='#263D42')
        e1H.config(fg='grey')
        err2.config(fg='#263D42')
        e2H.config(fg='grey')
        err3.config(fg='#263D42')
        e3H.config(fg='grey')
        err4.config(fg='#263D42')
        e4H.config(fg='grey')
        err5.config(fg='#263D42')
        e5H.config(fg='grey')
        err6.config(fg='#263D42')
        e6H.config(fg='grey')
        err7.config(fg='#263D42')
        e7H.config(fg='grey')

        info.delete(0,END)

def takeInput(AorU):
    global Updtn
    def validater():
        try:
            eid_col=list()
            global emp_data
            for i in emp_data:
                eid_col.append(int(i[0]))
            eidChk=e1.get().isdigit() and (int(e1.get()) not in eid_col) and len(e1.get())<=3
            #print(eidChk)
            dobChk=e2.get()[4]==e2.get()[7]=="-" and e2.get()[:4].isdigit() and e2.get()[5:7].isdigit() and e2.get()[8:].isdigit() and len(e2.get())==10
            fnChk=e3.get().isalpha() and (len(e3.get())<=10)
            #print(fnChk)
            lnChk=e4.get().isalpha() and (len(e4.get())<=10)
            #print(lnChk)
            genChk=e5.get().upper()=="M" or e5.get().upper()=="F"
            #print(genChk)
            depChk=e6.get().isalpha() and (len(e6.get())<=10)
            #print(depChk)
            salChk=e7.get().isdigit() and (len(e7.get())<=6)
            #print(salChk)
            if(eidChk==True and dobChk==True and fnChk==True and lnChk==True and genChk==True and depChk==True and salChk==True):
                sbmitbtn["state"]="normal"

            global Updtn
            #print(Updtn)
            if(Updtn):
                dobU=dobChk or (e2.get().strip()=='*s')
                fnU=fnChk or (e3.get()=='*s')
                lnU=lnChk or (e4.get()=='*s')
                genU=genChk or (e5.get()=='*s')
                depU=depChk or (e6.get()=='*s')
                salU=salChk or (e7.get()=='*s')

                if(dobU==True and fnU==True and lnU==True and genU==True and depU==True and salU==True):
                    sbmitbtn["state"]="normal"
            else:
                pass
                #print("No")
        except:
            pass
    def myUpd2(*args):
        val = e2.get().strip()
        e2H.config(fg='grey')
        err2.config(fg='red')
        dobChk=False
        if(len(val)==10):
            dobChk=val[4]==val[7]=="-" and val[:4].isdigit() and val[5:7].isdigit() and val[8:].isdigit()
        if(dobChk):
            err2.config(fg='#263D42')
            info.delete(0,END)
            validater()
        elif(Updtn==True and val=="*s"):
            validater()
            err2.config(fg='#263D42')
            #sbmitbtn["state"]="normal"
            info.delete(0,END)
        else:
            e2H.config(fg='red')
            sbmitbtn["state"]="disabled"
    dobstr.trace('w',myUpd2)

    def myUpd3(*args):
        info.delete(0,END)
        val = e3.get()
        err3.config(fg='red')
        e3H.config(fg='grey')
        global fnChk
        fnChk=val.isalpha() and (len(val)<=10)
        if(fnChk):
            err3.config(fg='#263D42')
            validater()
        elif(Updtn and val=="*s"):
            err3.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        else:
            info.delete(0,END)
            info.insert(END,"Please Enter First Name Only Without Whitespaces and Numbers")
            e3H.config(fg='red')
            sbmitbtn["state"]="disabled"
    fnstr.trace('w',myUpd3)

    def myUpd4(*args):
        info.delete(0,END)
        val = e4.get()
        e4H.config(fg='grey')
        err4.config(fg='red')
        global lnChk
        lnChk=val.isalpha() and (len(val)<=10)
        if(lnChk):
            err4.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        elif(Updtn and val=="*s"):
            err4.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        else:
            info.delete(0,END)
            info.insert(END,"Please Enter Last Name Only Without Whitespaces and Numbers")
            e4H.config(fg='red')
            sbmitbtn["state"]="disabled"
    lnstr.trace('w',myUpd4)

    def myUpd5(*args):
        val = e5.get()
        err5.config(fg='red')
        e5H.config(fg='grey')
        global genChk
        genChk=val=="M" or val=="F"
        if(genChk):
            err5.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        elif(Updtn==True and val=="*s"):
            err5.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        else:
            e5H.config(fg='red')
            sbmitbtn["state"]="disabled"
    genstr.trace('w',myUpd5)

    def myUpd6(*args):
        info.delete(0,END)
        val = e6.get()
        err6.config(fg='red')
        e6H.config(fg='grey')
        global depChk
        depChk=val.isalpha() and (len(val)<=10)
        if(depChk):
            err6.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        elif(Updtn and val=="*s"):
            err6.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
        else:
            info.delete(0,END)
            info.insert(END,"Please Enter Department Name Without Whitespaces and Numbers")
            e6H.config(fg='red')
            sbmitbtn["state"]="disabled"
    deptstr.trace('w',myUpd6)

    def myUpd7(*args):
        val = e7.get()
        err7.config(fg='red')
        e7H.config(fg='grey')
        global salChk
        salChk=val.isdigit() and (len(val)<=6)
        if(salChk):
            err7.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
            info.delete(0,END)
        elif(Updtn and val=="*s"):
            err7.config(fg='#263D42')
            validater()
            #sbmitbtn["state"]="normal"
            info.delete(0,END)
        else:
            e7H.config(fg='red')
            sbmitbtn["state"]="disabled"

    salstr.trace('w',myUpd7)
    
    sbmitbtn.bind("<Button-1>",submit)

def Add(entry):
    if(addBtn["state"]=="normal"):
        viewScreen()
        srcBtn["state"]="disabled"
        updBtn["state"]="disabled"
        delBtn["state"]="disabled"
        
        e1.config(state="normal")
        e2.config(state="normal")
        e3.config(state="normal")
        e4.config(state="normal")
        e5.config(state="normal")
        e6.config(state="normal")
        e7.config(state="normal")

        info.delete(0)
        info.insert(END,"Enter The Data Of The Employee→")
        info.insert(END,"Click Submit After Entering All Required Values→")

        new_row=list()
        eid_col=list()
        global emp_data
        global empdb_bak
        global fkey
        fkey="Add"
        global Updtn
        Updtn=False
            
        for i in emp_data:
                eid_col.append(int(i[0]))
        #print(eid_col)
        
        def myUpd1(*args):
            val = e1.get()
            info.delete(0,END)
            e1H.config(fg='grey')
            err1.config(fg="red")
            try:
                if(int(val) in eid_col):
                    info.delete(0,END)
                    info.insert(END,"EID Already In Use !")
            except:
                pass
            if(val.isdigit() and (int(val) not in eid_col) and len(val)<=3):
                #sbmitbtn["state"]="normal"
                err1.config(fg='#263D42')
                Updtn=False
            else:
                e1H.config(fg='red')
                sbmitbtn["state"]="disabled"
        eidstr.trace('w',myUpd1)
        global rowID
        rowID=-1
        takeInput(Updtn)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 5 : FOR UPDATION OF SPECIFIED ROWS FROM THE EMPLOYEE TABLE

def Update(entry):
    if(updBtn["state"]=="normal"):
        viewScreen()
        glist=globals()
        global emp_data
        global empdb_bak
        original_row=list()

        srcBtn["state"]="disabled"
        addBtn["state"]="disabled"
        delBtn["state"]="disabled"

        e1.config(state="normal")
        e2.config(state="normal")
        e3.config(state="normal")
        e4.config(state="normal")
        e5.config(state="normal")
        e6.config(state="normal")
        e7.config(state="normal")

        info.delete(0)
        info.config(font=("Helvetica",15))
        info.insert(END,"Enter The Data Of The Employee→")
        info.insert(END,"In Case A Value Doesnt Need Updation,Then Type '*s' To Retain Its Original Value")

        new_row=list()
        eid_col=list()
        eid_index=list()
        global emp_data
        global empdb_bak
        global fkey
        fkey="Update"
        #global rowID
        global eidChk
        eidChk=False
        global Updtn
        Updtn=True
            
        for i in emp_data:
                eid_col.append(int(i[0]))
                eid_index.append(emp_data.index(i))
        
        def myUpd1(*args):
            val = e1.get()
            info.delete(0,END)
            err1.config(fg='red')
            e1H.config(fg='grey')
            try:
                if(int(val) not in eid_col):
                    info.delete(0,END)
                    info.insert(END,"No Record Present With This EID !")
            except:
                pass
            if(val.isdigit() and (int(val) in eid_col) and len(val)<=3):
                eidChk=True
                err1.config(fg='#263D42')
                #sbmitbtn["state"]="normal"
                global rowID
                rowID=eid_index[(eid_col.index(int(val)))]
                original_row.append(int(val))
            else:
                e1H.config(fg='red')
                sbmitbtn["state"]="disabled"
        eidstr.trace('w',myUpd1)
        
        takeInput(Updtn)
        #info.delete(0)
        #info.delete(0)
        #info.config(font=("Helvetica",18))
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 6 : FOR DELETION OF SPECIFIED ROW FROM THE EMPLOYEE TABLE

def Delete(entry):
    viewScreen()
    if(delBtn["state"]=="normal"):
        global emp_data
        global empdb_bak
        eid_col=list()
        eid_index=list()
        global fkey
        fkey="Delete"

        srcBtn["state"]="disabled"
        addBtn["state"]="disabled"
        updBtn["state"]="disabled"

        info.delete(0)
        info.insert(END,"Enter The EID Of The Employee Whose Details Are To Be Deleted→")

        e1.config(state="normal")

        for i in emp_data:
            eid_col.append(int(i[0]))
            eid_index.append(emp_data.index(i))

        def myUpd1(*args):
            val = e1.get()
            info.delete(0,END)
            err1.config(fg='red')
            e1H.config(fg='grey')
            try:
                if(int(val) not in eid_col):
                    info.delete(0,END)
                    info.insert(END,"No Record Present With This EID !")
            except:
                pass
            if(val.isdigit() and (int(val) in eid_col) and len(val)<=3):
                err1.config(fg='#263D42')
                sbmitbtn["state"]="normal"
                rowID=eid_index[(eid_col.index(int(val)))]
                #original_row.append(int(val))
            else:
                e1H.config(fg='red')
                sbmitbtn["state"]="disabled"
        eidstr.trace('w',myUpd1)
        
        sbmitbtn.bind("<Button-1>",submit)
        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#METHOD 7 : FOR APPLYING THE FINAL CHANGES TO THE EMPLOYEE TABLE AND SAVING IT AS TEXT FILE

def Save():
    
    fileobj=open("EmployeeDB.txt","w")
    
    data=resize(emp_data)
    dataDEC=list()
    encryptedList=list()

    for i in range(len(data)):
        for j in range(7):
            data[i][j]=data[i][j].strip()
    
    m=len(data)
    
    a=","

    for i in range(1,m,1):
        dataDEC.append(a.join(data[i]))
        fileobj.write(a.join(data[i])+'\n')

    fileobj.flush()
    fileobj.close()

    fileENC=open("EncryptedDB.txt","w")

    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;,_-/ 0123456789"
    for j in dataDEC:
        encrypt=''
        for i in j:
            position=letters.find(i)
            newposition=(position+5)%68
            encrypt +=letters [newposition]
        fileENC.write(encrypt+'\n')  

    fileENC.flush()
    fileENC.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
def CreateUser(Entry):
    if(addUser["state"]=="normal"):
        userEntry.delete(0,END)
        passEntry.delete(0,END)
        addUser["state"]="disabled"
        OK["state"]="disabled"
        uH=Label(root, text ="Create Usernames Ending With '@employee'/'@admin'",font = ("Courier","10"),fg="white",bg="#263D42")
        uH.place(x=178,y=223)
        uH2=Label(root, text ="*",font = ("Courier","16"),fg="red",bg="#263D42")
        uH2.place(x=160,y=223)
        pH=Label(root, text ='Password Min Length : 5 | Max Length : 10',font = ("Courier",11),fg="white",bg="#263D42")
        pH.place(x=178,y=308)
        pH2=Label(root, text ="*",font = ("Courier","16"),fg="red",bg="#263D42")
        pH2.place(x=160,y=308)
        #name=userEntry.get()
        #passwd=passEntry.get()
        idPass=list()
        global mode
        fObj=open("IdPass.txt",'r')
        idPassData=fObj.readlines()

        for i in idPassData:
            row=i.rstrip('\n').split(',')
            idPass.append(row)

        ids=list()
        for i in idPass:
            ids.append(i[0])

        def OKip(Entry):
            if(OK["state"]=="normal"):
                name=userEntry.get()
                passwd=passEntry.get()
                file=open("IdPass.txt","a")
                file.write("\n"+name+","+passwd)
                file.flush()
                file.close()
                LOGinfo.delete(0,END)
                LOGinfo.insert(END,"       New Username Saved Successfully")
                uH.destroy()
                uH2.destroy()
                pH.destroy()
                pH2.destroy()
                addUser["state"]="normal"
                OK.bind("<Button-1>",OKhit)

        def IPvalid():
            name=userEntry.get()
            passwd=passEntry.get()
            a=name[-6:]=="@admin" or name[-9:]=="@employee"
            if(name not in ids and a and len(passwd)>=5 and len(passwd)<=10):
                OK["state"]="normal"
                OK.bind("<Button-1>",OKip)

        def idCheck(*args):
            LOGinfo.delete(0,END)
            uH2.config(fg="red")
            name=userEntry.get()
            if(name not in ids and (name[-6:]=="@admin" or name[-9:]=="@employee")):
                uH2.config(fg="green")
                IPvalid()
                #OK["state"]="normal"
                LOGinfo.delete(0,END)
            elif(name in ids):
                OK["state"]="disabled"
                LOGinfo.delete(0,END)
                LOGinfo.insert(END,"                Username Already Taken")
            else:
                OK["state"]="disabled"
        userStr.trace('w',idCheck)

        def passCheck(*args):
            pH2.config(fg="red")
            global passwd
            passwd=passEntry.get()
            if(len(passwd)>=5 and len(passwd)<=10):
                pH2.config(fg="green")
                IPvalid()
                #OK["state"]="normal"
                LOGinfo.delete(0,END)
            else:
                OK["state"]="disabled"
                LOGinfo.delete(0,END)
                LOGinfo.insert(END,"   Password Min Length : 5 | Max Length : 10")
        passStr.trace('w',passCheck)

def OKhit(Entry):
    if(OK["state"]=="normal"):
        name=userEntry.get()
        passwd=passEntry.get()
        idPass=list()
        global mode
        fObj=open("IdPass.txt",'r')
        idPassData=fObj.readlines()

        for i in idPassData:
            row=i.rstrip('\n').split(',')
            idPass.append(row)

            #print(idPass)
        present="absent"
        for i in idPass:
            if(name==i[0]):
                present="Yes"
                if(passwd==i[1]):
                    #print("ID Pass Match")
                    global mode
                    if(name[-5:]=="admin"):
                        mode.append("admin")
                        root.destroy()
                    elif(name[-8:]=="employee"):
                        mode.append("employee")
                        root.destroy()
                else:
                    LOGinfo.delete(0,END)
                    LOGinfo.insert(END,"                     Invalid Password !")
        if(present=="absent"):
            LOGinfo.delete(0,END)
            LOGinfo.insert(END,"                     Invalid Username !")
#--------------------------------------------------------------------------------------------------------------------------------
#MAIN
#PROGRAM FOR MENU OF CHOICES TO PERFORM CERTAIN OPERATIONS ON THE EMPLOYEE TABLE
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;,_-/ 0123456789"
encryptedList=list()
emp_data=list()
"""
fileobj=open("EmployeeDB.txt",'r')
csv_data=fileobj.readlines()

for i in csv_data:
    row=i.rstrip('\n').split(',')
    emp_data.append(row)"""

fileobj=open("EncryptedDB.txt","r")
csv_data=fileobj.readlines()

for i in csv_data:
    row=i.rstrip('\n')
    encryptedList.append(row)

for j in encryptedList:
    decrypt=''
    for i in j:
        pos=letters.find(i)
        newpos=(pos-5)%68
        decrypt +=letters [newpos]
    row=decrypt.split(',')
    emp_data.append(row)
fileobj.close()    
#print(emp_data)

empdb_bak=emp_data

rowID=-1
fkey=""
Updtn=False
mode=list()

#===============================LOGIN INTERFACE


from tkinter import simpledialog
from tkinter import *

root = Tk()
root.title("Employee Management System | Login")
root.geometry("720x550")
root.resizable(height="false",width="false")
root.config(bg="#263D42")
Label(root, text ='InfoTech Company Pvt Ltd',font = ("Dubai","28","bold"),fg="white",bg="#263D42").pack()
Label(root, text ='(since 2021,i.e when the project was assigned)',font = ("Courier",18),fg="white",bg="#263D42").place(x=34,y=50)
Label(root, text ='Employee Management System',font = ("Helvetica","28","bold"),fg="white",bg="#263D42").place(x=77,y=100)    #107,98
Label(root, text ='managed by Ahmedabad University',font = ("Courier",13),fg="white",bg="#263D42").place(x=200,y=515)
Label(root, text="Enter Username :", font=("Helvetica",17),fg='white',bg='#263D42').place(x=178,y=197)
Label(root, text ='Suggested : guest@admin / guest@employee',font = ("Courier","11"),fg="white",bg="#263D42").place(x=178,y=223)
userStr=StringVar(root)
userEntry=Entry(root,textvariable=userStr,width=57)
userEntry.place(x=180,y=248)
Label(root, text="Enter Password :", font=("Helvetica",17),fg='white',bg='#263D42').place(x=178,y=282)
Label(root, text ='Suggested : admin@123 / emp@123',font = ("Courier",11),fg="white",bg="#263D42").place(x=178,y=308)
passStr=StringVar(root)
passEntry=Entry(root,textvariable=passStr,width=57)
passEntry.place(x=180,y=333)
LOGinfo = Listbox(root,font=("Serif",16),bd=5,fg="white",bg="#263D52")
LOGinfo.place(height=37,width=450,x=136,y=450)
LOGinfo.insert(END,"          Enter Login Details To Continue")

OK = Button(root, text = "Submit",activebackground = "cyan", activeforeground = "black")
OK.place(x = 479, y = 389)
OK.bind("<Button-1>",OKhit)

addUser = Button(root, text = "Create New User ID",activebackground = "cyan", activeforeground = "black")
addUser.place(x = 179, y = 389)
addUser.bind("<Button-1>",CreateUser)


root.mainloop()
#========================MAIN INTERFACE=============================
if(len(mode)!=0):
    root = Tk()
    root.title("Employee Management System | Ahmedabad University")
    root.geometry("1280x550")
    root.resizable(height="false",width="false")
    root.config(bg="#263D42")

    w = Label(root, text ='Employee Management System | InfoTech Company Pvt Ltd',font = ("Dubai","20","bold"),fg="white",bg="#263D42")
    w.pack()

    scroll_bar = Scrollbar(root)

    mylist = Listbox(root,yscrollcommand = scroll_bar.set,font=("courier",14,'bold'),bd=5,fg="black",bg="cyan")
    empL=resize(emp_data)

    for line in range(len(empL)):
        row="|".join(empL[line])
        mylist.insert(END,row)
        if(line==0):
                mylist.insert(END,"========================================================================")

    mylist.place(height=360,width=795,x=225,y=50)
    scroll_bar.place(x=1020,y=50,height=360)

    scroll_bar.config( command = mylist.yview )

    info = Listbox(root,font=("Helvetica",18),bd=5,fg="white",bg="#263D52")
    info.place(height=69,width=813,x=225,y=450)

    #---------------------------------------
    #entrybg = Listbox(root,bd=3,fg="black",bg="#263D42",height=29,width=35).place(x=1070,y=46)

    eid = Label(root, text = "Enter EID :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 50)    
    eidstr=StringVar(root)
    e1 = Entry(root,textvariable=eidstr, state='disabled')
    e1.place(x = 1090, y = 90)
    err1 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err1.place(x=1080, y=48)
    e1H = Label(root, text ='Format→digits[Max:3]',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e1H.place(x=1090, y=68)

    dob = Label(root,text = "Enter DOB :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 113)     
    dobstr=StringVar(root)
    e2H = Label(root, text ='Format→YYYY-MM-DD',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e2H.place(x=1090, y=131)
    err2 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err2.place(x=1080, y=111)
    e2 = Entry(root,textvariable=dobstr,state='disabled')
    e2.place(x = 1090, y = 153)

    fn = Label(root, text = "Enter First Name :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 176)    
    fnstr=StringVar(root)
    e3H = Label(root, text ='Format→string[Max:10]',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e3H.place(x=1090, y=194)
    err3 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err3.place(x=1080, y=174)
    e3 = Entry(root,textvariable=fnstr, state='disabled')
    e3.place(x = 1090, y = 216)

    ln = Label(root, text = "Enter Last Name :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 239)
    lnstr=StringVar(root)
    e4H = Label(root, text ='Format→string[Max:10]',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e4H.place(x=1090, y=257)
    err4 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err4.place(x=1080, y=237)
    e4 = Entry(root,textvariable=lnstr,state='disabled')
    e4.place(x = 1090, y = 279)

    gen = Label(root, text = "Enter Gender :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 302)
    genstr=StringVar(root)
    e5H = Label(root, text ='Format→M/F',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e5H.place(x=1090, y=320)
    err5 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err5.place(x=1080, y=300)
    e5 = Entry(root,textvariable=genstr,state='disabled')
    e5.place(x = 1090, y = 342)

    dept = Label(root, text = "Enter Department :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 365)
    deptstr=StringVar(root)
    e6H = Label(root, text ='Format→string[Max:10]',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e6H.place(x=1090, y=383)
    err6 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err6.place(x=1080, y=363)
    e6 = Entry(root,textvariable=deptstr,state='disabled')
    e6.place(x = 1090, y = 405)

    sal = Label(root, text = "Enter Salary :", font=("Helvetica",13,'bold'),bg="#263D42",fg="white").place(x=1090,y = 428)
    salstr=StringVar(root)
    e7H = Label(root, text ='Format→digits[Max:6]',font = ("Helvetica",10),fg="grey",bg="#263D42")
    e7H.place(x=1090, y=446)
    err7 = Label(root, text ='!',font = ("Helvetica",14,'bold'),fg="#263D42",bg="#263D42")
    err7.place(x=1080, y=426)
    e7 = Entry(root,textvariable=salstr,state='disabled')
    e7.place(x = 1090, y = 468)

    sbmitbtn = Button(root, text = "Submit",activebackground = "cyan", activeforeground = "black",state="disabled")
    sbmitbtn.place(x = 1090, y = 500)  

    #---------------------------------------------
    menubg = Listbox(root,bd=3,fg="black",bg="#263D52",height=16,width=27).place(x=-2,y=49)

    label1 = Label(root, text = "Main Menu", font=("Dubai",20,'bold'),bg="#263D52",fg="white").place(x=10,y=50)

    srcBtn = Button(root, text = "Search Row", font = "20",anchor='center',width=12,bd=3)
    srcBtn.place(x=10,y=100)
    srcBtn.bind("<Button-1>",Search)

    addBtn = Button(root, text = "Add New Row", font = "20",width=12,anchor='center',bd=3)
    addBtn.place(x=10,y=150)
    addBtn.bind("<Button-1>",Add)

    updBtn = Button(root, text = "Update A Row", font = "20",width=12,anchor='center',bd=3)
    updBtn.place(x=10,y=200)
    updBtn.bind("<Button-1>",Update)

    delBtn = Button(root, text = "Delete Row", font = "20",width=12,anchor='center',bd=3)
    delBtn.place(x=10,y=250)
    delBtn.bind("<Button-1>",Delete)

    empTestList=resize(emp_data)
    if(mode[0]=="admin" and len(empTestList)==1):
        updBtn["state"]="disabled"
        delBtn["state"]="disabled"
    if(mode[0]=="employee"):
        addBtn["state"]="disabled"
        updBtn["state"]="disabled"
        delBtn["state"]="disabled"
    root.mainloop()

#====================================================================================================================================

