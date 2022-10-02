from tkinter import *
from tkinter import ttk
import regex as re
import sympy


class Scene1:
    # Caracteristicas gerais
    btn_width = 4
    def __init__(self, master):
        """Inicializa a cena."""
        self.frame = ttk.Frame(master)
        self.frame.grid(column=0, row=0, pady=25, padx=25)

        self.frame1 = ttk.Frame(master)
        self.frame1.grid(column=0, row=1, pady=5)

        self.valores = StringVar()
        self.valores.trace('w', self.event_on_write)

        self.textbox = ttk.Entry(self.frame)
        self.textbox['textvariable'] = self.valores
        self.textbox['width'] = 26
        self.textbox['font'] = ('Calibri', '14')
        self.textbox['justify'] = RIGHT
        self.textbox.bind('<Return>', lambda e: self.calcula())
        self.textbox.bind('<Down>', lambda e: self.btn_c.focus_force())
        self.textbox.bind('<BackSpace>', lambda e: self.key_backspace())
        self.textbox.focus_force()

        self.btn_shift = ttk.Button(self.frame1)
        self.btn_shift['text'] = 'Shift'
        self.btn_shift['width'] = self.btn_width
        self.btn_shift.bind('<Right>', lambda e: self.btn_ce.focus_force())
        self.btn_shift.bind('<Down>', lambda e: self.btn_7.focus_force())
        self.btn_shift.bind('<Up>', lambda e: self.textbox.focus_force())


        self.btn_0 = ttk.Button(self.frame1)
        self.btn_0['text'] = '0'
        self.btn_0['width'] = self.btn_width
        self.btn_0['command'] = self.insert_0
        self.btn_0.bind('<Right>', lambda e: self.btn_p.focus_force())
        self.btn_0.bind('<Left>', lambda e: self.btn_sub.focus_force())
        self.btn_0.bind('<Down>', lambda e: self.textbox.focus_force())
        self.btn_0.bind('<Up>', lambda e: self.btn_1.focus_force())

        self.btn_1 = ttk.Button(self.frame1)
        self.btn_1['text'] = '1'
        self.btn_1['width'] = self.btn_width
        self.btn_1['command'] = self.insert_1
        self.btn_1.bind('<Right>', lambda e: self.btn_2.focus_force())
        self.btn_1.bind('<Left>', lambda e: self.btn_x.focus_force())
        self.btn_1.bind('<Down>', lambda e: self.btn_0.focus_force())
        self.btn_1.bind('<Up>', lambda e: self.btn_4.focus_force())

        self.btn_2 = ttk.Button(self.frame1)
        self.btn_2['text'] = '2'
        self.btn_2['width'] = self.btn_width
        self.btn_2['command'] = self.insert_2
        self.btn_2.bind('<Right>', lambda e: self.btn_3.focus_force())
        self.btn_2.bind('<Left>', lambda e: self.btn_1.focus_force())
        self.btn_2.bind('<Down>', lambda e: self.btn_p.focus_force())
        self.btn_2.bind('<Up>', lambda e: self.btn_5.focus_force())

        self.btn_3 = ttk.Button(self.frame1)
        self.btn_3['text'] = '3'
        self.btn_3['width'] = self.btn_width
        self.btn_3['command'] = self.insert_3
        self.btn_3.bind('<Right>', lambda e: self.btn_sub.focus_force())
        self.btn_3.bind('<Left>', lambda e: self.btn_2.focus_force())
        self.btn_3.bind('<Down>', lambda e: self.btn_eq.focus_force())
        self.btn_3.bind('<Up>', lambda e: self.btn_6.focus_force())

        self.btn_4 = ttk.Button(self.frame1)
        self.btn_4['text'] = '4'
        self.btn_4['width'] = self.btn_width
        self.btn_4['command'] = self.insert_4
        self.btn_4.bind('<Right>', lambda e: self.btn_5.focus_force())
        self.btn_4.bind('<Left>', lambda e: self.btn_div.focus_force())
        self.btn_4.bind('<Down>', lambda e: self.btn_1.focus_force())
        self.btn_4.bind('<Up>', lambda e: self.btn_7.focus_force())

        self.btn_5 = ttk.Button(self.frame1)
        self.btn_5['text'] = '5'
        self.btn_5['width'] = self.btn_width
        self.btn_5['command'] = self.insert_5
        self.btn_5.bind('<Right>', lambda e: self.btn_6.focus_force())
        self.btn_5.bind('<Left>', lambda e: self.btn_4.focus_force())
        self.btn_5.bind('<Down>', lambda e: self.btn_2.focus_force())
        self.btn_5.bind('<Up>', lambda e: self.btn_8.focus_force())

        self.btn_6 = ttk.Button(self.frame1)
        self.btn_6['text'] = '6'
        self.btn_6['width'] = self.btn_width
        self.btn_6['command'] = self.insert_6
        self.btn_6.bind('<Right>', lambda e: self.btn_x.focus_force())
        self.btn_6.bind('<Left>', lambda e: self.btn_5.focus_force())
        self.btn_6.bind('<Down>', lambda e: self.btn_3.focus_force())
        self.btn_6.bind('<Up>', lambda e: self.btn_9.focus_force())

        self.btn_7 = ttk.Button(self.frame1)
        self.btn_7['text'] = '7'
        self.btn_7['width'] = self.btn_width
        self.btn_7['command'] = self.insert_7
        self.btn_7.bind('<Right>', lambda e: self.btn_8.focus_force())
        self.btn_7.bind('<Left>', lambda e: self.btn_sum.focus_force())
        self.btn_7.bind('<Down>', lambda e: self.btn_4.focus_force())
        self.btn_7.bind('<Up>', lambda e: self.btn_shift.focus_force())

        self.btn_8 = ttk.Button(self.frame1)
        self.btn_8['text'] = '8'
        self.btn_8['width'] = self.btn_width
        self.btn_8['command'] = self.insert_8
        self.btn_8.bind('<Right>', lambda e: self.btn_9.focus_force())
        self.btn_8.bind('<Left>', lambda e: self.btn_7.focus_force())
        self.btn_8.bind('<Down>', lambda e: self.btn_5.focus_force())
        self.btn_8.bind('<Up>', lambda e: self.btn_ce.focus_force())

        self.btn_9 = ttk.Button(self.frame1)
        self.btn_9['text'] = '9'
        self.btn_9['width'] = self.btn_width
        self.btn_9['command'] = self.insert_9
        self.btn_9.bind('<Right>', lambda e: self.btn_div.focus_force())
        self.btn_9.bind('<Left>', lambda e: self.btn_8.focus_force())
        self.btn_9.bind('<Down>', lambda e: self.btn_6.focus_force())
        self.btn_9.bind('<Up>', lambda e: self.btn_ce.focus_force())

        self.btn_p = ttk.Button(self.frame1)
        self.btn_p['text'] = '.'
        self.btn_p['width'] = self.btn_width
        self.btn_p['command'] = self.insert_p
        self.btn_p.bind('<Right>', lambda e: self.btn_eq.focus_force())
        self.btn_p.bind('<Left>', lambda e: self.btn_0.focus_force())
        self.btn_p.bind('<Down>', lambda e: self.textbox.focus_force())
        self.btn_p.bind('<Up>', lambda e: self.btn_2.focus_force())

        self.btn_eq = ttk.Button(self.frame1)
        self.btn_eq['text'] = '='
        self.btn_eq['width'] = self.btn_width
        self.btn_eq['command'] = self.calcula
        self.btn_eq.bind('<Right>', lambda e: self.btn_sum.focus_force())
        self.btn_eq.bind('<Left>', lambda e: self.btn_p.focus_force())
        self.btn_eq.bind('<Down>', lambda e: self.textbox.focus_force())
        self.btn_eq.bind('<Up>', lambda e: self.btn_3.focus_force())

        self.btn_div = ttk.Button(self.frame1)
        self.btn_div['text'] = '/'
        self.btn_div['width'] = self.btn_width
        self.btn_div['command'] = self.insert_div
        self.btn_div.bind('<Right>', lambda e: self.btn_4.focus_force())
        self.btn_div.bind('<Left>', lambda e: self.btn_9.focus_force())
        self.btn_div.bind('<Down>', lambda e: self.btn_x.focus_force())
        self.btn_div.bind('<Up>', lambda e: self.btn_c.focus_force())

        self.btn_x = ttk.Button(self.frame1)
        self.btn_x['text'] = 'x'
        self.btn_x['width'] = self.btn_width
        self.btn_x['command'] = self.insert_x
        self.btn_x.bind('<Right>', lambda e: self.btn_1.focus_force())
        self.btn_x.bind('<Left>', lambda e: self.btn_6.focus_force())
        self.btn_x.bind('<Down>', lambda e: self.btn_sub.focus_force())
        self.btn_x.bind('<Up>', lambda e: self.btn_div.focus_force())

        self.btn_sub = ttk.Button(self.frame1)
        self.btn_sub['text'] = '-'
        self.btn_sub['width'] = self.btn_width
        self.btn_sub['command'] = self.insert_sub
        self.btn_sub.bind('<Right>', lambda e: self.btn_0.focus_force())
        self.btn_sub.bind('<Left>', lambda e: self.btn_3.focus_force())
        self.btn_sub.bind('<Down>', lambda e: self.btn_sum.focus_force())
        self.btn_sub.bind('<Up>', lambda e: self.btn_x.focus_force())

        self.btn_sum = ttk.Button(self.frame1)
        self.btn_sum['text'] = '+'
        self.btn_sum['width'] = self.btn_width
        self.btn_sum['command'] = self.insert_sum
        self.btn_sum.bind('<Right>', lambda e: self.btn_7.focus_force())
        self.btn_sum.bind('<Left>', lambda e: self.btn_eq.focus_force())
        self.btn_sum.bind('<Down>', lambda e: self.textbox.focus_force())
        self.btn_sum.bind('<Up>', lambda e: self.btn_sub.focus_force())

        self.btn_ce = ttk.Button(self.frame1)
        self.btn_ce['text'] = 'CE'
        self.btn_ce['width'] = self.btn_width
        self.btn_ce['command'] = self.insert_ce
        self.btn_ce.bind('<Right>', lambda e: self.btn_c.focus_force())
        self.btn_ce.bind('<Left>', lambda e: self.btn_shift.focus_force())
        self.btn_ce.bind('<Down>', lambda e: self.btn_9.focus_force())
        self.btn_ce.bind('<Up>', lambda e: self.textbox.focus_force())

        self.btn_c = ttk.Button(self.frame1)
        self.btn_c['text'] = 'C'
        self.btn_c['width'] = self.btn_width
        self.btn_c['command'] = self.insert_c
        self.btn_c.bind('<Right>', lambda e: self.btn_7.focus_force())
        self.btn_c.bind('<Left>', lambda e: self.btn_ce.focus_force())
        self.btn_c.bind('<Down>', lambda e: self.btn_div.focus_force())
        self.btn_c.bind('<Up>', lambda e: self.textbox.focus_force())

        self.draw_widgets()

    def draw_widgets(self):
        self.textbox.grid()

        self.btn_shift.grid(row=0, column=0, pady=10)
        self.btn_ce.grid(row=0, column=2)
        self.btn_c.grid(row=0, column=3)

        self.btn_7.grid(row=1, column=0, padx=5, pady=5)
        self.btn_4.grid(row=2, column=0)
        self.btn_1.grid(row=3, column=0)
        self.btn_0.grid(row=4, column=0)

        self.btn_8.grid(row=1, column=1, padx=5)
        self.btn_5.grid(row=2, column=1, pady=5)
        self.btn_2.grid(row=3, column=1)
        self.btn_p.grid(row=4, column=1)

        self.btn_9.grid(row=1, column=2, padx=5)
        self.btn_6.grid(row=2, column=2)
        self.btn_3.grid(row=3, column=2, pady=5)
        self.btn_eq.grid(row=4, column=2)

        self.btn_div.grid(row=1, column=3, padx=5)
        self.btn_x.grid(row=2, column=3)
        self.btn_sub.grid(row=3, column=3)
        self.btn_sum.grid(row=4, column=3, pady=5)

    def event_on_write(self, *args):
        """
        Impossibilita escrita de caracteres não númericos a partir do teclado.
        """

        valores = self.valores.get()

        if len(valores) > 0:
            if not valores[-1].isnumeric() \
                    and valores[-1] != '+' \
                    and valores[-1] != '-' \
                    and valores[-1] != '*' \
                    and valores[-1] != '/' \
                    and valores[-1] != '.':
                self.valores.set(valores[:-1])

            if valores[0] in '*/+.':
                self.valores.set('')

        if len(valores) > 1:
            if valores[-1] == '+' and valores[-2] == '+':
                self.valores.set(valores[:-1])
            if valores[-1] == '-' and valores[-2] == '-':
                self.valores.set(valores[:-1])
            if valores[-1] == '*' and valores[-2] == '*':
                self.valores.set(valores[:-1])
            if valores[-1] == '/' and valores[-2] == '/':
                self.valores.set(valores[:-1])
            if valores[-1] == '.' and valores[-2] == '.':
                self.valores.set(valores[:-1])
            if valores[-2] in '*/-+.' and valores[-1] in '*/-+.':
                self.valores.set(valores[:-1])

    def add_number(self, number):
        if 'Erro' == self.valores.get():
            self.valores.set('')
        self.valores.set(self.valores.get() + number)

        self.textbox.icursor(END)
        self.textbox.focus_force()

    def add_simbol(self, simbol):
        if len(self.valores.get()) > 0:
            if self.valores.get()[-1] not in '/*-+':
                self.valores.set(self.valores.get() + simbol)
        else:
            if simbol == '-':
                self.valores.set(simbol)

        self.textbox.icursor(END)
        self.textbox.focus_force()

    def insert_1(self):
        self.add_number('1')

    def insert_2(self):
        self.add_number('2')

    def insert_3(self):
        self.add_number('3')

    def insert_4(self):
        self.add_number('4')

    def insert_5(self):
        self.add_number('5')

    def insert_6(self):
        self.add_number('6')

    def insert_7(self):
        self.add_number('7')

    def insert_8(self):
        self.add_number('8')

    def insert_9(self):
        self.add_number('9')

    def insert_0(self):
        self.add_number('0')

    def insert_p(self):
        self.add_number('.')

    def insert_c(self):
        if "Erro" == self.valores.get():
            self.valores.set('')
        else:

            self.valores.set(self.valores.get()[:-1])

        self.textbox.icursor(END)
        self.textbox.focus_force()

    def insert_ce(self):
        self.valores.set('')
        self.textbox.icursor(END)
        self.textbox.focus_force()

    def insert_div(self):
        floatNull = re.compile(r'(-)*\d+(\.\d+)*')
        if floatNull.match(self.valores.get()):
            self.add_simbol('/')
        else:
            self.textbox.icursor(END)
            self.textbox.focus_force()

    def insert_x(self):
        floatNull = re.compile(r'(-)*\d+(\.\d+)*')
        if floatNull.match(self.valores.get()):
            self.add_simbol('*')
        else:
            self.textbox.icursor(END)
            self.textbox.focus_force()

    def insert_sub(self):
        floatNull = re.compile(r'(-)*\d+(\.\d+)*')
        if floatNull.match(self.valores.get()) or self.valores.get() == '':
          self.add_simbol('-')
        else:
            self.textbox.icursor(END)
            self.textbox.focus_force()

    def insert_sum(self):
        floatNull = re.compile(r'(-)*\d+(\.\d+)*')
        if floatNull.match(self.valores.get()):
            self.add_simbol('+')
        else:
            self.textbox.icursor(END)
            self.textbox.focus_force()

    def insert_shift(self):
        # Calculadora cientifica
        self.textbox.icursor(END)
        self.textbox.focus_force()


    def key_backspace(self):
        if 'Erro' == self.valores.get():
            self.valores.set('')
        else:
            self.textbox.icursor(END)
            self.textbox.focus_force()

    def calcula(self):
        floatBeInt = re.compile(r'\d+.0*')
        fractionResult = re.compile(r'(-)*\d+/(-)*\d+')
        smallDecimal = re.compile(r'(-)*\d+\.\d+')
        largeDecimal = re.compile(r'\d+\.\d\d\d')

        try:
            self.valores.set(sympy.sympify(self.valores.get()))
            print(self.valores.get())

            if smallDecimal.match(self.valores.get()):
                self.valores.set(float(self.valores.get()))

            if fractionResult.match(self.valores.get()):
                self.valores.set(sympy.Float(self.valores.get()))

                if smallDecimal.match(self.valores.get()):
                    self.valores.set(float(self.valores.get()))
                else:
                    self.valores.set(round(sympy.Float(self.valores.get()), 3))

        except:
            if '' == self.valores.get():
                self.valores.set('')
            else:
                self.valores.set('Error')

        self.textbox.icursor(END)
        self.textbox.focus_force()
