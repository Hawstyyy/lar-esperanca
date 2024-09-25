#Ana :D

import customtkinter as ctk
from util import Utils as U
from PIL import Image
import pywinstyles

janela = ctk.CTk()
janela.state('zoomed')
janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
janela.configure(fg_color='#FAFEFC')
janela.title("Lista")
janela.resizable(False, False)

# IMAGENS ----------------------------------------------
fotologin = ctk.CTkImage(
light_image=Image.open("imagens/logintransp.png"),
dark_image=Image.open("imagens/logintransp.png"),
size=(920, 920)
)

curva = ctk.CTkImage(
light_image=Image.open("curva.png"),
dark_image=Image.open("curva.png"),
size=(2000, 200)
)

linha = ctk.CTkImage(
light_image=Image.open("texto.png"),
dark_image=Image.open("texto.png"),
size=(450, 80)
)

# FUNÇÕES ------------------------------------------------------
def imagem_tela (janela, imagem, posicaox, posicaoy):

    image_label = ctk.CTkLabel(janela, image=imagem, text="")
    image_label.place(relx=posicaox, rely=posicaoy, anchor="center")
    pywinstyles.set_opacity(image_label, color="#FAFEFC")


imagem_tela(janela, fotologin, 0.3, 0.49)
imagem_tela(janela, curva, 0.5, 0.91)
imagem_tela(janela, linha, 0.74, 0.28)

def quadrados(cor, bg, width, height, posicaox, posicaoy):
    
    ctk.CTkFrame(
    janela, 
    width= width, 
    height= height,
    fg_color = cor,
    bg_color= bg

    ).place(relx=posicaox, rely=posicaoy, anchor="center")

linha1 = quadrados("#171717", '#2D5E6C', 550, 3, 0.74, 0.18)
linha2 = quadrados("#171717", '#2D5E6C', 550, 3, 0.74, 0.8)

def textos(texto, fonte, estilo, cor_texto, fundo_texto, posicaox, posicaoy):

    nome_fonte, tamanho_fonte = fonte

    if estilo == "bold":
        fonte_com_estilo = (nome_fonte, tamanho_fonte, "bold")
    elif estilo == "italic":
        fonte_com_estilo = (nome_fonte, tamanho_fonte, "italic")
    elif estilo == "underline":
        fonte_com_estilo = (nome_fonte, tamanho_fonte, "underline")
    else:
        fonte_com_estilo = (nome_fonte, tamanho_fonte, "normal")

    ctk.CTkLabel(
        janela, 
        text=texto,
        font=fonte_com_estilo,
        text_color=cor_texto,
        fg_color=fundo_texto
    ).place(relx=posicaox, rely=posicaoy, anchor="center")

textos("Entrar", U.f_simples, "normal", "#97BCAA", "transparent", 0.74, 0.35)
textos("Bem Vindo de Volta!", U.f_simples, "underline", "#2D5E6C", "transparent", 0.74, 0.39)
textos("Usuário:", U.f_simples, "normal", "#2D5E6C", "transparent", 0.665, 0.46)
textos("Senha:", U.f_simples, "normal", "#2D5E6C", "transparent", 0.663, 0.545)

user_entry = ctk.CTkEntry(
    janela, 
    width= 380, 
    height= 40,
    border_color = "#8ED6D0",
    fg_color = "#8ED6D0",
    bg_color='#FAFEFC'
)
user_entry.place(relx= 0.74, rely= 0.5, anchor="center")

senha_entry = ctk.CTkEntry(
    janela, 
    width= 380, 
    height= 40,
    border_color = "#8ED6D0",
    fg_color = "#8ED6D0",
    bg_color='#FAFEFC',
    show = "*"
)
senha_entry.place(relx= 0.74, rely= 0.585, anchor="center")

# Só pra ter noção de espaço -----------------------------------------
hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
hotbar_frame.place(relx=.5, rely=.045, anchor="center")
back_icon = ctk.CTkLabel(janela, text='', image=U.imagemCTK('imagens/hotbar/back_icon.png', 40, 40))
back_icon.place(relx=.02, rely=.12, anchor='center')

janela.mainloop()

