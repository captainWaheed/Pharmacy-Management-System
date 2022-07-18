# Final Project
# Username : Admin/admin/ADMIN
# Password : 111

from datetime import datetime
from tkinter import*
import random
import time

def main(): #..................mainloop for the execution of each event called
    root=Tk()
    app=Window1(root)

class Window1:

    def __init__(self,master):
        self.master=master
        self.master.title("PHARMACY")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg="white")
        self.frame=Frame(self.master)
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame,font=("arial",50,"bold",),text="PHARMACY",bd=20)
        self.lblTitle.grid(row=0,column=0,columnspan=2,pady=40)

        self.login1=Frame(self.frame,width=1010,height=300,relief="ridge",bd=20)
        self.login1.grid(row=1,column=0)

        self.login2=Frame(self.frame,width=1000,height=100,relief="ridge",bd=20)
        self.login2.grid(row=2,column=0)

        self.login3=Frame(self.frame,width=1000,height=200,relief="ridge",bd=20)
        self.login3.grid(row=3,column=0)

        #............................................................................................................................#

        labels = ["Username" , "Password"] #...................... LIST

        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(self.login1,font=("arial",30,"bold",),text=labels[i],bd=22)
            self.cur_label.grid(row=i,column=0)

        entry_box = {"Username": self.Username,"Password": self.Password} #.....................DICTIONARY

        counter = 0

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(self.login1,font=("arial",30,"bold"),bd=22,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=1,padx=85)
            if counter==1:
                self.cur_entrybox.config(show="*")
            counter += 1

        

        #............................................................................................................................#

        self.btnlogin=Button(self.login2,text="Login",width=17,font=("arial",20,"bold"),command=self.LoginSystem)
        self.btnlogin.grid(row=0,column=0)

        self.btnReset=Button(self.login2,text="Reset",width=17,font=("arial",20,"bold"),command=self.Reset)
        self.btnReset.grid(row=0,column=1)

        self.btnExit=Button(self.login2,text="Exit",width=17,font=("arial",20,"bold"),command=self.iExit)
        self.btnExit.grid(row=0,column=2)

        #............................................................................................................................#

        self.btnReg=Button(self.login3,text="Patients Registerations",font=("arial",20,"bold"),state=DISABLED,command=self.Registeration_window)
        self.btnReg.grid(row=0,column=0,pady=8,padx=57)

        self.btnPhar=Button(self.login3,text="Pharmacy Management",font=("arial",20,"bold"),state=DISABLED,command=self.Pharmacy_window)
        self.btnPhar.grid(row=0,column=1,pady=8,padx=57)

        #.............................................................................................................................#
        
    def LoginSystem(self):
        user=(self.Username.get())
        password=(self.Password.get())

        if (user==str("ADMIN")) or (user==str("admin")) or (user==str("Admin")) and (password==str(111)):
            self.btnReg.config(state=NORMAL)
            self.btnPhar.config(state=NORMAL)

        else:
            tkinter.messagebox.askyesno("Hospital Management","Invalid username or password, please try again.")
            self.btnReg.config(state=DISABLED)
            self.btnPhar.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")

    def Reset(self):
        self.btnReg.config(state=DISABLED)
        self.btnPhar.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Hospital Management","Please confirm to exit!")
        if self.iExit>0:
            self.master.destroy()
        return

    #......................................................................................................................................#
    
    def Registeration_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=Window2(self.newwindow)

    def Pharmacy_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=Window3(self.newwindow)

    
        
class Window2:

    def __init__(self,master):
        self.master=master
        self.master.title("Patients Registerations")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="grey")
        self.frame=Frame(self.master)
        self.frame.pack()

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address= StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Ref = StringVar()
        Date= StringVar()
        
        

        Membership = StringVar()
        Membership.set("0")
        #------------------------Functions-----------------------
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Registrations","Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return
        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Date.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

        def iDelete():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Date.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)

            self.txtRecipt.delete("1.0",END)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Patient Registrations","Confirm if you want to Add a new record")
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtRecipt.delete("1.0",END)
                return
        
        def Ref_No():
            
            x = random.randint(1000,60000)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtRecipt.insert(END,"\t"+Ref.get()+"\t\t"+ Firstname.get() +"\t\t"+ Surname.get() +"\t\t"+ Address.get()+"\t\t"+DateofOrder.get()+"\t\t"+Telephone.get()+"\t\t"+Membership.get()+"\n")

        def Fees():
    

            if (var4.get()==1):
                self.txtMembership.configure(state=NORMAL)
                Item1 = float(500)
                Membership.set("Rs"+ str(Item1))
               
            elif (var4.get() ==0):
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")



        #-------------------------------Frame--------------------

        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, bd= 20, width=1350, padx=26,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame,font=('arial',59,'bold'),text="Patient Registrations",padx=2)
        self.lblTitle.grid()

        #-------------------------------LowerFrames---------------

        MemberDetailFrame = LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)

        MemberDetailFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailFrame, bd=10,width= 880, height= 400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)
        
        MembersName_F = LabelFrame(FrameDetails,bd=10,width= 350, height= 400,font=('arial',12,'bold'),text="Patient Name ", relief=RIDGE)
        MembersName_F.grid(row=0,column=0)

        Recipt_ButtonFrame = LabelFrame(MemberDetailFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Recipt_ButtonFrame.pack(side=RIGHT)

        #-----------------------------------------------------------

        self.lblReferenceNo = Label(MembersName_F,font=('arial',14,'bold'),text="Reference no.",bd=7)
        self.lblReferenceNo.grid(row=0,column=0,sticky=W)
        self.txtReferenceNo = Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=Ref,state=DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)

        self.lblDate = Label(MembersName_F,font=('arial',14,'bold'),text="Date",bd=7)
        self.lblDate .grid(row=6,column=0,sticky=W)
        self.txtDate  = Entry(MembersName_F,font=('arial',14,'bold'),bd=7,textvariable=DateofOrder,insertwidth=2)
        self.txtDate .grid(row=6,column=1)

        #-----------------------------------------------------------

        labels = ["Firstname" , "Surname" , "Address" , "Postcode" , "Telephone"] #............ LIST
        counter = 1

        for i in range(len(labels)): 
            self.cur_label = "label" + str(i)
            self.cur_label = Label(MembersName_F,font=('arial',14,'bold'),text=labels[i],bd=7)
            self.cur_label.grid(row=counter,column=0,sticky=W)
            counter += 1


        user_info = {"Firstname": Firstname , "Surname": Surname , "Address": Address , "Postcode": Postcode , "Telephone": Telephone} #........DICTIONARY
        counter=1
        for i in user_info:
            self.cur_entrybox = "entry" + i 
            self.cur_entrybox = Entry(MembersName_F,font=('arial',14,'bold'),bd=7,insertwidth=2,textvariable=user_info[i])
            self.cur_entrybox.grid(row = counter,column=1)
            counter += 1 




        

        #---------------------------------Member info--------------------------

        self.lblProve_of_ID = Label(MembersName_F,font=('arial',14,'bold'),text="Prove of ID",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)

        self.cboProve_of_ID=ttk.Combobox(MembersName_F,textvariable = var1,state='readonly',font=('arial',14,'bold'),width=19)
        self.cboProve_of_ID['value']= ('','Pilot Licence', 'Driving Licence','Passport','Student ID') #.............. Array
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)

        self.lblType_of_Member = Label(MembersName_F,font=('arial',14,'bold'),text="Patient Type",bd=7)
        self.lblType_of_Member.grid(row=8,column=0,sticky=W)

        self.cboType_of_Member=ttk.Combobox(MembersName_F,textvariable = var2,state='readonly',font=('arial',14,'bold'),width=19)
        self.cboType_of_Member['value']= ('','Full Member', 'Annual membership','Pay As You Go','Homorary Member') #............ Array
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)

        self.lblMethod_of_Payment = Label(MembersName_F,font=('arial',14,'bold'),text="Method of Payment",bd=7)
        self.lblMethod_of_Payment.grid(row=9,column=0,sticky=W)

        self.cboMethod_of_Payment=ttk.Combobox(MembersName_F,textvariable = var3,state='readonly',font=('arial',14,'bold'),width=19)
        self.cboMethod_of_Payment['value']= ('','Visa Card', 'Master Card','Debit card','Cash') #................. Array
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1)


        #-----------------------------Check Button------------------------------

        self.chkMembership = Checkbutton(MembersName_F,text="Fees", variable=var4,onvalue=1,offvalue= 0,font=('arial',16,'bold'),command=Fees).grid(row=10,column=0,sticky=W)

        self.txtMembership = Entry(MembersName_F,font=('arial',14,'bold'),textvariable=Membership, bd=7,insertwidth=2 ,state=DISABLED, justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)

        #------------------------------------Recipt ----------------------------------
        self.lblLable = Label(Recipt_ButtonFrame,font=('arial',10,'bold'),pady=10,text="Member Ref\t Firstname\t Surename\t Address\t\t Date Reg.\t Telephone\t Member Paid",bd=7)
        self.lblLable.grid(row=0,column=0,columnspan=4)

        self.txtRecipt = Text(Recipt_ButtonFrame,font=('arial',10,'bold'),height=22,width=112)
        self.txtRecipt.grid(row=1,column=0,columnspan=4)

        #------------------------------------Buttons-----------------------------
        self.btnRecipt = Button(Recipt_ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width=13,text="Receipt",command=Receipt).grid(row=2,column=0)

        self.btnReset = Button(Recipt_ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width=13,text="Reset",command=Reset).grid(row=2,column=1)

        self.btnExit = Button(Recipt_ButtonFrame,padx=18,bd=7,font=('arial',10,'bold'),width=13,text="Exit",command=iExit).grid(row=2,column=2)

        self.btnDelete = Button(Recipt_ButtonFrame,padx=18,text="Delete",font=("arial",10,"bold"),width=13,bd=7,command=iDelete).grid(row=2,column=3)

class Window3:

    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.master.configure(background="grey")
        self.frame=Frame(self.master)
        self.frame.pack()

        cmbTablets=StringVar()
        RefNo=StringVar()
        Dose=StringVar()
        IssueDate=StringVar()
        ExpDate=StringVar()
        SideEffects=StringVar()
        PatientID=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientAddress=StringVar()
        NHSNo=StringVar()
        StorageAdvice=StringVar()
        FurtherInformation=StringVar()
        UsingMachine=StringVar()
        Medication=StringVar()
        NoofTablets=StringVar()
        Lot=StringVar()
        Strength=StringVar()
        Prescription=StringVar()

        #.......................................................................................................................#

        def iExit():
            iExit=tkinter.messagebox.askyesno ("Pharmacy Management System", "Confirm if you want to exit")
            if iExit>0:
                self.master.destroy()
                return

        def iReset():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            

            return

        def iDelete():
            cmbTablets.set("")
            RefNo.set("")
            Dose.set("")
            IssueDate.set("")
            ExpDate.set("")
            SideEffects.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            NHSNo.set("")
            StorageAdvice.set("")
            FurtherInformation.set("")
            UsingMachine.set("")
            Medication.set("")
            NoofTablets.set("")
            Lot.set("")
            Strength.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return

        def iReceipt():

            self.txtFrameDetail.insert(END, cmbTablets.get()+"\t\t"+ RefNo.get()+"\t"+ Dose.get()+"\t\t"+NoofTablets.get() + "\t"+ Lot.get()+ "\t"+ IssueDate.get()+
                                       "\t\t"+ ExpDate.get() +"\t" + Strength.get() + "\t\t"+ StorageAdvice.get() + "\t"+ NHSNo.get() + "\t\t"+ PatientName.get()
                                       + "\t"+ DateOfBirth.get() +"\t"+ PatientAddress.get()+ "\n")

            return

        def iPrescription():
            self.txtPrescription.insert(END,"Name of Tablet: \t\t\t\t" + cmbTablets.get() + "\n")
            self.txtPrescription.insert(END,"Dose: \t\t\t\t" + Dose.get() + "\n")
            self.txtPrescription.insert(END,"Number of Tablets: \t\t\t\t" + NoofTablets.get() + "\n")
            self.txtPrescription.insert(END,"Lot: \t\t\t\t" + Lot.get() + "\n")
            self.txtPrescription.insert(END,"Issue Date: \t\t\t\t" + IssueDate.get() + "\n")
            self.txtPrescription.insert(END,"Exp. Date: \t\t\t\t" + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,"Strength: \t\t\t\t" + Strength.get() + "\n")
            self.txtPrescription.insert(END,"Possible Side Effects: \t\t\t\t" + SideEffects.get() + "\n")
            self.txtPrescription.insert(END,"Storage Advice: \t\t\t\t" + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,"NHS Number: \t\t\t\t" + NHSNo.get() + "\n")
            self.txtPrescription.insert(END,"Extra Information: \t\t\t\t" + FurtherInformation.get() + "\n")

            return
            
            
            
            
            
            



        #.......................................................................................................................#
        

        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,width=1350,padx=20,bd=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.lblTitle=Label(TitleFrame,font=("arial",40,"bold"),text="Pharmacy Management System",padx=2)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,font=("arial",12,"bold"),text="Patient Detail:",relief=RIDGE,padx=20)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,font=("arial",12,"bold"),text="Prescription:",relief=RIDGE,padx=20)
        DataFrameRIGHT.pack(side=RIGHT)

        #..................................................................................................................#

        self.lblTablet=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Tablet:",padx=2,pady=2)
        self.lblTablet.grid(row=0,column=2,sticky=W)

        self.Tablet=ttk.Combobox(DataFrameLEFT,font=("arial",12,"bold"),state="readonly",width=23,textvariable=cmbTablets)
        self.Tablet["value"]=('',"Panadol","Disprin") #............ARRAY
        self.Tablet.current(0)
        self.Tablet.grid(row=0,column=3)

        #..................................................................................................................#

        labels = ["Patient Name:" , "DateOfBirth:" , "NHS No:" , "Patient Address:" , "Patient ID:" , "Lot:" ,
                  "No.of Tablets:" , "Strength:" , "Medication:"] #.............LIST
        counter = 0
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("arial",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=0,sticky=W)

            counter += 1

        entry_box = {"Patient Name:":PatientName , "DateOfBirth:":DateOfBirth , "NHS No:":NHSNo , "Patient Address:":PatientAddress , "Patient ID:":PatientID , "Lot:":Lot
                     , "No.of Tablets:":NoofTablets , "Strength:":Strength , "Medication:":Medication} #.........DICTIONARY

        counter = 0

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("arial",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=1)
            counter += 1

        labels = ["Dose:" , "Issue Date:" , "Exp Date:" , "Side Effects:" , "Ref No:" , "Storage Advice:" , "Using Machine:" , "Further Information:"]#..LIST
        
        counter = 1
        
        for i in range (len(labels)):
            self.cur_label = "label" + str(i)
            self.cur_label=Label(DataFrameLEFT,font=("arial",12,"bold"),text=labels[i],padx=2,pady=2)
            self.cur_label.grid(row=counter,column=2,sticky=W)

            counter += 1

        entry_box = {"Dose:":Dose , "Issue Date:":IssueDate , "Exp Date:":ExpDate , "Side Effects:":SideEffects , "Ref No:":RefNo ,
                     "Storage Advice:":StorageAdvice , "Using Machine:":UsingMachine , "Further Information:":FurtherInformation}#........DICTIONARY

        counter = 1

        for i in entry_box:
            self.cur_entrybox = "entry" + i
            self.cur_entrybox = Entry(DataFrameLEFT,font=("arial",12,"bold"),width=25,textvariable=entry_box[i])
            self.cur_entrybox.grid(row=counter,column=3)
            counter += 1

        #..........................................................................................................................#

        self.txtPrescription=Text(DataFrameRIGHT,font=("arial",12,"bold"),width=43,height=12,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #..........................................................................................................................#

        self.btnPrescription=Button(ButtonFrame,text="Prescription",font=("arial",12,"bold"),width=24,bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)

        self.btnReceipt=Button(ButtonFrame,text="Receipt",font=("arial",12,"bold"),width=24,bd=4,command=iReceipt)
        self.btnReceipt.grid(row=0,column=1)

        self.btnDelete=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),width=24,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)

        self.btnReset=Button(ButtonFrame,text="Reset",font=("arial",12,"bold"),width=24,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),width=24,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=4)

        #...........................................................................................................................#

        self.lblLabel=Label(FrameDetail,font=("arial",10,"bold"),pady=8,text="Name of Tablet \tReference No. \tDoseage \tNo.of Tablets \tLot \tIssue Date \tExp. Date \tStrength\tStorage Adv. \tNHS Number \tPatient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0,column=0)

        self.txtFrameDetail=Text(FrameDetail,font=("arial",12,"bold"),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)





if __name__=="__main__":
    main()
