from tkinter import *
def delete():
    f=open("aditi.txt","r")
    data=f.read()
    f.close()
    f=open("aditi.txt","w")
    m=data[0:len(data)-1]
    f.write(m)
    f.close()
    makelabel()

def clear():
    f=open("aditi.txt","w")
    f.close()
    makelabel()

def fun(c):
    f=open("aditi.txt", "a")
    f.write(c)
    f.close()
    makelabel()

def makelabel():
    f=open("aditi.txt","r")
    m=f.read()
    L=Label(text=m,height=3,width=8)
    L.grid(row=0,column=1)
    f.close()

def sum():
    f=open("aditi.txt","r")
    data=f.read()
    if "+" in data:
        t=data.split("+",1)
        m=str(int(t[0])+int(t[1]))
    if "-" in data:
        t=data.split("-",1)
        m=str(int(t[0])-int(t[1]))
    if "*" in data:
        t=data.split("*",1)
        m=str(int(t[0])*int(t[1]))
    if "/" in data:
        t=data.split("/",1)
        m=str(int(t[0])/int(t[1]))
    f.close()
    f=open("aditi.txt","w")
    f.write(m)
    f.close()
    makelabel()
    #f=open("aditi.txt","w")
    #f.close()

root=Tk()
f=open("aditi.txt","w")
f.close()
B1=Button(text="1",height=3, width=8,command=lambda:fun("1"))
B1.grid(row=1,column=1)
B2=Button(text="2",height=3, width=8,command=lambda:fun("2"))
B2.grid(row=1,column=2)
B3=Button(text="3",height=3, width=8,command=lambda:fun("3"))
B3.grid(row=1,column=3)
B4=Button(text="4",height=3, width=8,command=lambda:fun("4"))
B4.grid(row=2,column=1)
B5=Button(text="5",height=3, width=8,command=lambda:fun("5"))
B5.grid(row=2,column=2)
B6=Button(text="6",height=3, width=8,command=lambda:fun("6"))
B6.grid(row=2,column=3)
B7=Button(text="7",height=3, width=8,command=lambda:fun("7"))
B7.grid(row=3,column=1)
B8=Button(text="8",height=3, width=8,command=lambda:fun("8"))
B8.grid(row=3,column=2)
B9=Button(text="9",height=3, width=8,command=lambda:fun("9"))
B9.grid(row=3,column=3)
B10=Button(text="+",height=3, width=8,command=lambda:fun("+"))
B10.grid(row=1,column=4)
B11=Button(text="-",height=3, width=8,command=lambda:fun("-"))
B11.grid(row=2,column=4)
B12=Button(text="=",height=3, width=8,command=lambda:sum())
B12.grid(row=0,column=4)
B13=Button(text="0",height=3, width=8,command=lambda:fun("0"))
B13.grid(row=4,column=2)
B16=Button(text="*",height=3, width=8,command=lambda:fun("*"))
B16.grid(row=3,column=4)
B14=Button(text="/",height=3, width=8,command=lambda:fun("/"))
B14.grid(row=4,column=4)
B15=Button(text="clear",height=3, width=8,command=lambda:clear())
B15.grid(row=4,column=3)
#L=Label(height=3,width=8)
#L.grid(row=0,column=1)
B17=Button(text="delete",height=3, width=8,command=lambda:delete())
B17.grid(row=4,column=1)



root.mainloop()