from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from tkinter import messagebox
from util import imagemCTK, FontsUI
from hotbar import Hotbar
from db_handler import DB
from search_bar import SearchBar
from hour_entry import HourEntry
from datetime import time

#-----------------------TELA --------------------------------

class Receita(CTkFrame):
    BGC = '#ffffff'
    COR = '#8ED6D0'
    TX = '#18504B'

    def __init__(self, master: CTkFrame, funcionario:int):
        super().__init__(master)

        self.configure(fg_color='white', corner_radius=0)
        self.place(relheigh=1, relwidth=1)

        self.func = funcionario

        #Hotbar
        #self.f_hotbar = Hotbar(self, self.user)
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

        #Search Nome Paciente
        self.search_paciente = SearchBar(self.f_holder, primary='id_paciente', column='nome_paciente', table='paciente', height=40, bg_color='white')
        self.search_paciente.place(relx=0.5, rely=0.25, anchor='n', relwidth=1)

        #Remédio
        ctk.CTkLabel(
            self.f_holder,
            text='Remédio',
            fg_color=self.BGC,
            font=FontsUI.simples,
            text_color=self.TX,
            anchor='w'
        ).place(relx=0.5, rely=0.4, anchor='s', relwidth=1)

        #Search Nome Remédio
        self.search_remedio = SearchBar(self.f_holder, primary='id_remedio', column='nome_remedio', table='remedio', height=40, bg_color='white')
        self.search_remedio.place(relx=0.5, rely=0.4, anchor='n', relwidth=1)

        #Hora inicial
        ctk.CTkLabel(
            self.f_holder,
            text='Horário da Primeira Dose',
            fg_color=self.BGC,
            font=('Segoe UI', 20),
            text_color=self.TX,
            anchor='w'
        ).place(relx=0, rely=0.55, anchor='sw', relwidth=0.54)

        self.e_hora = HourEntry(self.f_holder, width=100, height=40)
        self.e_hora.place(relx=0, rely=0.55, anchor='nw')

        #Intervalo
        ctk.CTkLabel(
            self.f_holder,
            text='Intervalo(horas)',
            fg_color=self.BGC,
            font=FontsUI.simples,
            text_color=self.TX,
            anchor='w'
        ).place(relx=1, rely=0.55, anchor='se', relwidth=0.42)

        self.validate_entry_hour = (self.register(self.validate_hour), '%S', '%P', '%i')

        self.e_hora_intervalo = ctk.CTkEntry(
            self.f_holder,
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#000000',
            border_width=0,
            validate="key",
            validatecommand=self.validate_entry_hour
        )
        self.e_hora_intervalo.place(relx=1, rely=0.55, anchor='ne', relwidth=0.42)

        self.b_adicionar = ctk.CTkButton(
            self.f_holder,
            text='ADICIONAR',
            corner_radius=5,
            fg_color=self.COR,
            font=FontsUI.simples,
            text_color='#000000',
            border_width=0,
            command=self.validate_receita,
            hover_color='#2D5E6C'
        )
        self.b_adicionar.place(relx=0.5, rely=0.7, anchor='n')

    def validate_hour(self, char: str, current_text: str, cursor_position: int):
        if len(current_text) > 2:
            return False
        if current_text == '':
            return True
        if not current_text.isdigit():
            return False
        if int(current_text) < 0 or int(current_text) > 23:
            return False

        return True
    
    def validate_receita(self):
        if(self.search_paciente._selected_id
            and self.search_remedio._selected_id
            and self.e_hora.get_time()
            and self.e_hora_intervalo.get()
        ):
            #print(self.search_paciente._selected_id,
            #self.search_remedio._selected_id,
            #self.e_hora.get_time(),
            #self.e_hora_intervalo.get())

            paciente_id = int(self.search_paciente._selected_id)
            remedio_id = int(self.search_remedio._selected_id)
            hora = self.e_hora.get_time()
            hora_inicial = time(hora[0], hora[1])
            intervalo = int(self.e_hora_intervalo.get())

            #print(paciente_id, remedio_id, hora_inicial, intervalo)

            try:
                db = DB()
                query = """
                    insert into receita
                        values (
                            NULL,
                            %s,
                            %s,
                            %s,
                            true,
                            %s,
                            %s
                        )
                """
                db.exec(query, (paciente_id, remedio_id, self.func, hora_inicial, intervalo))
                db.commit()
                db.close()
            except Exception as e:
                messagebox.showerror('Algo deu errado!', f'Ocorreu um erro na conexão com o banco de dados!\nErro:{e}')

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)
    frame = Receita(root, 2)


    #dt = datetime.combine(date.today(), time(13, 20)) + timedelta(hours=15)
    #print (dt.time())
    #print(time(13,45))
    root.mainloop()
    