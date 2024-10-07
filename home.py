import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from util import imagemCTK
 
# TELA --------------------------------------------------------

# Função para abrir nova janela ou realizar ações dos botões
def abrir_pacientes():
    messagebox.showinfo("Pacientes", "Tela de pacientes em desenvolvimento")

def nova_receita():
    messagebox.showinfo("Nova Receita", "Tela de nova receita em desenvolvimento")

def abrir_registros():
    messagebox.showinfo("Registros", "Tela de registros em desenvolvimento")

def novo_registro():
    messagebox.showinfo("Novo Registro", "Tela de novo registro em desenvolvimento")

#Socorro
# TELA --------------------------------------------------------
janela = ctk.CTk()
janela.after(0, janela.state('zoomed'))
janela.configure(fg_color='white')
janela.title("Home")

# Conteúdo principal ----------------------------------------
# Adicionando a imagem da médica no centro
doctor_img = imagemCTK('imagens/fotomulher.png', 600, 700)
doctor_label = ctk.CTkLabel(janela, image=doctor_img, text="", fg_color="transparent")
doctor_label.place(x=50, y=200)  # Ajuste as coordenadas conforme necessário

# Criando um frame para os botões     
frame_buttons = ctk.CTkFrame(janela, fg_color="white", corner_radius=0)
frame_buttons.place(x=650, y=200)  # Ajuste as coordenadas conforme necessário

# Botões principais (Pacientes, Nova Receita, Registros, Novo Registro)
btn_pacientes = ctk.CTkButton(frame_buttons, text="Pacientes", width=200, height=80, fg_color="#00A699", hover_color="#007E6E", command=abrir_pacientes)
btn_pacientes.grid(row=0, column=0, padx=20, pady=20)

btn_receita = ctk.CTkButton(frame_buttons, text="Nova Receita", width=200, height=80, fg_color="#00A699", hover_color="#007E6E", command=nova_receita)
btn_receita.grid(row=0, column=1, padx=20, pady=20)

btn_registros = ctk.CTkButton(frame_buttons, text="Registros", width=200, height=80, fg_color="#00A699", hover_color="#007E6E", command=abrir_registros)
btn_registros.grid(row=1, column=0, padx=20, pady=20)

btn_novo_registro = ctk.CTkButton(frame_buttons, text="Novo Registro", width=200, height=80, fg_color="#00A699", hover_color="#007E6E", command=novo_registro)
btn_novo_registro.grid(row=1, column=1, padx=20, pady=20)

janela.mainloop()
