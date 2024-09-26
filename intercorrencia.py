import customtkinter as ctk
from hotbar import Hotbar
from PIL import Image
import util

class Intercorrencia:
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.set_geometry(self.root ,1440 ,900)
    self.root.resizable(False, False)
    self.frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    self.frame.place(relwidth=1, relheight=1)
    self.f_hotbar = Hotbar(self.frame)
    self.root.title("Lar Esperança")

  def set_geometry(self, master, width, height):
    screen_width = self.root.winfo_screenwidth()
    screen_height = self.root.winfo_screenheight()
    app_width = width
    app_height = height

    x = (screen_width // 2) - (app_width // 2)
    y = (screen_height // 2) - (app_height // 2)

    master.geometry(f'{app_width}x{app_height}+{x}+{y}')
  
  def texto(self, master, text, f_texto, x, y, color='Black'):
      texto = ctk.CTkLabel(master, text=text, font=(f_texto), text_color=color)
      texto.place(x=x, y=y)

  def botao(self, master, text, f_texto, width, height, color, text_color, command, x, y):
      botao = ctk.CTkButton(master, text=text, width=width, height=height, font=(f_texto), fg_color=color, text_color=text_color, command=command)
      botao.place(x=x, y=y)
      return botao

  def imagem(self, name, master, x, y, sizeX, sizeY):
    imagem = ctk.CTkImage(Image.open(f"{util.basePath()}/{name}"), size=(sizeX, sizeY))
    imagem_place = ctk.CTkLabel(master, image=imagem, text='')
    imagem_place.place(x=x, y=y)

  def entry(self, master, width, height, fg_color, border_width, text_color, f_font, x, y):
    entry = ctk.CTkEntry(master, width=width, height=height, fg_color=fg_color, border_width=border_width, text_color=text_color, font=(f_font))
    entry.place(x=x,y=y)
  
  def intercorrencia(self):
    self.texto(self.frame, 'Intercorrência', util.FontsUI.titulo, 600, 289)
    self.imagem("imagens/linha_torcida.png", self.frame, 549, 339, 342, 30)

    self.texto(self.frame, 'Descreva as alterações do paciente', util.FontsUI.simples, 500, 405)

    self.entry(self.frame, 440, 42, '#8ED6D0', 0, 'Black', util.FontsUI.simples, 500, 441)

    self.texto(self.frame, 'Ligue aqui para Emergência →', util.FontsUI.simples, 445, 509)
    self.botao(self.frame, 'Ligar', util.FontsUI.simples, 171, 42, '#8ED6D0', '#2D5E6C', None, 769, 507)

    self.botao(self.frame, 'Adicionar', util.FontsUI.simples, 162, 53, '#19AAA5', 'White', None, 639, 608)

    self.imagem(f"{'/imagens/curva_rodape.png'}", self.frame, 0, 750, 1618, 185)
    self.root.mainloop()

if __name__ == '__main__':
  Intercorrencia().intercorrencia()