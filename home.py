import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
 
# TELA --------------------------------------------------------
 
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

# Função para abrir nova janela ou realizar ações dos botões
def abrir_pacientes():
    messagebox.showinfo("Pacientes", "Tela de pacientes em desenvolvimento")

def nova_receita():
    messagebox.showinfo("Nova Receita", "Tela de nova receita em desenvolvimento")

def abrir_registros():
    messagebox.showinfo("Registros", "Tela de registros em desenvolvimento")

def novo_registro():
    messagebox.showinfo("Novo Registro", "Tela de novo registro em desenvolvimento")

# TELA --------------------------------------------------------
janela = ctk.CTk()
janela.after(0, janela.state('zoomed'))
janela.configure(fg_color='white')
janela.title("Home")

# Cabeçalho superior -----------------------------------------
frame_top = ctk.CTkFrame(janela, height=70, fg_color='#EAF6F7', corner_radius=0)
frame_top.pack(side="top", fill="x")

# Ícone usuário
img_user = Image.open("/Users/RicardoSilva/Downloads/Captura de tela_24-9-2024_91526_www.figma.com.jpeg")  # Coloque o caminho para a imagem do ícone do usuário
img_user = img_user.resize((80, 80), Image.LANCZOS)
user_icon = ctk.CTkImage(img_user)
user_label = ctk.CTkLabel(frame_top, image=user_icon, text="NomeUser", fg_color="transparent", anchor="w")
user_label.place(x=1200, y=15)  # Ajuste as coordenadas conforme necessário

# Ícone logotipo
img_logo = Image.open("/Users/RicardoSilva/Downloads/amoreesperanca (1).png")  # Substitua pelo caminho para seu logotipo
img_logo = img_logo.resize((100, 100),Image.LANCZOS)
logo_icon = ctk.CTkImage(img_logo)
logo_label = ctk.CTkLabel(frame_top, image=logo_icon, text="", fg_color="transparent")
logo_label.place(x=10, y=15)  # Ajuste as coordenadas conforme necessário

# Conteúdo principal ----------------------------------------
# Adicionando a imagem da médica no centro
img_doctor = Image.open("/Users/RicardoSilva/Downloads/Captura de tela_24-9-2024_82432_www.figma.com.jpeg")  # Substitua pelo caminho para a imagem da médica
img_doctor = img_doctor.resize((700, 600), Image.LANCZOS)
doctor_img = ctk.CTkImage(img_doctor)
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
