from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext

import cx_Oracle

root=Tk()
root.title("Student Management System")
root.geometry("300x300+400+200")

vist=Toplevel(root)
vist.title("View Student")
vist.geometry("300x300+400+200")
vist.withdraw()

stData=scrolledtext.ScrolledText(vist,width=30,height=15)

def  f4():
	root.deiconify()
	vist.withdraw()
	stData.config(state=NORMAL)
	stData.delete("1.0",END)
	stData.config(state=DISABLED)
	
btnBackView=Button(vist,text="Back",command=f4)
stData.pack()
btnBackView.pack()

adst=Toplevel(root)
adst.title("Add Student")
adst.geometry("300x300+400+200")
adst.withdraw()

lblRnoAdd=Label(adst,text="Roll No.")
entRnoAdd=Entry(adst,bd=5)
lblNameAdd=Label(adst,text="Name")
entNameAdd=Entry(adst,bd=5)

def f5():
	con=None
	try:
		con=cx_Oracle.connect("system/abc123")
		cursor=con.cursor()
		s1=entRnoAdd.get()
		if(s1 ==""):
			messagebox.showerror("Incomplete",'Roll no is empty')
			entRnoAdd.focus()
			return
		s2=entNameAdd.get()
		if(s2==""):
			messagebox.showerror("Incomplete",'Name is empty')
			entNameAdd.focus()
			return
		name=entNameAdd.get()
		#rno1=int(entRnoAdd.get())
		try:
			rno=int(entRnoAdd.get())
		except:
			if s1.isalpha():
				messagebox.showerror("Invalid ","Roll no. should be integer")
				entRnoAdd.delete(0,END)
				entRnoAdd.focus()
				return
				
				
		if not name.isalpha():
			messagebox.showerror("Invalid ","Name should be a string")
			entNameAdd.delete(0,END)
			entNameAdd.focus()
			return
		sql="insert into student values('%d','%s')"
		args=(rno,name)
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+" row inserted"
		messagebox.showinfo("Success",msg)
	
	except cx_Oracle.DatabaseError as e:
		msg="Issue" + str(e)
		messagebox.showerror("Error",msg)
		con.rollback()
			
	finally:
		cursor.close()
		if con is not None:
			con.close()
	entRnoAdd.delete(0,END)
	entNameAdd.delete(0,END)
	entRnoAdd.focus()
		
			
btnSaveAdd=Button(adst,text="Save",command=f5)

def f2():
	root.deiconify()
	adst.withdraw()
	
btnBackAdd=Button(adst,text="Back",command=f2)

lblRnoAdd.pack(pady=5)
entRnoAdd.pack(pady=5)
lblNameAdd.pack(pady=5)
entNameAdd.pack(pady=5)
btnSaveAdd.pack(pady=5)
btnBackAdd.pack(pady=5)


def f1():
	adst.deiconify()
	entRnoAdd.focus()
	root.withdraw()


btnAddRoot=Button(root,text="Add",width=10,command=f1)

def f3():
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor =con.cursor()
		stData.config(state=NORMAL)
		sql="select * from student"
		cursor.execute(sql)
		rows =cursor.fetchall()
		data=""
		for r in rows:
			rno=r[0]
			name=r[1]
			data=data + "Roll no.: " + str(rno) + " Name: " +str(name) + "\n"
			stData.insert(INSERT,data)
		stData.config(state=DISABLED)	
	except cx_Oracle.DatabaseError as e:
		msg="Issue" + str(e)
		messagebox.showerror("Error",msg)
		
	finally:
		cursor.close()
		if con is not None:
			con.close()
	

btnViewRoot=Button(root,text="View",width=10,command=f3)


upst=Toplevel(root)
upst.title("Update Student")
upst.geometry("300x300+400+200")
upst.withdraw()


lblRnoUp=Label(upst,text="Roll no.")
entRnoUp=Entry(upst,bd=5)
lblNameUp=Label(upst,text="Update Name")
entNameUp=Entry(upst,bd=5)

def f8():
	con=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor =con.cursor()
		s=entRnoUp.get()

		if(s==""):
			messagebox.showerror("incomplete",'Empty!!')
			entNameDlst.focus()
			return
		
		rno=int(entRnoUp.get())
		name=entNameUp.get()
		if name=="":
			messagebox.showerror("Invalid","Name cannot be empty")
			entNameUp.focus()
			return
		sql="update student set name='%s' where rno='%d'"
		args=(name,rno)
		cursor.execute(sql % args)
		con.commit()
		msg="rows updated"
		messagebox.showinfo("Success",msg)
		entRnoUp.delete(0,END)
		entNameUp.delete(0,END)
		entRnoUp.focus()
	
		
				
	except cx_Oracle.DatabaseError as e:
		msg="Issue" + str(e)
		messagebox.showerror("Error",msg)
		
	finally:
		cursor.close()
		if con is not None:
			con.close()
	

btnSaveUp=Button(upst,text="Save",command=f8)


def f9():
	root.deiconify()
	upst.withdraw()


btnBackUp=Button(upst,text="Back",command=f9)

lblRnoUp.pack(pady=5)
entRnoUp.pack(pady=5)
lblNameUp.pack(pady=5)
entNameUp.pack(pady=5)
btnSaveUp.pack(pady=5)
btnBackUp.pack(pady=5)

def f7():
	upst.deiconify()
	root.withdraw()
	entRnoUp.focus()
	

btnUpdateRoot=Button(root,text="Update",width=10,command=f7)

	
dlst=Toplevel(root)
dlst.title("Delete Student")
dlst.geometry("300x300+400+200")
dlst.withdraw()

lblNameDlst=Label(dlst,text="Name")
entNameDlst=Entry(dlst,bd=5)
lblRnoDlst=Label(dlst,text="Roll no.")
entRnoDlst=Entry(dlst,bd=5)


def f10():
	con=None
	try:
		con = cx_Oracle.connect("system/abc123")
		cursor =con.cursor()
		s=entRnoDlst.get()
		
		if(s==""):
			messagebox.showerror("incomplete",'Empty!!')
			entNameDlst.focus()
			return
		if not entRnoDlst.get().isdigit():
			messagebox.showerror("Invalid","Roll No. should be Integer")
			entRnoDlst.delete(0,END)
			entRnoDlst.focus()
			return
			
		rno=int(entRnoDlst.get())	
		sql="DELETE FROM student WHERE rno='%d'"
		args=rno
		cursor.execute(sql%args)
		con.commit()
		msg=str(cursor.rowcount)+"row deleted"
		messagebox.showinfo("Success",msg)
		entRnoDlst.delete(0,END)
		entRnoDlst.focus()
	
				
	except cx_Oracle.DatabaseError as e:
		msg="Issue" + str(e)
		messagebox.showerror("Error",msg)
		
	finally:
		cursor.close()
		if con is not None:
			con.close()
	
	



btnDeleteDlst=Button(dlst,text="Delete",command=f10)

def f12():
	root.deiconify()
	dlst.withdraw()
	
btnBackDlst=Button(dlst,text="Back",command=f12)
#lblNameDlst.pack(pady=5)
#entNameDlst.pack(pady=5)
lblRnoDlst.pack(pady=5)
entRnoDlst.pack(pady=5)
btnDeleteDlst.pack(pady=5)
btnBackDlst.pack(pady=5)

def f11():
	dlst.deiconify()
	root.withdraw()
	entRnoDlst.focus()
	

btnDeleteRoot=Button(root,text="Delete",width=10,command=f11)
btnAddRoot.pack(pady=10)
btnViewRoot.pack(pady=10)
btnDeleteRoot.pack(pady=10)
btnUpdateRoot.pack(pady=10)

def f6():
	ans=messagebox.askyesno("Exit",'You really want to exit')
	if ans:
		import sys
		sys.exit()
		
root.protocol("WM_DELETE_WINDOW",f6)
root.mainloop()
