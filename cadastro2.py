import customtkinter as ctk
from PIL import Image
from hotbar import Hotbar
import util

class Cadastro2:
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    self.frame.place(relwidth=1, relheight=1)
    self.root.after(0, lambda:self.root.state('zoomed'))
    self.root.title("Lar esperança")
    hotbar = Hotbar(self.frame)

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

  def cadastro2(self):
    div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
    div.place(x=761, y=186)

    self.imagem("imagens/lar_esperanca.png", self.frame, 739, 224, 477, 82)

    self.texto(self.frame, "Usuário", util.FontsUI.simples_negrito, 763, 421)
    self.entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 760, 451)

    self.texto(self.frame, "Senha", util.FontsUI.simples_negrito, 761, 500)
    self.entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 758, 530)

    self.texto(self.frame, "Confirmar senha", util.FontsUI.simples_negrito, 761, 579)
    self.entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 758, 609)

    self.botao(self.frame, "Finalizar", util.FontsUI.simples, 162, 53, "#19AAA5", "White", None, 896, 688)

    div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
    div.place(x=748, y=848)

    self.imagem("imagens/curva_rodape.png", self.frame, 0, 850, 2158, 210)
    self.root.mainloop()

if __name__ == "__main__":
  Cadastro2().cadastro2()