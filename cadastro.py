import customtkinter as ctk
from PIL import Image
import os, sys

class Cadastro():
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.geometry('1440x900')

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))
  
  def cadastro(self):
    frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    frame.place(relwidth=1, relheight=1)

    texto = ctk.CTkImage(Image.open(f"{self.basePath()}/texto.png"), size=(487,80))
    texto_place = ctk.CTkLabel(frame, image=texto, text='')
    texto_place.place(rely=0.25, relx=0.5, anchor="center")

    nome_completo = ctk.CTkEntry(frame, width=440, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Arial", 24))
    nome_completo.place(rely=0.4,relx=0.5, anchor="center")

    nome_completo_label = ctk.CTkLabel(frame, text='Nome completo', text_color='Black', font=("Arial", 24, "bold"))
    nome_completo_label.place(rely=0.344,relx=0.47, anchor="ne")

    cpf = ctk.CTkEntry(frame, width=207, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Arial", 24))
    cpf.place(rely=0.48,relx=0.49, anchor="ne")

    cpf_label = ctk.CTkLabel(frame, text='CPF', text_color='Black', font=("Arial", 24, "bold"))
    cpf_label.place(rely=0.445,relx=0.376, anchor="ne")

    rg = ctk.CTkEntry(frame, width=207, height=42, fg_color="#8ED6D0", border_width=0, text_color='Black', font=("Arial", 24))
    rg.place(rely=0.48,relx=0.51, anchor="nw")

    rg_label = ctk.CTkLabel(frame, text='RG', text_color='Black', font=("Arial", 24, "bold"))
    rg_label.place(rely=0.445,relx=0.535, anchor="ne")

    curva = ctk.CTkImage(Image.open(f"{self.basePath()}/curva.png"),size=(1618, 185))
    curva_place = ctk.CTkLabel(frame, image=curva, text='')
    curva_place.place(rely=0.9, relx=0.5, anchor="center")

    self.root.mainloop()

if __name__ == "__main__":
  Cadastro().cadastro()