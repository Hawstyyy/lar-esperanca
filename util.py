import os
import sys
import hashlib
from PIL import Image
import customtkinter as ctk

class Utils:
    f_titulo = ('Segoe UI', 40)
    f_subtitulo = ('Segoe UI', 32)
    f_simples = ('Segoe UI', 24)

    def __init__(self) -> None:
        pass

    @staticmethod
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

    @staticmethod
    def toHash(string: str) -> str:
        """
        Retorna a Hash da string de entrada, utilizando algoritmo SHA256

        Args:
            string: Uma string qualquer.

        Returns:
            Uma string contendo a Hash, como: '13ee3badae639da216c9eaa9b104047a1421a40b4e449ea78cc524631a6be75d'.
        """
        return hashlib.sha256(string.encode()).hexdigest()

    @staticmethod
    def imagemCTK(path: str, largura: int, altura: int):
        """Retorna uma instância de CTkImage"""
        img = Image.open(Utils.basePath(path)).convert("RGBA")
        return ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(largura, altura)
        )
