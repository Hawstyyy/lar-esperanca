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

        validate_var = (self.register(self.validate_time_input), '%S', '%P', '%i')

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
            textvariable=self._var,
            validate="key",
            validatecommand=validate_var
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
    
    def _add_separator(self):
        self._var.set(self._var.get() + ':')
        self._entry.after(5, lambda: self._entry.icursor(self._entry.index('end'))) 
    
    def _in_between(self, ini: int, end: int):
        try:
            num = int(self._get_last())

            if(num >= ini and num <= end):
                return True
            return False
        except ValueError as e:
            print(f'Valor não é um número: {e}')

    def _is_pos_valide(self, pos: int) -> bool:
        try:
            return self._var.get()[pos].isdigit()
        except IndexError as e:
            print(f'Index inválido: {e}')

    def e_callback(self, var, index, mode):
        pass
        #if(len(self._var.get()) and not self._is_pos_valide(0)):


        # match(len(temp)):
        #     case 1:
        #         if(not self._is_valide()):
        #             self._remove_last()
        #             return
        #         elif(self._in_between(0 , 2)):
        #             return

        #         self._var.set('0' + temp)
        #         self._add_separator()

        #     case 2:
        #         if(not self._is_valide()):
        #             self._remove_last()
        #             return
        #         elif(temp[0] == '2' and not self._in_between(0, 3)):
        #             self._remove_last()
        #             return

        #         self._add_separator()

        #     case 3:
        #         if(not self._get_last() == ':'):
        #             self._remove_last()
        #             self._add_separator()
        #             return

        #     case 4:
        #         if(not self._is_valide()):
        #             self._remove_last()
        #             return
        #         elif(not self._in_between(0, 5)):
        #             self._remove_last()
        #             return
        #         return

        #     case 5:
        #         if(not self._is_valide()):
        #             self._remove_last()
        #             return
        #         return

        #     case _:
        #         self._remove_last()
        #         return

    def validate_time_input(self, char: str, current_text: str, cursor_position: int):
        print(char, current_text, cursor_position, sep=' - ')
        if len(current_text) > 5:
            return False

        # Permite apenas números e ':' na posição do index
        if cursor_position == 2 and char != ':':
            return False
        if cursor_position != 2 and not char.isdigit():
            return False

        # Valida as horas
        if len(current_text) >= 2:
            hour = current_text[:2]
            if hour.isdigit() and (int(hour) < 0 or int(hour) > 23):
                return False

        # Valida os minutos
        if len(current_text) == 5:
            minute = current_text[3:]
            if minute.isdigit() and (int(minute) < 0 or int(minute) > 59):
                return False

        return True

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)

    frame = HourEntry(root, width=300, height=40)
    frame.place(relx=0.5,rely=0.5, anchor='n')
    root.mainloop()