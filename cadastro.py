import customtkinter as ctk
from PIL import Image
import os, sys

class Cadastro():
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.geometry('1440x900')
    self.root.resizable(False, False)

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))
  
  def cadastro(self):
    frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    frame.place(relwidth=1, relheight=1)

    div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
    div.place(relx=0.5, rely=0.15, anchor="center")

    texto = ctk.CTkImage(Image.open(f"{self.basePath()}/texto.png"), size=(487,80))
    texto_place = ctk.CTkLabel(frame, image=texto, text='')
    texto_place.place(rely=0.25, relx=0.5, anchor="center")

    nome_completo = ctk.CTkEntry(frame, width=440, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    nome_completo.place(rely=0.4,relx=0.5, anchor="center")

    nome_completo_label = ctk.CTkLabel(frame, text='Nome completo', text_color='Black', font=("Segoe UI", 24, "bold"))
    nome_completo_label.place(rely=0.34,relx=0.475, anchor="ne")

    cpf = ctk.CTkEntry(frame, width=207, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    cpf.place(rely=0.48,relx=0.49, anchor="ne")

    cpf_label = ctk.CTkLabel(frame, text='CPF', text_color='Black', font=("Segoe UI", 24, "bold"))
    cpf_label.place(rely=0.444,relx=0.378, anchor="ne")

    rg = ctk.CTkEntry(frame, width=207, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    rg.place(rely=0.48,relx=0.51, anchor="nw")

    rg_label = ctk.CTkLabel(frame, text='RG', text_color='Black', font=("Segoe UI", 24, "bold"))
    rg_label.place(rely=0.444,relx=0.535, anchor="ne")

    endereco = ctk.CTkEntry(frame, width=440, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    endereco.place(rely=0.6,relx=0.5, anchor="center")

    endereco_label = ctk.CTkLabel(frame, text='Endereço', text_color='Black', font=("Segoe UI", 24, "bold"))
    endereco_label.place(rely=0.54,relx=0.42, anchor="ne")

    data = ctk.CTkEntry(frame, width=60, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    data.place(rely=0.7,relx=0.365, anchor="center")

    mes = ctk.CTkEntry(frame, width=60, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    mes.place(rely=0.7,relx=0.41, anchor="center")

    ano = ctk.CTkEntry(frame, width=60, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Segoe UI", 24))
    ano.place(rely=0.7,relx=0.455, anchor="center")

    data_de_nascimento_label = ctk.CTkLabel(frame, text='Data de nascimento', text_color='Black', font=("Segoe UI", 24, "bold"))
    data_de_nascimento_label.place(rely=0.64,relx=0.502, anchor="ne")

    div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
    div.place(relx=0.5, rely=0.83, anchor="center")

    curva = ctk.CTkImage(Image.open(f"{self.basePath()}/curva.png"),size=(1618, 185))
    curva_place = ctk.CTkLabel(frame, image=curva, text='')
    curva_place.place(rely=0.9, relx=0.5, anchor="center")

    botao_prosseguir = ctk.CTkButton(frame, text="Prosseguir", width=162, height=63, corner_radius=5, fg_color="#19AAA5", font=("Segoe UI", 28), text_color="white")
    botao_prosseguir.place(rely=0.773, relx=0.5, anchor="center")

    self.root.mainloop()

if __name__ == "__main__":
  Cadastro().cadastro()