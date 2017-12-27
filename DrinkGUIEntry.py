'''Created on Dec 24, 2017, @author: daneaadland'''


from tkinter import *

root = Tk()

def calc_amt():
    Label(root, text=calc_oz_of_alc(e1AmtVar, e1AbvVar)).grid(row=1, column=4)
    Label(root, text=calc_oz_of_alc(e2AmtVar, e2AbvVar)).grid(row=2, column=4)
    Label(root, text=calc_oz_of_alc(e3AmtVar, e3AbvVar)).grid(row=3, column=4)
    Label(root, text=calc_sum_amt()).grid(row=4, column=2)
    Label(root, text=calc_sum_total_oz_of_alc()).grid(row=4, column=4)
    Label(root, text=calc_total_abv()).grid(row=5, column=4)
    
def calc_oz_of_alc(amt, abv):
    alc_in_oz = round(amt.get()*abv.get(), 2)
    return alc_in_oz

def calc_sum_amt():
    amt_sum = e1AmtVar.get() + e2AmtVar.get() + e3AmtVar.get()
    return amt_sum

def calc_sum_total_oz_of_alc():
    e1 = calc_oz_of_alc(e1AmtVar, e1AbvVar)
    e2 = calc_oz_of_alc(e2AmtVar, e2AbvVar)
    e3 = calc_oz_of_alc(e3AmtVar, e3AbvVar)
    alc_oz_sum = round(e1+e2+e3,2)
    return alc_oz_sum

def calc_total_abv():
    total_abv = round(calc_sum_total_oz_of_alc() / calc_sum_amt(), 2)
    return total_abv

#Row Labels at row 0
Label(root, text="Name").grid(row=0, column=1)
Label(root, text="Amt (in oz)").grid(row=0, column=2)
Label(root, text="ABV").grid(row=0, column=3)
Label(root, text="Total oz of Alcohol").grid(row=0, column=4)

#Column Labels at column 0
Label(root, text="Drink #1").grid(row=1)
Label(root, text="Drink #2").grid(row=2)
Label(root, text="Drink #3").grid(row=3)
Label(root, text='Total ABV of Drink').grid(row=5, column=3)
Label(root, text="0.0").grid(row=4, column=2)
Label(root, text="0.0").grid(row=1, column=4)
Label(root, text="0.0").grid(row=2, column=4)
Label(root, text="0.0").grid(row=3, column=4)
Label(root, text="0.0").grid(row=4, column=4)
Label(root, text="0.0").grid(row=5, column=4)



#Name entries
e1NameVar = StringVar()
e2NameVar = StringVar()
e3NameVar = StringVar()
e1NameVar.set('Enter a Name')
e2NameVar.set('Enter a Name')
e3NameVar.set('Enter a Name')
e1Name = Entry(root, textvariable=e1NameVar).grid(row=1, column=1)
e2Name = Entry(root, textvariable=e2NameVar).grid(row=2, column=1)
e3Name = Entry(root, textvariable=e3NameVar).grid(row=3, column=1)

#Amt entries
e1AmtVar = DoubleVar()
e2AmtVar = DoubleVar()
e3AmtVar = DoubleVar()
e1Amt = Entry(root, textvariable=e1AmtVar).grid(row=1, column=2)
e2Amt = Entry(root, textvariable=e2AmtVar).grid(row=2, column=2)
e3Amt = Entry(root, textvariable=e3AmtVar).grid(row=3, column=2)

#ABV entries
e1AbvVar = DoubleVar()
e2AbvVar = DoubleVar()
e3AbvVar = DoubleVar()
e1Abv = Entry(root, textvariable=e1AbvVar).grid(row=1, column=3)
e2Abv = Entry(root, textvariable=e2AbvVar).grid(row=2, column=3)
e3Abv = Entry(root, textvariable=e3AbvVar).grid(row=3, column=3)


#Buttons
b1 = Button(root, text='Calculate', command=calc_amt).grid(row=6, column=1)
b2 = Button(root, text='Quit', command=root.quit).grid(row=6, column=2)

mainloop( )