from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title('Расчёт прибыли по вкладу')
root.geometry('100x240')

lb_summa = Label(text="Вклад")
lb_summa.pack()

ent1 = Entry()
ent1.pack()

lb_procent = Label(text="Процент")
lb_procent.pack()

ent2 = Entry()
ent2.pack()

lb_year = Label(text='На сколько лет?')
lb_year.pack()

ent3 = Entry()
ent3.pack()


def invest():
    summa = ent1.get()
    summa = int(summa)

    procent = ent2.get()
    procent = int(procent)
    procent = procent / 100

    year = ent3.get()
    year = int(year)

    lst = Listbox()
    lst.pack()
    for i in range(year):
        vclad = summa + (summa * procent)
        lst.insert(END, f"{i} год: {vclad}")

btn = Button(text='Рассчитать', command=invest())
btn.pack()

root.mainloop()