import os
import sys
import hashlib

class Utils:
    f_titulo = ('Segoe UI', 40)
    f_subtitulo = ('Segoe UI', 32)
    f_simples = ('Segoe UI', 24)

    def __init__(self) -> None:
        pass

    def basePath(self, file:str = None) -> str:
        """
        Retorna o caminho para a pasta atual em que o script se encontra. Util para adicionar caminho para imagens e outros.

        Args:
            file: Um arquivo ou pasta escifica. Podendo conter outro caminho.

        Returns:
            Uma string contendo o caminho como: 'C:\\users\\joaozinho\\py'.

        Examples:
            basePath()
                'C:\\users\\joaozinho\\py'
            basePath('imagem.png')
                'C:\\users\\joaozinho\\py\\imagem.png'
        """
        if(file):
            return os.path.dirname(os.path.abspath(sys.argv[0])) + f'\\{file}'
        return os.path.dirname(os.path.abspath(sys.argv[0]))

    def toSHA256(self, string: str) -> str:
        """
        Retorna a Hash da string de entrada, utilizando algoritmo SHA256

        Args:
            string: Uma string qualquer.

        Returns:
            Uma string contendo a Hash, como: '13ee3badae639da216c9eaa9b104047a1421a40b4e449ea78cc524631a6be75d'.
        """
        return hashlib.sha256(string.encode()).hexdigest()