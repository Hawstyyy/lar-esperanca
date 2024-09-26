
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import pymysql.cursors # pip install PyMySQL para adquirir essa blibioteca
# Tkinter é utilizado para criação da interface e janela.
from receita import Receita
from sinais_vitais import Sinais_vitais


class App():
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.title('Lar Esperança')
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')
        self.root.state('zoomed')
        self.root.resizable(False,False)

        self.receita = Receita(self.root, 'Cunha')
        self.receita.b_adicionar.configure(command=lambda: self.sinal_vital(2))
    
        self.root.mainloop()

    def sinal_vital(self, id_paciente: int):
        if(hasattr(self, 'p_sinal')):
            self.p_sinal.mudar_paciente(id_paciente)
            self.p_sinal.tkraise()

        self.p_sinal = Sinais_vitais(self.root, id_paciente)

if __name__ == '__main__':
    App()