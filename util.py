import os
import sys
import hashlib
from PIL import Image
import customtkinter as ctk
import pywinstyles

class FontsUI:
    titulo = ('Segoe UI', 40)
    titulo_negrito = ('Segoe UI', 40, 'bold')
    titulo_italico = ('Segoe UI', 40, 'italic')
    titulo_underline = ('Segoe UI', 40, 'underline')
    subtitulo = ('Segoe UI', 32)
    subtitulo_negrito = ('Segoe UI', 32, 'bold')
    subtitulo_italico = ('Segoe UI', 32, 'italic')
    subtitulo_underline = ('Segoe UI', 32, 'underline')
    simples = ('Segoe UI', 24)
    simples_negrito = ('Segoe UI', 24, 'bold')
    simples_italico = ('Segoe UI', 24, 'italic')
    simples_underline = ('Segoe UI', 24, 'underline')

def basePath(file:str = None) -> str:
    """
    Retorna o caminho para a pasta atual em que o script se encontra. Util para adicionar caminho para imagens e outros.

    Args:
        file: Um arquivo ou pasta específica, podendo conter outro caminho.

    Returns:
        Uma string contendo o caminho como: 'C:\\users\\joaozinho\\py'.

    Examples:
        basePath()\n
        ->\t'C:\\users\\joaozinho\\py'\n
        basePath('imagem.png')\n
        ->\t'C:\\users\\joaozinho\\py\\imagem.png'
    """
    if(file):
        return os.path.dirname(os.path.abspath(sys.argv[0])) + f'\\{file}'
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def toHash(string: str) -> str:
    """
    Retorna a Hash da string de entrada, utilizando algoritmo SHA256

    Args:
        string: Uma string qualquer.

    Returns:
        Uma string contendo a Hash, como: '13ee3badae639da216c9eaa9b104047a1421a40b4e449ea78cc524631a6be75d'.
    """
    return hashlib.sha256(string.encode()).hexdigest()

def imagemCTK(path: str, largura: int = 200, altura: int = 200):
    """Retorna uma instância de CTkImage"""
    img = Image.open(basePath(path)).convert("RGBA")
    return ctk.CTkImage(
        light_image=img,
        dark_image=img,
        size=(largura, altura)
    )

def imagem(janela: ctk.CTkFrame, imagem: ctk.CTkImage, posx: float | int, posy: float | int, anchor: str = 'center', absolute_pos: bool = False) -> ctk.CTkLabel:
    """Adiciona uma imagem a tela, sendo esta um Label com fundo trasnparente. O argumento absolute_pos muda o place para posição absoluta"""
    image_label = ctk.CTkLabel(janela, image=imagem, text="", bg_color='#ffffff')
    pywinstyles.set_opacity(image_label, color='#ffffff')

    if(absolute_pos):
        image_label.place(x=posx, y=posy, anchor=anchor)
        return image_label

    image_label.place(relx=posx, rely=posy, anchor=anchor)
    return image_label

def texto(janela: ctk.CTkFrame, texto: str, fonte: FontsUI, cor_texto: str, fundo_texto: str, posx: float | int, posy: float | int, anchor: str = "center",
          absolute_pos: bool = False) -> ctk.CTkLabel:
    """Adiciona um texto a tela. O argumento absolute_pos muda o place para posição absoluta"""

    label = ctk.CTkLabel(
        janela, 
        text=texto,
        font=fonte,
        text_color=cor_texto,
        bg_color='#ffffff',
        fg_color=fundo_texto
    )
    pywinstyles.set_opacity(label, color='#ffffff')

    if(absolute_pos):
        label.place(x=posx, y=posy, anchor=anchor)
        return label

    label.place(relx=posx, rely=posy, anchor=anchor)
    return label

def frame(janela: ctk.CTkFrame, cor: str, width: int = 200, height: int = 200, posx: float | int = 0.5, posy: float | int = 0.5,
              anchor: str = "center", absolute_pos: bool = False) -> ctk.CTkFrame:
    """Adiciona um frame a tela. O argumento absolute_pos muda o place para posição absoluta"""

    frame = ctk.CTkFrame(
        janela, 
        width= width, 
        height= height,
        fg_color = cor,
        bg_color= '#ffffff'
    )
    pywinstyles.set_opacity(frame, color='#ffffff')

    if(absolute_pos):
        frame.place(x=posx, y=posy, anchor=anchor)
        return frame

    frame.place(relx=posx, rely=posy, anchor=anchor)
    return frame