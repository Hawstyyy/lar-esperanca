import customtkinter as ctk
from PIL import Image
import os, sys
from hotbar import Hotbar
import util
import db_handler as db
 
class Sinais_vitais():
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')
    self.root.state('zoomed')
    self.root.title("Sinais Vitais")
    self.root.resizable(False, False)
    self.p_sinal_vital = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    self.p_sinal_vital.place(relwidth=1, relheight=1)
    database = db.DB()
    self.status_label = None
 
  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))
  
  def insercao(self):
    pass
 
  def atualizar_status(self):
    if self.status_label is None:
            self.status_label = ctk.CTkLabel(
                self.p_sinal_vital, 
                text="Normal",  # Initial value
                text_color="white", 
                font=("Segoe UI", 28, "bold"), 
                fg_color="#8ED6D0"
            )
            self.status_label.place(rely=0.69, relx=0.41, anchor="center")
  def sinais_vitais(self):
    
    #self.f_hotbar = Hotbar(self.root)
    
    # Imagem texto encima
    registrar_sinal_vital_texto = ctk.CTkLabel(self.p_sinal_vital, text= "Registrar Sinal Vital", text_color="black", font= ("Segoe UI",40))
    registrar_sinal_vital_texto.place(rely = 0.25, relx = 0.5, anchor = "center")
    width_tela = self.root.winfo_width()
    
    curva_place = ctk.CTkLabel(self.p_sinal_vital, image=util.Utils.imagemCTK("imagens/linha_torcida.png",344,36), text='')
    curva_place.place(rely=0.3, relx=0.5, anchor="center")
    
    # Entries do sinal vital
    nome_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "Nome do paciente", text_color="black", font= ("Segoe UI",30))
    nome_cliente.place(rely = 0.35, relx = 0.45, anchor = "center")
    nome_cliente_entry = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 440)
    nome_cliente_entry.place(rely = 0.4, relx = 0.5, anchor = "center")

    # Temperatura cliente
    temperatura_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "Temperatura", text_color="black", font= ("Segoe UI",28))
    temperatura_cliente.place(rely = 0.45, relx = 0.425, anchor = "center")
    temperatura_cliente_entry = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 140)
    temperatura_cliente_entry.place(rely = 0.5, relx = 0.423, anchor = "center")
    # Pressão Sanguinea
    pressao_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "Pressão Sanguinea", text_color="black", font= ("Segoe UI",28))
    pressao_cliente.place(rely = 0.45, relx = 0.545, anchor = "center")
    # Entry 1
    pressao_cliente_entry_1 = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 140)
    pressao_cliente_entry_1.place(rely = 0.5, relx = 0.52, anchor = "center")
    # Entry 2    
    pressao_cliente_entry_2 = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 100)
    pressao_cliente_entry_2.place(rely = 0.5, relx = 0.587, anchor = "center")

    # BPM
    bpm_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "BPM", text_color="black", font= ("Segoe UI",28))
    bpm_cliente.place(rely = 0.55, relx = 0.4, anchor = "center")
    bpm_cliente_entry = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 140)
    bpm_cliente_entry.place(rely = 0.6, relx = 0.423, anchor = "center")

    # Saturação
    saturacao_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "Saturação", text_color="black", font= ("Segoe UI",28))
    saturacao_cliente.place(rely = 0.55, relx = 0.515, anchor = "center")
    saturacao_cliente_entry = ctk.CTkEntry(self.p_sinal_vital, text_color= "black", fg_color= "#8ED6D0",font= ("Segoe UI",36), border_width= 0, corner_radius= 10, width= 140)
    saturacao_cliente_entry.place(rely = 0.6, relx = 0.52, anchor = "center")

    # Status do cliente
    quadrado_frame = ctk.CTkFrame(self.p_sinal_vital, width= 450, height= 50, corner_radius= 10, fg_color= "#8ED6D0")
    quadrado_frame.place(rely = 0.69, relx = 0.5, anchor = "center")
    status_cliente = ctk.CTkLabel(self.p_sinal_vital, text= "Status :", text_color="white", font= ("Segoe UI",28, "bold"), fg_color= "#8ED6D0")
    status_cliente.place(rely = 0.69, relx = 0.41, anchor = "center")


    # Imagem de curva embaixo
    curva_place = ctk.CTkLabel(self.p_sinal_vital, image= util.Utils.imagemCTK("curva.png", width_tela,151), text='')
    curva_place.place(rely=0.925, relx=0.5, anchor="center")

    self.atualizar_status()
    self.root.mainloop()
 
if __name__ == "__main__":
  Sinais_vitais().sinais_vitais()