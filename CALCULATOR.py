import parser
from tkinter import  *

root=Tk()
root.title("CALCULATOR")
display=Entry(root)
display.grid(row=1,columnspan=6)

i=0
def  click_num(num):
    global i
    display.insert(i, num)
    i+=1

def click_delete():
    display.delete(0,END)

def delete_onebyone():
    variable1=display.get()
    if len(variable1):
        variable2=variable1[ :-1]
        click_delete()
        display.insert(0,variable2)
    else:
        click_delete()
        display.insert(0,"erorr")

def get_operators(oprators):
    global i
    length=len(oprators)
    display.insert(i,oprators)
    i+=length

def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        click_delete()
        display.insert(0, result)
    except Exception:
        click_delete()
        display.insert(0,"erorr")





Button(root,text="1",command=lambda:click_num(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda:click_num(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda:click_num(3)).grid(row=2,column=2)
Button(root,text="4",command=lambda:click_num(4)).grid(row=2,column=3)
Button(root,text="5",command=lambda:click_num(5)).grid(row=3,column=0)
Button(root,text="6",command=lambda:click_num(6)).grid(row=3,column=1)
Button(root,text="7",command=lambda:click_num(7)).grid(row=3,column=2)
Button(root,text="8",command=lambda:click_num(8)).grid(row=3,column=3)
Button(root,text="9",command=lambda:click_num(9)).grid(row=4,column=0)
Button(root,text="0",command=lambda:click_num(0)).grid(row=4,column=1)

Button(root,text="AC",command=lambda:click_delete()).grid(row=4,column=2)
Button(root,text="=",command=lambda:calculate()).grid(row=4,column=3)
Button(root,text="+",command=lambda:get_operators('+')).grid(row=5,column=0)
Button(root,text="-",command=lambda:get_operators('-')).grid(row=5,column=1)
Button(root,text="*",command=lambda:get_operators('*')).grid(row=5,column=2)
Button(root,text="/",command=lambda:get_operators('/')).grid(row=5,column=3)
Button(root,text="%",command=lambda:get_operators('%')).grid(row=6,column=0)
Button(root,text="Del",command=lambda:delete_onebyone()).grid(row=6,column=1)
Button(root,text="pi",command=lambda:get_operators(*3.14)).grid(row=6,column=2)
Button(root,text="(",command=lambda:get_operators('(')).grid(row=6,column=3)
Button(root,text=")",command=lambda:get_operators(')')).grid(row=2,column=4)
Button(root,text="exp",command=lambda:get_operators('**')).grid(row=4,column=4)
Button(root,text="x!",command=lambda:get_operators()).grid(row=5,column=4)
Button(root,text="^2",command=lambda:get_operators('**2')).grid(row=3,column=4)

root.mainloop()