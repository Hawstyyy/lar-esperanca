from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from util import Utils as U
from db_handler import DB

class EntryDropdown(CTkFrame):
    """Um entry que quando editado abre um menu Dropdown com uma lista de valores. Selecionar um valor aplica o valor ao Entry e remove a lista da tela"""
    def __init__(self, master: CTkFrame, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, values:list[str] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.configure(fg_color='orange')
        self._WT = '#ffffff'
        self._BT = '#000000'
        self._COR = '#8ED6D0'
        self._values = values
        self._hover = '#BBF4F0'

        self.columnconfigure(0,weight=1)
        rows = [i for i in range( len(self._values) + 1 ) ]
        self.rowconfigure(rows, weight=1)

        self._entry_var = ctk.StringVar()
        def my_callback(var, index, mode):
            print(f"Traced variable: {self._entry_var.get()}")
            self.create_list_buttons()

        self._entry_var.trace_add('write', my_callback)

        self._entry = ctk.CTkEntry(
            self,
            corner_radius=5,
            fg_color=self._COR,
            text_color=self._WT,
            font=U.f_simples,
            border_width=0,
            textvariable=self._entry_var
        )
        self._entry.grid(row=0, column=0, sticky='nsew')

        self.create_list_buttons()

    def set_entry_text(self, value:str):
            self._entry_var.set(value)
            self.destroy_list()

    def create_list_buttons(self):
        #Deleta todos os itens da tela caso ja existam
        if(hasattr(self, '_list_butoes')):
            self.destroy_list()

        self._list_butoes:list[ctk.CTkButton] = []

        for idx, item in enumerate(self._values):
            self._list_butoes.append(
                ctk.CTkButton(self,
                    text=item,
                    corner_radius=5,
                    fg_color=self._COR,
                    font=U.f_simples,
                    text_color='#ffffff',
                    border_width=0,
                    command=
                        lambda item = item: self.set_entry_text(item),
                    hover_color=self._hover
                )
            )
            self._list_butoes[idx].grid(row=idx + 1, column=0, sticky='nsew')

    def destroy_list(self):
        for item in self._list_butoes:
            item.destroy()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)
    db = DB()
    db.exec('select nome_paciente from paciente')
    funcionarios = [nome[0] for nome in db.f_many(10)]
    print(funcionarios)
    frame = EntryDropdown(root, width=550,values=funcionarios)
    frame.place(relx=0.5,rely=0.5, anchor='n')
    root.mainloop()