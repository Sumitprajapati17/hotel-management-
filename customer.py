from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk 


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        # ===================title=========
        lbl_title=Label(self.root,text="ADD Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=60)


        #=====================logo=============
        img2=Image.open(r"C:\SumitPrajapati\hotel management\image\logo.png")
        img2=img2.resize((100,57),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=1,width=100,height=57)

        # =====================labelFrame====================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=60,width=425,height=490)


        #===================== labels and entrys==========
        #custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        enty_ref=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        enty_ref.grid(row=0,column=1)

        #cust name 
        cname=Label(labelframeleft,font=("times new roman",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtcname.grid(row=1,column=1)

        #mother name 
        lblmname=Label(labelframeleft,font=("times new roman",12,"bold"),text="Mother Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtmname.grid(row=2,column=1)

        #father name 
        #lblFatherName=Label(labelframeleft,font=("times new roman",12,"bold"),text="Father Name:",padx=2,pady=6)
        #lblFatherName.grid(row=3,column=0,sticky=W)
        #txtFatherName=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        #txtFatherName.grid(row=3,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("times new roman",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=4,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1)

        # postcode
        lblPostCode=Label(labelframeleft,font=("times new roman",12,"bold"),text="Post Code:",padx=2,pady=6)
        lblPostCode.grid(row=5,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtPostCode.grid(row=5,column=1)

        #mobilenumber
        lblMobile=Label(labelframeleft,font=("times new roman",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtMobile.grid(row=6,column=1)

        # email
        lblEmail=Label(labelframeleft,font=("times new roman",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=7,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtEmail.grid(row=7,column=1)

        #nationality
        lblNationality=Label(labelframeleft,font=("times new roman",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=8,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=8,column=1)


        #idproof type combobox
        lblIdProof=Label(labelframeleft,font=("times new roman",12,"bold"),text="Id Proof Type",padx=2,pady=6)
        lblIdProof.grid(row=9,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_id["value"]=("AdharCard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=9,column=1)

        # ID number
        lblIdNumber=Label(labelframeleft,font=("times new roman",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=10,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtIdNumber.grid(row=10,column=1)

        # Address
        lblAddress=Label(labelframeleft,font=("times new roman",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=11,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,width=29,font=("times new roman",13,"bold"))
        txtAddress.grid(row=11,column=1)

        #=========================btns================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("times of roman",12,"bold"),bg="grey",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",font=("times of roman",12,"bold"),bg="grey",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",font=("times of roman",12,"bold"),bg="grey",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",font=("times of roman",12,"bold"),bg="grey",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #==========================table frame===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=60,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("times new roman",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search=ttk.Combobox(Table_Frame,font=("times new roman",12,"bold"),width=27,state="readonly")
        combo_Search["value"]=("Mobile","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_Frame,width=27,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("times of roman",12,"bold"),bg="grey",fg="white",width=8)
        btnSearch.grid(row=0,column=3,padx=1)

        btnUpdate=Button(Table_Frame,text="Show All",font=("times of roman",12,"bold"),bg="grey",fg="white",width=8)
        btnUpdate.grid(row=0,column=4,padx=1)

        #======================Show data Table=============

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
    
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)

#   def add_data(self):


#if __name__ == "__main__":
#    root=Tk()
#   obj=Cust_Win(root)
#   root.mainloop()