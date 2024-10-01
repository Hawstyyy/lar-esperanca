#Ana :D

import customtkinter as ctk
from util import imagem, texto, frame, imagemCTK
from util import FontsUI as U
from PIL import Image
import pywinstyles
import db_handler as db

# db = db()

# FUNÇÕES ------------------------------------------------------
def tela_login(janela: ctk.CTkFrame | ctk.CTk):

    tela = ctk.CTkFrame(janela,fg_color='#FAFEFC')
    tela.place(relwidth=1, relheight=1)

    fotologin = imagemCTK("imagens/logintransp.png", 920, 920)
    curva = imagemCTK("imagens/curva_rodape.png", 1920, 150)
    linha = imagemCTK("imagens/lar_esperanca.png", 450, 80)

    def imagem_tela (janela, imagem, posicaox, posicaoy):

        image_label = ctk.CTkLabel(janela, image=imagem, text="")
        image_label.place(relx=posicaox, rely=posicaoy, anchor="center")
        pywinstyles.set_opacity(image_label, color="#FAFEFC")


    imagem_tela(tela, fotologin, 0.3, 0.49)
    imagem_tela(tela, curva, 0.5, 0.93)
    imagem_tela(tela, linha, 0.74, 0.28)

    def quadrados(cor, bg, width, height, posicaox, posicaoy):

        ctk.CTkFrame(
        tela, 
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
            tela, 
            text=texto,
            font=fonte_com_estilo,
            text_color=cor_texto,
            fg_color=fundo_texto
        ).place(relx=posicaox, rely=posicaoy, anchor="center")

    textos("Entrar", U.simples, "normal", "#97BCAA", "transparent", 0.74, 0.35)
    textos("Bem Vindo de Volta!", U.simples, "underline", "#2D5E6C", "transparent", 0.74, 0.398)
    textos("Usuário:", U.simples, "normal", "#2D5E6C", "transparent", 0.665, 0.46)
    textos("Senha:", U.simples, "normal", "#2D5E6C", "transparent", 0.663, 0.545)


    user_entry = ctk.CTkEntry(
        tela, 
        width= 380, 
        height= 40,
        border_color = "#8ED6D0",
        fg_color = "#8ED6D0",
        bg_color='#FAFEFC',
        text_color= "black"
    )
    user_entry.place(relx= 0.74, rely= 0.5, anchor="center")

    senha_entry = ctk.CTkEntry(
        tela, 
        width= 380, 
        height= 40,
        border_color = "#8ED6D0",
        fg_color = "#8ED6D0",
        bg_color='#FAFEFC',
        text_color= "black",
        show = "*"
    )
    senha_entry.place(relx= 0.74, rely= 0.585, anchor="center")

    logar = ctk.CTkButton(
        tela,
        text="Logar",
        font=(U.simples),
        width=120, 
        height=50,
        text_color="White",
        fg_color="#19AAA5",
        hover_color="#3bd9d3",
        bg_color = '#FAFEFC'
    )
    logar.place(relx=0.74, rely=0.66, anchor="center")

    clique_aqui = ctk.CTkButton(
        tela,
        text= "Clique aqui!",
        font=(U.simples_underline),
        width=50, 
        height=30,
        text_color="#97BCAA",
        fg_color="#FAFEFC",
        hover_color="#FAFEFC",
        bg_color = '#FAFEFC'
    )
    clique_aqui.place(relx=0.74, rely=0.75, anchor="center")
    textos("Não tem cadastro?", U.simples, "normal", "#97BCAA", "transparent", 0.74, 0.72)

    # # Só pra ter noção de espaço -----------------------------------------
    # hotbar_frame = ctk.CTkFrame(tela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
    # hotbar_frame.place(relx=.5, rely=.045, anchor="center")
    # # back_icon = ctk.CTkLabel(janela, text='', image=imagemCTK('imagens/hotbar/back_icon.png', 40, 40))
    # # back_icon.place(relx=.02, rely=.12, anchor='center')

    return tela

if __name__ == '__main__':
    janela = ctk.CTk()
    janela.state('zoomed')
    janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
    janela.configure(fg_color='#FAFEFC')
    janela.title("Login")
    janela.resizable(False, False)
    tela_login(janela)
    janela.mainloop()