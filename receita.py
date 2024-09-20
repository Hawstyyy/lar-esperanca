import customtkinter as ctk
from customtkinter import CTkFrame
from tkinter import messagebox
from util import Utils as U
from PIL import Image
from hotbar import Hotbar


BGC = 'white'
COR = '#8ED6D0'
TX = 'black'
# TELA --------------------------------------------------------

def imagemFrom(path: str, largura: int = 300, altura: int = 300) -> ctk.CTkImage:
    img = Image.open(path).convert("RGBA")
    return ctk.CTkImage(
        light_image=img,
        dark_image=img,
        size=(largura, altura)
    )

class Receita(CTkFrame):
    def __init__(self, master: Image.Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Image.Tuple[str] = "transparent", fg_color: str | Image.Tuple[str] | None = None, border_color: str | Image.Tuple[str] | None = None, background_corner_colors: Image.Tuple[str | Image.Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.place(relheigh=1, relwidth=1)

        self.p_hotbar = Hotbar(self)

        #Frame 
        self.p_holder = CTkFrame(self, width=440, height=600, fg_color=BGC)
        self.p_holder.place(relx=0.5, rely=0.5, anchor='center')

        #titulo
        ctk.CTkLabel(self.p_holder, text='Nova Receita', fg_color=BGC, font=U.f_titulo, text_color=TX).place(relx=0.5, rely=0, anchor='n')
        ctk.CTkLabel(self.p_holder, text='', image=imagemFrom('linha_torcida.png', 344, 36)).place(relx=0.5, rely=0.1, anchor='n')

        #Nome paciente
        ctk.CTkLabel(self.p_holder, text='Nome do paciente', fg_color=BGC, font=U.f_simples, text_color=TX, anchor='w').place(relx=0.5, rely=0.25, anchor='s', relwidth=1)

        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)

        self.lista_pacientes = ['\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t','Lucas', 'Ana', 'João', 'Maria', 'Pedro', 'Carolina', 'Rafael', 'Juliana', 'Bruno', 'Fernanda']
        self.optionmenu = ctk.CTkOptionMenu(
            self.p_holder,
            fg_color=COR,
            text_color=TX,
            font=U.f_simples,
            corner_radius=10,
            dropdown_fg_color=COR,
            dropdown_font=U.f_simples,
            dropdown_hover_color='white',
            dropdown_text_color=TX,
            button_color='#2D5E6C',
            values=self.lista_pacientes,
            command=optionmenu_callback
        )
        self.optionmenu.place(relx=0.5, rely=0.25, anchor='n', relwidth=1)
        
        #Remedio
        ctk.CTkLabel(self.p_holder, text='Remédio', fg_color=BGC, font=U.f_simples, text_color=TX, anchor='w').place(relx=0.5, rely=0.4, anchor='s', relwidth=1)
        self.e_remedio = ctk.CTkEntry(self.p_holder, corner_radius=10, fg_color=COR, font=U.f_simples,text_color=TX,  border_width=0)
        self.e_remedio.place(relx=0.5, rely=0.4, anchor='n', relwidth=1)
        
        #Hora inicial
        ctk.CTkLabel(self.p_holder, text='Horário da Primeira Dose', fg_color=BGC, font=('Segoe UI', 20), text_color=TX, anchor='w').place(relx=0, rely=0.55, anchor='sw', relwidth=0.54)
        self.e_hora_inicial = ctk.CTkEntry(self.p_holder, corner_radius=10, fg_color=COR, font=U.f_simples,text_color=TX,  border_width=0)
        self.e_hora_inicial.place(relx=0, rely=0.55, anchor='nw', relwidth=0.54)

        #Intervalo
        ctk.CTkLabel(self.p_holder, text='Intervalo(horas)', fg_color=BGC, font=U.f_simples, text_color=TX, anchor='w').place(relx=1, rely=0.55, anchor='se', relwidth=0.42)
        self.e_hora_inicial = ctk.CTkEntry(self.p_holder, corner_radius=10, fg_color=COR, font=U.f_simples,text_color=TX,  border_width=0)
        self.e_hora_inicial.place(relx=1, rely=0.55, anchor='ne', relwidth=0.42)

        ctk.CTkButton(self.p_holder, text='ADICIONAR', corner_radius=10, fg_color=COR, font=U.f_simples,text_color=TX,  border_width=0, command=lambda: print('yeee'), hover_color='#2D5E6C').place(relx=0.5, rely=0.7, anchor='n')








if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)
    frame = Receita(root, fg_color='white')
    root.mainloop()