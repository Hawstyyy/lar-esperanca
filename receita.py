from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from tkinter import messagebox
from util import imagemCTK, FontsUI
from hotbar import Hotbar
from db_handler import DB
from search_bar import SearchBar

#-----------------------TELA --------------------------------

class Receita(CTkFrame):
    BGC = '#ffffff'
    COR = '#8ED6D0'
    TX = '#000000'

    def __init__(self, master: CTkFrame, user:str):
        super().__init__(master)

        self.configure(fg_color='white', corner_radius=0)
        self.place(relheigh=1, relwidth=1)

        self.user = user

        #Hotbar
        self.f_hotbar = Hotbar(self, self.user)
        #self.f_hotbar.place(relx=0.5, rely=0, relwidth=1, anchor='n')

        #Footer
        self.footer = ctk.CTkLabel(self, height=151, text='', image=imagemCTK('imagens/curva_rodape.png', 1920, 151))
        self.footer.place(relx=0.5, rely=1, anchor='s')

        #Frame 
        self.f_holder = CTkFrame(
            self,
            width=440,
            height=600,
            fg_color=self.BGC
        )
        self.f_holder.place(relx=0.5, rely=0.5, anchor='center')

        #titulo
        ctk.CTkLabel(
            self.f_holder,
            text='Nova Receita',
            fg_color=self.BGC,
            font=FontsUI.titulo,
            text_color=self.TX
        ).place(relx=0.5, rely=0, anchor='n')

        ctk.CTkLabel(
            self.f_holder,
            text='',
            image=imagemCTK('imagens/linha_torcida.png', 344, 36)
        ).place(relx=0.5, rely=0.1, anchor='n')

        #Nome paciente
        ctk.CTkLabel(
            self.f_holder,
            text='Nome do paciente',
            fg_color=self.BGC,
            font=FontsUI.simples,
            text_color=self.TX,
            anchor='w'
        ).place(relx=0.5, rely=0.25, anchor='s', relwidth=1)

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        #Pegando lista de Pacientes do banco
        self.db = DB()
        self.db.exec('select nome_paciente from paciente')

        self.lista_pacientes =  [item[0] for item in self.db.f_all()]
        self.db.close()

        #Search Bar
        self.search_bar = SearchBar(self.f_holder, height=40, values=self.lista_pacientes, bg_color='white')
        self.search_bar.place(relx=0.5, rely=0.25, anchor='n', relwidth=1)
        self.search_bar.update()

        #Remedio
        ctk.CTkLabel(
            self.f_holder,
            text='Remédio',
            fg_color=self.BGC,
            font=FontsUI.simples,
            text_color=self.TX,
            anchor='w'
        ).place(relx=0.5, rely=0.4, anchor='s', relwidth=1)

        self.e_remedio = ctk.CTkEntry(
            self.f_holder,
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#ffffff',
            border_width=0
        )
        self.e_remedio.place(relx=0.5, rely=0.4, anchor='n', relwidth=1)
        
        #Hora inicial
        ctk.CTkLabel(
            self.f_holder,
            text='Horário da Primeira Dose',
            fg_color=self.BGC,
            font=('Segoe UI', 20),
            text_color=self.TX,
            anchor='w'
        ).place(relx=0, rely=0.55, anchor='sw', relwidth=0.54)

        self.e_hora_inicial = ctk.CTkEntry(
            self.f_holder,
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#ffffff',
            border_width=0
        )
        self.e_hora_inicial.place(relx=0, rely=0.55, anchor='nw', relwidth=0.54)

        #Intervalo
        ctk.CTkLabel(
            self.f_holder,
            text='Intervalo(horas)',
            fg_color=self.BGC,
            font=FontsUI.simples,
            text_color=self.TX,
            anchor='w'
        ).place(relx=1, rely=0.55, anchor='se', relwidth=0.42)

        self.e_hora_inicial = ctk.CTkEntry(
            self.f_holder,
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#ffffff',
            border_width=0
        )
        self.e_hora_inicial.place(relx=1, rely=0.55, anchor='ne', relwidth=0.42)

        self.b_adicionar = ctk.CTkButton(
            self.f_holder,
            text='ADICIONAR',
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#ffffff',
            border_width=0,
            command=
                lambda: print('yoo'), hover_color='#2D5E6C'
        )
        self.b_adicionar.place(relx=0.5, rely=0.7, anchor='n')

        self.search_bar.tkraise()


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)
    frame = Receita(root, 'Brabo')
    root.mainloop()