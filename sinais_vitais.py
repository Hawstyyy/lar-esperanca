import customtkinter as ctk
from PIL import Image
import os, sys

 
class Sinais_vitais():
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.after(0, self.root.state('zoomed'))
    self.root.title("Sinais Vitais")
    self.root.resizable(False, False)
 
  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))
 
  def sinais_vitais(self):
    p_sinal_vital = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    p_sinal_vital.place(relwidth=1, relheight=1)
    
    # Entries do sinal vital
    nome_cliente = ctk.CTkLabel(p_sinal_vital, text= "Nome do paciente", text_color="black", font= ("Segoe UI",36))
    nome_cliente.place(rely = 0.5, relx = 0.5, anchor = "center")


    # Imagem de curva embaixo
    width_tela = self.root.winfo_width()
    curva = ctk.CTkImage(Image.open(f"{self.basePath()}/curva.png"),size=(width_tela, 151))
    curva_place = ctk.CTkLabel(p_sinal_vital, image=curva, text='')
    curva_place.place(rely=0.925, relx=0.5, anchor="center")
 
 
    self.root.mainloop()
 
if __name__ == "__main__":
  Sinais_vitais().sinais_vitais()