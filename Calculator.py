#simple calculator implemented in python

from tkinter import *
from tkinter import ttk
import tkinter as tk
 
window = Tk()
window.geometry('700x350')
window.resizable(False, False)


window.title('WELCOME TO OUR CALCULATOR!')
window.configure(bg='black')
window.grid_columnconfigure(2, weight=1)
#the file we will save the history in
history_file = open("calc_history.txt", 'a') 
#list to be parsed
mylist = []
#list to store the history of commands 
history=[]
lines="\n\n\n\n\n\n\n\n\n"

#function used to parse the operators
def parseOpp(op):
    mylist.append(op)
    history_file = open("calc_history.txt", "a")
    history_file .write(op)
    history_file.close()
    print(mylist)
    
    history_file = open("calc_history.txt", "r")
    print("Output of Readlines after writing")
    out = history_file.readlines()[-1]
    #out= history_file.read()
    history_file.close()
    r = Label(text=lines+out,fg='black', bg='white',width=36,height=33,font='sans 9 bold').place(x=450, y=0, anchor=CENTER)

#function to execute the commands
def Execute():
    
    result =0 
    while len(mylist) > 1:
        for x in range (0,len(mylist)):
            print(f"start {x}")
            if mylist[x]=="+":
                result =mylist[x-1]+mylist[x+1]
                history.append(str(mylist[x-1])+" + "+str(mylist[x+1]) +" = " + str(result) )
                mylist.pop(x-1)
                mylist.pop(x-1)
                print(f"and index is {x-1}")
                mylist[x-1]=result
                print(len(mylist))
                print(mylist)
                
                history_file = open("calc_history.txt", "a")
                history_file .write(" = " + str(result) +"\n" )
                history_file.close()
                print(mylist)
    
                break
                
            elif mylist[x]=="-":
                result =mylist[x-1]-mylist[x+1]
                history.append(str(mylist[x-1])+" - "+str(mylist[x+1]) +" = " + str(result) )
                mylist.pop(x-1)
                mylist.pop(x-1)
                print(f"and index is {x-1}")
                mylist[x-1]=result
                print(len(mylist))
                print(mylist)
                
                history_file = open("calc_history.txt", "a")
                history_file .write(" = " + str(result)+ "\n"  )
                history_file.close()
                print(mylist)
                
                break
                
            elif mylist[x]=="*":
                result =mylist[x-1]*mylist[x+1]
                history.append(str(mylist[x-1])+" * "+str(mylist[x+1]) +" = " + str(result) )
                mylist.pop(x-1)
                mylist.pop(x-1)
                print(f"and index is {x-1}")
                mylist[x-1]=result
                print(len(mylist))
                print(mylist)
                
                history_file = open("calc_history.txt", "a")
                history_file .write(" = " + str(result) +"\n" )
                history_file.close()
                print(mylist)
                
                break
                
            elif mylist[x]=="/":
                try:
                    result =mylist[x-1]/mylist[x+1]
                    history.append(str(mylist[x-1])+" / "+str(mylist[x+1]) +" = " + str(result) )
                    mylist.pop(x-1)
                    mylist.pop(x-1)
                    print(f"and index is {x-1}")
                    mylist[x-1]=result
                    print(len(mylist))
                    print(mylist)
                    
                    history_file = open("calc_history.txt", "a")
                    history_file .write(" = " + str(result) +"\n" )
                    history_file.close()
                    print(mylist)
                    
                    break

                except ZeroDivisionError:
                    result="can't divide on 0"
                    history_file = open("calc_history.txt", "a")
                    history_file .write("  " + result +"\n" )
                    history_file.close()
                    mylist.clear()
                    history.clear()
                    
                    break
            else :
                continue
    


    print(history)
    r = Label(text=lines+str(result),fg='black', bg='white',width=36,height=33,font='sans 9 bold').place(x=450, y=0, anchor=CENTER)
    mylist.clear()

#function to parse the digits  
def parseInt(i):
    
    if len(mylist) !=0 and type(mylist[len(mylist)-1]) == int:
        if mylist[len(mylist)-1]==0:
            temp= str(i)
            print("temp =",temp)
            mylist[len(mylist)-1]= int(temp)
        else:    
            temp= str(mylist[len(mylist)-1])+ str(i)
            print("temp =",temp)
            mylist[len(mylist)-1]= int(temp)
    else:
        mylist.append(i)
        
    history_file = open("calc_history.txt", "a")
    history_file .write(str(i))
    history_file.close()
    print(mylist)
    
    history_file = open("calc_history.txt", "r")
    print("Output of Readlines after writing")
    out = history_file.readlines()[-1]
    #out= history_file.read()
    history_file.close()
    
    r = Label(text=lines+out, fg='black', bg='white',width=36,height=33,font='sans 9 bold').place(x=450, y=0, anchor=CENTER)




#digits in the calculater 
 
b0= Button(window,text='0', command=lambda: parseInt(0), fg='pink', bg='black',height = 7, 
      width = 31,font='sans 9 bold')

b0.place(x=7, y=200)

b1 = Button(window,text='1', command=lambda: parseInt(1),  fg='pink', bg='black',height = 3, 
          width = 10,  font='sans 9 bold')
b1.grid(row=4,column=0,sticky=W)

b2 = Button(window,text='2', command=lambda: parseInt(2),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold')
b2.grid(row = 4, column =1,sticky=W )

b3 = Button(window,text='3', command=lambda: parseInt(3), fg='pink', bg='black',height = 3, 
          width = 10 ,font='sans 9 bold')
b3.grid( row=4,column=2,sticky=W)

b4 = Button(text='4', command=lambda: parseInt(4), fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=0, row=3,sticky=W)

b5 = Button(text='5', command=lambda: parseInt(5),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=1, row=3,sticky=W)

b6 = Button(text='6', command=lambda: parseInt(6), fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=2, row=3,sticky=W)

b7 = Button(text='7', command=lambda: parseInt(7),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=0, row=2,sticky=W)

b8 = Button(text='8', command=lambda: parseInt(8),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=1, row=2,sticky=W)

b9 = Button(text='9', command=lambda: parseInt(9),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=2, row=2,sticky=W)

#operators in the calculater 
 
add_b = Button(window,text='+', command=lambda: parseOpp("+") , fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=3, row=2,sticky=W)
sub_b = Button(window,text='-', command=lambda: parseOpp("-"),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=3, row=3,sticky=W)
mult_b = Button(window,text='x', command=lambda: parseOpp("*"),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=3, row=4,sticky=W)
devide_b = Button(window,text='÷', command=lambda: parseOpp("/"),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=3, row=5,sticky=W)
equal_b = Button(window,text='=', command=lambda:Execute(),  fg='pink', bg='black',height = 3, 
          width = 10,font='sans 9 bold').grid(column=3, row=6,sticky=W)


r = Label(text=" ", fg='black', bg='white',width=36,height=34,font='sans 9 bold').place(x=450, y=3, anchor=CENTER)

window.mainloop()