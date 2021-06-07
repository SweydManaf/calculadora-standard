from tkinter import *

from ttkthemes import ThemedStyle

from scene1 import Scene1


class Main:
    """Root Master"""

    def __init__(self):
        self.master = Tk()
        self.master.title('Calculadora')
        self.style = ThemedStyle(self.master)
        self.style.set_theme('radiance')

        # Configuracoes da janela
        self.width = 370
        self.height = 360

        self.width_sys = int(self.master.winfo_screenwidth() / 2 - self.width / 2)
        self.height_sys = int(self.master.winfo_screenheight() / 2 - self.height / 2)

        # Configuracoes de redimensao
        self.master.maxsize(self.width, self.height)
        self.master.minsize(self.width, self.height)
        self.master.geometry(f'{self.width}x{self.height}+{self.width_sys}+{self.height_sys}')

        self.frame1 = Scene1(self.master)

        self.master.focus_force()
        self.master.mainloop()


if __name__ == '__main__':
    Main()
