import time
import datetime
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Payroll Systems")
root.geometry('1350x650+0+0')

Tops = Frame(root, width= 1350, height=50, bd= 8, relief="raise")
Tops.pack(side = TOP)
f1 = Frame(root, width = 600, height = 600, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 300, height = 700, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width = 600, height = 200, bd=20, relief="raise")
f1a.pack(side=TOP)
f1b = Frame(f1, width = 600, height = 600, bd=20, relief="raise")
f1b.pack(side=TOP)

lblinfo=Label(Tops, font=('times new roman', 60,'bold'), text="   Payment management systems   ", bd=10, foreground="blue")
lblinfo.grid(row=0,column=0)

def iExit():
    qExit = messagebox.askokcancel("Playroll System", "Do you want to exit the systems")
    if qExit > 0:
        root.destroy()
        return
    
def Reset():
    Name.set("")
    Address.set("")
    Employer.set("")
    HoursWorked.set("")
    HourlyRate.set("")
    Tax.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPayable.set("")
    NINumber.set("")
    DateofOrder.set("")
    Weeklywages.set("")
    Enter_Info.set("")
    txtPaySlip.delete("1.0",END)

def Enter_Info():
    txtPaySlip.insert(END, "\t\tPay Slip\n\n")
    txtPaySlip.insert(END, "Name: \t\t" + Name.get()+ "\n\n")
    txtPaySlip.insert(END, "Address: \t\t" + Address.get()+ "\n\n")
    txtPaySlip.insert(END, "Employer: \t\t" + Employer.get()+ "\n\n")
    txtPaySlip.insert(END, "NINumber:  \t\t" + NINumber.get()+ "\n\n")
    txtPaySlip.insert(END, "Hours Worked: \t\t" + HoursWorked.get()+ "\n\n")
    txtPaySlip.insert(END, "Net Payable: \t\t" + NetPayable.get()+ "\n\n")
    txtPaySlip.insert(END, "Wages Per hour: \t\t" + Wageshour.get()+ "\n\n")
    txtPaySlip.insert(END, "Tax Paid: \t\t" + Taxable.get()+ "\n\n")
    txtPaySlip.insert(END, "Payable:  \t\t" + Payable.get()+ "\n\n")
    


def WeeklyWages():
    HoursWorkedPerWeek=float(HoursWorked.get())
    WagesPerHours=float(wageshour.get)

    paydue=WagesPerhours * HoursWorkedPerWeek
    PaymentDue = "£", str('%.2f' %(paydue))
    


#================================================Variables===========================================================

Name=StringVar()
Address=StringVar()
Employer=StringVar()
HoursWorked=StringVar()
HourlyRate=StringVar()
Tax=StringVar()
OverTime=StringVar()
GrossPay=StringVar()
NetPay=StringVar()
NINumber=StringVar()
DateofOrder=StringVar()
Weeklywages=StringVar()
EnterInfo=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
Wageshour=StringVar()


DateofOrder.set(time.strftime("%d/%m/5y"))
#================================================Label Widget===========================================================

lblName=Label(f1a, text="Name", font=('times new roman', 16,'bold'),foreground="Purple", bd=20).grid(row= 0,column=0)
lblEmployer=Label(f1a, text="Employer", font=('times new roman', 16,'bold'),foreground="black", bd=20).grid(row= 0,column=2)
lblAddress=Label(f1a, text="Address", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 1,column=0)
lblNINumber=Label(f1a, text="NI Number", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 1,column=2)
lblHoursWorked=Label(f1a, text="Hours Worked", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 2,column=0)
lblHourlyRate=Label(f1a, text="Hourly Rate", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 2,column=2)
lblTax=Label(f1a, text="Tax", font=('times new roman', 16,'bold'),foreground="Green", bd=20, anchor='w').grid(row= 3,column=0)
lblOvertime=Label(f1a, text="Overtime", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 3,column=2)
lblGrossPay=Label(f1a, text="Gross Pay", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 4,column=0)
lblNetPay=Label(f1a, text="Net Pay", font=('times new roman', 16,'bold'),foreground="Green", bd=20).grid(row= 4,column=2)
#================================================Entry Widget===========================================================
etxtName= Entry(f1a,textvariable=Name, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtName.grid(row=0, column=1)

etxtAddress= Entry(f1a,textvariable=Address, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtAddress.grid(row=0, column=3)


etxtEmployer= Entry(f1a,textvariable=Employer, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtEmployer.grid(row=1, column=1)
etxtHoursWorked= Entry(f1a,textvariable=HoursWorked, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtHoursWorked.grid(row=2, column=1)
etxtHourlyRate= Entry(f1a,textvariable=HourlyRate, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtHourlyRate.grid(row=2, column=3)
etxtTax= Entry(f1a,textvariable=Tax, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtTax.grid(row=3, column=1)
etxtOverTime= Entry(f1a,textvariable=OverTime, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtOverTime.grid(row=3, column=3)
etxtGrossPay= Entry(f1a,textvariable=GrossPay, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtGrossPay.grid(row=4, column=1)
etxtNetPayable= Entry(f1a,textvariable=NetPayable, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtNetPayable.grid(row=4, column=3)
etxtNINumber= Entry(f1a,textvariable=NINumber, font=('times new roman', 16,'bold') ,bd=16, width=22, justify='left')
etxtNINumber.grid(row=1, column=3)

#================================================Text Widget===========================================================

lblPaySlip=Label(f2, font=('times new roman', 21,'bold'), textvariable=DateofOrder,).grid(row = 0,column = 0)
txtPaySlip = Text(f2, height = 22, width = 34, bd=16, font=('times new roman', 12,'bold'))
txtPaySlip.grid(row=1, column=0)

#================================================Buttons===========================================================
btnSalary=Button(f1b, text='Weekly Salary', command=WeeklyWages, padx=16, bd=8, fg="black",
                    font=('arial',16,'bold'), width=14, height=1).grid(row=0,column=0)

btnReset=Button(f1b, text='Reset', command=Reset, padx=16, bd=8, fg="black",
                    font=('arial',16,'bold'), width=14, height=1).grid(row=0,column=1)

btnPaySlip=Button(f1b, text='View Payslip', command=Enter_Info, padx=16, bd=8, fg="black",
                    font=('arial',16,'bold'), width=14, height=1).grid(row=0,column=2)

btnExit=Button(f1b, text='Exit System', padx=16, bd=8, fg="black",
                    font=('arial',16,'bold'), width=14, height=1, command=iExit,).grid(row=0,column=3)  

root.mainloop()

command=WeeklyWages
    
