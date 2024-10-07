import customtkinter as ctk
from util import basePath, FontsUI, imagemCTK
from PIL import Image
from hotbar import Hotbar

class Tela_principal:
  def __init__(self) -> None:
    self.root = ctk.CTk()
    self.set_geometry(self.root, 1440, 900)
    self.root.resizable(False, False)
    self.frame = ctk.CTkFrame(self.root, fg_color='white', corner_radius=0)
    self.frame.place(relwidth=1, relheight=1)
    self.f_hotbar = Hotbar(self.frame)

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

  def botao(self, master, text, f_texto, width, height, color, text_color, command, x, y, image='', compound='left'):
      botao = ctk.CTkButton(master, text=text, width=width, height=height, font=(f_texto), fg_color=color, text_color=text_color, command=command, compound=compound, image=image)
      botao.place(x=x, y=y)
      return botao

  def imagem(self, name, master, x, y, sizeX, sizeY):
    #imagem = ctk.CTkImage(Image.open(f"{basePath()}/{name}"), size=(sizeX, sizeY))
    imagem_place = ctk.CTkLabel(master, image=imagemCTK(name), text='')
    imagem_place.place(x=x, y=y)

  def entry(self, master, width, height, fg_color, border_width, text_color, f_font, x, y):
    entry = ctk.CTkEntry(master, width=width, height=height, fg_color=fg_color, border_width=border_width, text_color=text_color, font=(f_font))
    entry.place(x=x,y=y)

  def tela_principal(self):
    self.imagem("imagens/fotomulher.png", self.frame, 138, 100, 595, 673)

    self.texto(self.frame, 'Home', FontsUI.titulo, 955, 227)
    self.imagem("imagens/linha_torcida.png", self.frame, 830, 277, 342, 32)

    #coracao = ctk.CTkImage(Image.open(f"{basePath()}/imagens/coracao.png"), size=(70, 70))
    self.botao(self.frame, 'Pacientes', FontsUI.subtitulo, 214, 137, '#19AAA5', 'white', None, 773, 368, image=imagemCTK('imagens/coracao.png'), compound='top')

    #novareceita = ctk.CTkImage(Image.open(f"{basePath()}/imagens/novareceita.png"), size=(70, 70))
    self.botao(self.frame, 'Nova Receita', FontsUI.subtitulo, 214, 137, '#19AAA5', 'white', None, 1016, 368, image=imagemCTK('imagens/novareceita.png'), compound='top')
    
    #registros = ctk.CTkImage(Image.open(f"{basePath()}/imagens/registros.png"), size=(70, 70))
    self.botao(self.frame, 'Registros', FontsUI.subtitulo, 214, 137, '#19AAA5', 'white', None, 773, 530, image=imagemCTK('imagens/registros.png'), compound='top')

    #novoregistro = ctk.CTkImage(Image.open(f"{basePath()}/imagens/novoregistro.png"), size=(70, 70))
    self.botao(self.frame, 'Novo Registro', FontsUI.subtitulo, 214, 137, '#19AAA5', 'white', None, 1016, 530, image=imagemCTK('imagens/novoregistro.png'), compound='top')

    self.imagem("imagens\\curva_rodape.png", self.frame, 0, 750, 1618, 185)
    self.root.mainloop()

if __name__ == "__main__":
  Tela_principal().tela_principal()