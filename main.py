import tkinter as tk
from tkinter import ttk

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file= '../icons/icons8-папка.gif')
        button_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog, bg='#d7d8e0',
                                       bd=0, compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'cost', 'total'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('cost', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Основание')
        self.tree.heading('cost', text='Доход/Расход')
        self.tree.heading('total', text='Сумма')
        self.tree.pack()


    def open_dialog(self):
        Child()


class Child (tk.Toplevel):
    def __int__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавить доходы/расходы')
        self.geometry('400x300+400+300')
        self.resizable(False, False)

        label_description = ttk.Label(self, text='Наименование')
        label_description.place(x=50, y=50)
        label_select = ttk.Label(self, text='Статья')
        label_select.place(x=50, y=80)
        label_summa = ttk.Label(self, text='Сумма:')
        label_summa.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='CLOSE', command=self.destroy)
        btn_cancel.place(x=300, y=80)

        btn_new = ttk.Button(self, text='NEW DATA')
        btn_new.place(x=220, y=170)
        btn_new.bind('<Button-1>')

        self.grab_set()
        self.focus_set()






if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('My Home Finans Prog')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.mainloop()