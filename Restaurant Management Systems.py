from tkinter import *
import random
import time
from tkinter import messagebox

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set(operator)

def btnEquals():
    global operator
    solution = str(eval(operator))
    text_Input.set(solution)
    operator = ""

def ref():
    x = random.randint(12908, 50876)
    randomRef = str(x)
    rand.set(randomRef)
    if Fries.get() == "":
        CoF = 0
    else:
        try:
            CoF = float(Fries.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
    if Drinks.get() == "":
        CoD = 0
    else:
        CoD = float(Drinks.get())
    if Filet.get() == "":
        CoFilet = 0
    else:
        try:
            CoFilet = float(Filet.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
    if Burger.get() == "":
        CoBurger = 0
    else:
        try:
            CoBurger = float(Burger.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
    if Chicken_Burger.get() == "":
        CoChicken_Burger = 0
    else:
        try:
            CoChicken_Burger = float(Chicken_Burger.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
    if Cheese_Burger.get() == "":
        CoCheese_Burger = 0
    else:
        try:
            CoCheese_Burger = float(Cheese_Burger.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")


    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet = CoFilet * 2.99
    CostofBurger = CoBurger * 2.87
    CostofChicken_Burger = CoChicken_Burger * 2.89
    CostofCheese_Burger = CoCheese_Burger * 2.69

    CostofMeal = "pln", str('%.2f' % (CostofFries + CostofDrinks
                                    + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger))

    PayTax = 0.2 *(CostofFries + CostofDrinks
                                    + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)

    TotalCost = (CostofFries + CostofDrinks
                                    + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)

    Ser_Charge = ((CostofFries + CostofDrinks
                                    + CostofFilet + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)/99)

    Service = 'pln', str('%.2f' % round(Ser_Charge, 2))

    OverAllCost = "pln", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "pln", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PayTax)
    Sub_Total.set(CostofMeal)
    Total.set(OverAllCost)

def gExit():
    app.destroy()

def reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Filet.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    Sub_Total.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Drinks.set("")
    Cost.set("")
    Service_Charge.set("")
    Tax.set("")
    Sub_Total.set("")
    Total.set("")




app = Tk()
app.title("Restaurant Management Systems")
app.geometry("1600x700")
app.resizable(0, 0)
operator = ""

text_Input = StringVar()

Tops = Frame(app, width = 1600, height = 70, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(app, width = 800, height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(app, width = 300, height = 700, bg="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)

localTime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Restaurant Management Systems", fg='Steel Blue', bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localTime, fg='Steel Blue', bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

#========Calculator

txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd = 30, insertwidth=4,
                   bg='powder blue', justify='right').grid(columnspan=4)

btn7 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg='powder blue', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg='powder blue', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg='powder blue', command=lambda:btnClick(9)).grid(row=1, column=2)
Addition = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg='powder blue', command=lambda:btnClick("+")).grid(row=1, column=3)
btn4 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg='powder blue', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg='powder blue', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg='powder blue', command=lambda:btnClick(6)).grid(row=2, column=2)
Subraction = Button(f2, padx=18, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg='powder blue', command=lambda:btnClick("-")).grid(row=2, column=3)
btn1 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg='powder blue', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg='powder blue', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg='powder blue', command=lambda:btnClick(3)).grid(row=3, column=2)
Multiplication = Button(f2, padx=18, pady=18, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg='powder blue', command=lambda:btnClick("*")).grid(row=3, column=3)
btnClear = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg='powder blue', command=btnClearDisplay).grid(row=4, column=0)
btn0 = Button(f2, padx=18, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg='powder blue', command=lambda:btnClick(0)).grid(row=4, column=1)
btnEquals = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg='powder blue', command=btnEquals).grid(row=4, column=2)
Division = Button(f2, padx=17, pady=17, bd=8, fg="black", font=('arial', 20, 'bold'), text=".", bg='powder blue', command=lambda:btnClick(".")).grid(row=4, column=3)

#=================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Filet = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()
Sub_Total = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Drinks = StringVar()
Cost = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
Sub_Total = StringVar()
Total = StringVar()


lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), text=rand, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), text=Fries, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtFries.grid(row=1, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger Meal", bd=16, anchor='w')
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), text=Burger, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtBurger.grid(row=2, column=1)

lblFilet = Label(f1, font=('arial', 16, 'bold'), text="Filet Meal", bd=16, anchor='w')
lblFilet.grid(row=3, column=0)
txtFilet = Entry(f1, font=('arial', 16, 'bold'), text=Filet, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtFilet.grid(row=3, column=1)

lblChicken = Label(f1, font=('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChicken.grid(row=4, column=0)
txtChicken = Entry(f1, font=('arial', 16, 'bold'), text=Chicken_Burger, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtChicken.grid(row=4, column=1)

lblCheese = Label(f1, font=('arial', 16, 'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5, column=0)
txtCheese = Entry(f1, font=('arial', 16, 'bold'), text=Cheese_Burger, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtCheese.grid(row=5, column=1)

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), text=Drinks, bd=16, insertwidth=4,
                     bg="powder blue", justify='right')
txtDrinks.grid(row=0, column=3)

#================

lblMeal = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblMeal.grid(row=1, column=2)
txtMeal = Entry(f1, font=('arial', 16, 'bold'), text=Cost, bd=16, insertwidth=4,
                     bg="sky blue", justify='right')
txtMeal.grid(row=1, column=3)

lblCharge = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor='w')
lblCharge.grid(row=2, column=2)
txtCharge = Entry(f1, font=('arial', 16, 'bold'), text=Service_Charge, bd=16, insertwidth=4,
                     bg="sky blue", justify='right')
txtCharge.grid(row=2, column=3)

lblTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w')
lblTax.grid(row=3, column=2)
txtTax = Entry(f1, font=('arial', 16, 'bold'), text=Tax, bd=16, insertwidth=4,
                     bg="sky blue", justify='right')
txtTax.grid(row=3, column=3)

lblTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblTotal.grid(row=4, column=2)
txtTotal = Entry(f1, font=('arial', 16, 'bold'), text=Sub_Total, bd=16, insertwidth=4,
                     bg="sky blue", justify='right')
txtTotal.grid(row=4, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor='w')
lblCost.grid(row=5, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), text=Total, bd=16, insertwidth=4,
                     bg="sky blue", justify='right')
txtCost.grid(row=5, column=3)

#=============

btnTotal = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Total", bg="powder blue", command=ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Reset", bg="powder blue", command=reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=12, fg="black", font=('arial', 16, 'bold'), width=10,
                  text="Exit", bg="powder blue", command=gExit).grid(row=7, column=3)

app.mainloop()