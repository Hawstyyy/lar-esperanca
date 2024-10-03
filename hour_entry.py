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

        validate_entry_hour = (self.register(self.validate_hour), '%S', '%P', '%i')
        validate_entry_minute = (self.register(self.validate_minute), '%S', '%P', '%i')

        #Variaveis do entry
        #self._var = ctk.StringVar()

        # Configure grid to make the entry expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=10)

        #Entry Hour
        self._entry_hour = ctk.CTkEntry(
            self,
            corner_radius=5,
            fg_color=self._COR,
            text_color=self._BT,
            bg_color=self._WT,
            font=F.simples,
            border_width=0,
            height=self._height,
            width=self.winfo_reqwidth(),
            validate="key",
            validatecommand=validate_entry_hour
        )
        #Configuração para permitir entry propagar para o tamanho do frame
        self._entry_hour.grid(row=0, column=0, sticky='nsew')

        #Label :
        self._label = ctk.CTkLabel(self, width=15, height=self._height, text=':', fg_color='white', bg_color=self._WT, font=F.simples, text_color=self._BT)
        self._label.grid(row=0, column=1)

        #Entry Minute
        self._entry_minute = ctk.CTkEntry(
            self,
            corner_radius=5,
            fg_color=self._COR,
            text_color=self._BT,
            bg_color=self._WT,
            font=F.simples,
            border_width=0,
            height=self._height,
            width=self.winfo_reqwidth(),
            validate="key",
            validatecommand=validate_entry_minute
        )
        #Configuração para permitir entry propagar para o tamanho do frame
        self._entry_minute.grid(row=0, column=2, sticky='nsew')

        #Faz frame respeitar o tamanho dado no input
        self.grid_propagate(False)

###Métodos da Classe
    def get_time(self) -> tuple[int]:
        if(len(self._entry_hour.get()) != 0 and len(self._entry_minute.get()) != 0):
            return (int(self._entry_hour.get()), int(self._entry_minute.get()))

    def validate_hour(self, char: str, current_text: str, cursor_position: int):
        if len(current_text) > 2:
            return False
        if current_text == '':
            return True
        if not current_text.isdigit():
            return False
        if int(current_text) < 0 or int(current_text) > 23:
            return False

        if(len(current_text) == 2):
            self._entry_minute.focus()
        return True
    
    def validate_minute(self, char: str, current_text: str, cursor_position: int):
        if len(current_text) > 2:
            return False
        if current_text == '':
            return True
        if not current_text.isdigit():
            return False
        if int(current_text) < 0 or int(current_text) > 59:
            return False
        return True

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)

    frame = HourEntry(root, width=100, height=40)
    frame.place(relx=0.5,rely=0.5, anchor='n')
    root.mainloop()