from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from tkinter import messagebox
from util import FontsUI as F

class HourEntry(CTkFrame):
    """Uma SearchBar que permite selecionar um valor da lista. Selecionar um valor aplica o valor ao Entry e remover a lista da tela"""
    def __init__(self, master: CTkFrame, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self._WT = '#ffffff'
        self._BT = '#000000'
        self._COR = '#8ED6D0'
        self._height = height
        self._hover = '#BBF4F0'

        #Variaveis do entry
        self._var = ctk.StringVar()
        self.set_callback_var()

        # Configure grid to make the entry expand
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #Criação do entry incial
        self._entry = ctk.CTkEntry(
            self,
            corner_radius=5,
            fg_color=self._COR,
            text_color=self._BT,
            bg_color=self._WT,
            font=F.simples,
            border_width=0,
            height=self._height,
            width=self.winfo_reqwidth(),
            textvariable=self._var
        )

        #Configuração para permitir entry propagar para o tamanho do frame
        self._entry.grid(row=0, column=0, sticky='nsew')

        #Faz frame respeitar o tamanho dado no input
        self.grid_propagate(False)

### Métodos da Classe
    def set_callback_var(self):
        """Adiciona o callback na variavel presente no entry e salva o nome do callback. É necessário salvar o nome gerado por trace_add quando o callback é adicionado, para remoção  posterior..."""
        self._callback_name = self._var.trace_add('write', self.e_callback)
    

    def _remove_last(self):
        self._var.set(self._var.get()[:-1])
        
    def _get_last(self):
        return self._var.get()[-1]

    def e_callback(self):
        temp = self._var.get()

        
        

        match(len(temp)):
            case 1:
                if(not self._get_last().isdigit() and self._get_last() not in (0,1,2)):
                    self._remove_last()
                    return
