
from tkinter import *

"""
Определение функций - слотов(command=AddContact)
"""
def Selected():
    """
    функция для возврата выбранного значения
    """
    return int(select.curselection()[0])

def AddContact():
    """
    функция для добавления нового контакта
    """
    if Number.get().isdigit() and Number != "":
        contactlist.append([Name.get(), Number.get()])
    else:
        lbl = Label(window, text='вводите цифры! ', font='arial 8', fg='red')
        lbl.place(x=150, y=50)
        window.after(2000, lbl.destroy)
    Select_set()

def EDIT():
    """
    функция редактирует существующий контакт
    """
    contactlist[Selected()] = [Name.get(), Number.get()]
    Select_set()


def DELETE():
    """
    функция удалит выбранный контакт
    """
    del contactlist[Selected()]
    Select_set()

def VIEW():
    """
    функция будет просматривать выбранный контакт
    """
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    """
    используется для выхода из основного цикла(mainloop)
    """
    window.destroy()

def RESET():
    """
     поля имени и номера сбросит в пустые строки
    """
    Name.set('')
    Number.set('')

def Select_set() :
    """
    сортирует список контактов, а также используется в других функциях
    """
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

if __name__=='__main__':
    """
    Инициализация главного окна 
    """
    window = Tk()
    window.geometry('800x700')
    window.config(bg='SlateGray3')
    window.resizable(0, 0)
    window.title('Телефонный справочник')

    # Предопределенный список телефонной книги
    contactlist = [
        ['Иван Петров', '0176738493'],
        ['Петров Иван', '2684430000'],
        ['Коренев Владимир', '4338354432'],
        ['Карл Маркс', '6834552341'],
        ['Павел Корчагин', '1234852689'],
        ['Семён Дежнёв', '2119876543'],
        ]

    Name = StringVar()  # поле Фамилия
    Number = StringVar()  # поле Номер телефона

    # фрейм просмотра списка абонентов телефонной книги
    frame = Frame(window)
    frame.pack(side=RIGHT)

    scroll = Scrollbar(frame, orient=VERTICAL)
    select = Listbox(frame, yscrollcommand=scroll.set, height=35, width=32)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)

    """
    Определение кнопок и меток 
    """
    # Фамилия
    Label(window, text='Имя: ', font='arial 12 bold', bg='SlateGray3').place(x=50, y=20)
    Entry(window, textvariable=Name).place(x=120, y=20)
    # Номер Телефона
    Label(window, text='Телефон: ', font='arial 12 bold', bg='SlateGray3').place(x=50, y=70)
    Entry(window, textvariable=Number).place(x=160, y=70)

    Button(window, text=" Добавить", font='arial 12 bold', bg='SlateGray4', command=AddContact).place(x=50, y=110)
    Button(window, text="Редактировать", font='arial 12 bold', bg='SlateGray4', command=EDIT).place(x=50, y=260)
    Button(window, text="Удалить", font='arial 12 bold', bg='SlateGray4', command=DELETE).place(x=50, y=210)
    Button(window, text="Просмотреть", font='arial 12 bold', bg='SlateGray4', command=VIEW).place(x=50, y=160)

    Button(window, text="Выход", font='arial 12 bold',bg='tomato', command=EXIT).place(x=50, y=620)
    Button(window, text="Сброс", font='arial 12 bold',bg='SlateGray4', command=RESET).place(x=50, y=310)

    Select_set()
    window.mainloop()

