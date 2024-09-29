import customtkinter as ctk
from PIL import Image
from util import frame, texto, imagem, imagemCTK
from util import FontsUI as U
import os, sys
from hotbar import Hotbar

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
    hotbar = Hotbar(frame)

    div = ctk.CTkFrame(self.root, fg_color='#2D5E6C', width=440, height=2, corner_radius=0)
    div.place(relx=0.5, rely=0.15, anchor="center")

    texto = ctk.CTkImage(Image.open(f"{self.basePath()}/imagens/lar_esperanca.png"), size=(487,80))
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

    curva = ctk.CTkImage(Image.open(f"{self.basePath()}/imagens/curva_rodape.png"),size=(1618, 185))
    curva_place = ctk.CTkLabel(frame, image=curva, text='')
    curva_place.place(rely=0.9, relx=0.5, anchor="center")

    botao_prosseguir = ctk.CTkButton(frame, text="Prosseguir", width=162, height=63, corner_radius=5, fg_color="#19AAA5", font=("Segoe UI", 28), text_color="white")
    botao_prosseguir.place(rely=0.773, relx=0.5, anchor="center")

    self.root.mainloop()

if __name__ == "__main__":
  Cadastro().cadastro()


def cadastro( master: ctk.CTkFrame | ctk.CTk) -> ctk.CTkFrame:
  """Cria a tela de cadastro e retorna o frame criado"""
  tela = ctk.CTkFrame(master, fg_color='#FFFFFF', corner_radius=0)

  tx_color = '#000000'
  back_color = '#ffffff'
  fill_color = "#8ED6D0"

  tela.place(relwidth=1, relheight=1)
  hotbar = Hotbar(tela)

  f_holder = frame(tela, back_color, 440, 350, 0.5, 0.5)

  imagem(tela, imagemCTK('imagens/lar_esperanca.png', 487, 80), 0.5, 0.25,)
  imagem(tela, imagemCTK('imagens/curva_rodape.png', 1920, 150), 0.5, 1, 's')

  #Nome
  texto(f_holder, 'Nome completo', U.simples, tx_color, back_color, 0, 0.09, 'sw')
  e_nome = ctk.CTkEntry(f_holder, width=440, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_nome.place(relx=0.5, rely=0.09, anchor="n")

  #Cpf
  texto(f_holder, 'CPF', U.simples, tx_color, back_color, 0, 0.35, 'sw' )
  e_cpf = ctk.CTkEntry(f_holder, width=210, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_cpf.place(relx=0, rely=0.35, anchor="nw")

  #Rg
  l_rg = texto(f_holder, 'RG', U.simples, tx_color, back_color, 1, 0.35, 'se' )
  l_rg.configure(anchor='w', width=210, justify='left')
  e_rg = ctk.CTkEntry(f_holder, width=210, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_rg.place(relx=1, rely=0.35, anchor="ne")

  #Endereço
  texto(f_holder, 'Endereço', U.simples, tx_color, back_color, 0, 0.6, 'sw' )
  e_endereco = ctk.CTkEntry(f_holder, width=440, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_endereco.place(relx=0, rely=0.6, anchor="nw")

  #Data nascimento
  texto(f_holder, 'Data de nascimento', U.simples, tx_color, back_color, 0, 0.85, 'sw' )
  e_dia = ctk.CTkEntry(f_holder, width=60, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_dia.place(relx=0, rely=0.85, anchor="nw")

  e_mes = ctk.CTkEntry(f_holder, width=60, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_mes.place(relx=0.2, rely=0.85, anchor="nw")

  e_ano = ctk.CTkEntry(f_holder, width=60, height=40, fg_color=fill_color, border_width=0, text_color=tx_color, font=U.simples)
  e_ano.place(relx=0.40, rely=0.85, anchor="nw")

  #Linha Superior
  ctk.CTkFrame(tela, fg_color='#2D5E6C', width=440, height=2, corner_radius=0).place(relx=0.5, rely=0.15, anchor="center")
  #Linha Inferior
  ctk.CTkFrame(tela, fg_color='#2D5E6C', width=440, height=2, corner_radius=0).place(relx=0.5, rely=0.83, anchor="center")
  
  def validar_cadastro(nome: ctk.CTkEntry, cpf: ctk.CTkEntry, rg: ctk.CTkEntry, endereco: ctk.CTkEntry, dia: ctk.CTkEntry, mes: ctk.CTkEntry, ano: ctk.CTkEntry):
    """TODO: Fazer função a para validar os valores recebidos"""
    print(f'Validado cadastro:\nNome: {nome.get()}\nCpf: {cpf.get()}\nRg: {rg.get()}\nEndereço: {endereco.get()}\nData Nascimento: {dia.get()}/{mes.get()}/{ano.get()}\nSeguindo para prox. pagina!')

  b_prosseguir = ctk.CTkButton(tela, text="Prosseguir", width=162, height=53, corner_radius=5, fg_color="#19AAA5", font=U.simples, text_color="white", command=lambda:validar_cadastro(e_nome,e_cpf, e_rg, e_endereco, e_dia, e_mes, e_ano))
  b_prosseguir.place(relx=0.5, rely=0.7, anchor="n")

  return tela