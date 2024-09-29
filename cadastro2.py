import customtkinter as ctk
from PIL import Image
import os, sys
from hotbar import Hotbar
from intercorrencia import Intercorrencia
import util

if __name__ == "__main__":

  class Cadastro2:
    def __init__(self) -> None:
      self.root = ctk.CTk()
      self.frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
      self.frame.place(relwidth=1, relheight=1)
      Intercorrencia().set_geometry(self.root ,1440 ,900)
      self.root.resizable(False, False)
      self.root.title("Lar esperança")
      hotbar = Hotbar(self.root)

    def cadastro2(self):
      div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
      div.place(x=500, y=143)
      
      Intercorrencia().imagem("imagens/lar_esperanca.png", self.frame, 481, 200, 477, 82)

      Intercorrencia().texto(self.frame, "Usuário", util.FontsUI.simples_negrito, 502, 378)
      Intercorrencia().entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 499, 408)

      Intercorrencia().texto(self.frame, "Senha", util.FontsUI.simples_negrito, 500, 457)
      Intercorrencia().entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 499, 487)

      Intercorrencia().texto(self.frame, "Confirmar senha", util.FontsUI.simples_negrito, 500, 536)
      Intercorrencia().entry(self.frame, 440, 42, "#8ED6D0", 0, "black", util.FontsUI.simples, 499, 566)

      Intercorrencia().botao(self.frame, "Finalizar", util.FontsUI.simples, 162, 53, "#19AAA5", "White", None, 635, 645)

      div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
      div.place(x=487, y=750)

      Intercorrencia().imagem("imagens/curva_rodape.png", self.frame, 0, 750, 1618, 185)
      self.root.mainloop()

  Cadastro2().cadastro2()