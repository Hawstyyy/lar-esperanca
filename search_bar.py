from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from util import FontsUI as F
from db_handler import DB

class SearchBar(CTkFrame):
    """Uma SearchBar que permite selecionar um valor da lista. Selecionar um valor aplica o valor ao Entry e remover a lista da tela"""
    def __init__(self, master: CTkFrame, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, values:list[str] = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self._WT = '#ffffff'
        self._BT = '#000000'
        self._COR = '#8ED6D0'
        self._values = values[:]
        self._hover = '#BBF4F0'

        #Faz frame respeitar o tamanho dado no input
        self.grid_propagate(False)
        self.update()

        #Variaveis do entry
        self._entry_var = ctk.StringVar()
        self._entry_set_state = False
        self.set_callback_var()

        #Criação do entry incial
        self._entry = ctk.CTkEntry(
            self,
            corner_radius=5,
            fg_color=self._COR,
            text_color=self._WT,
            bg_color=self._WT,
            font=F.simples,
            border_width=0,
            height=40,
            width=self.winfo_reqwidth(),
            textvariable=self._entry_var
        )
        self._entry.grid_propagate(False)
        self._entry.grid(row=0, column=0, sticky='nsew')

### Métodos da Classe
    def update_entry_size(self):
        self.update()
        self._entry.configure(width=self.winfo_reqwidth())

    def set_callback_var(self):
        """Adiciona o callback na variavel presente no entry e salva o nome do callback. É necessário salvar o nome gerado por trace_add quando o callback é adicionado, para remoção  posterior..."""
        self._callback_name = self._entry_var.trace_add('write', self.my_callback)

    def set_entry_text(self, value:str):
        """Adiciona o texto selecionado no entry e remove a lista de opções. Lida com a interação com o trace para evitar erros"""
        self._entry_var.trace_remove('write', self._callback_name)
        self._entry_set_state = True
        self._entry_var.set(value)
        self.destroy_list()
        self.set_callback_var()
        self.focus()

    def create_list_buttons(self):
        """Cria a lista de botões abaixo do entry"""
        #Deleta todos os itens da tela caso ja existam
        if(hasattr(self, '_list_butoes')):
            self.destroy_list()

        #Configuração do grid
        self.configure(height=40*(len(self._values) + 1))
        self.columnconfigure(0,weight=1)
        rows = [i for i in range( len(self._values) + 1 ) ]
        self.rowconfigure(rows, weight=1)

        self._list_butoes:list[ctk.CTkButton] = []

        for idx, item in enumerate(self._values):
            self._list_butoes.append(
                ctk.CTkButton(self,
                    text=item,
                    corner_radius=0,
                    fg_color=self._COR,
                    bg_color=self._WT,
                    font=F.simples,
                    text_color='#ffffff',
                    border_width=0,
                    height=40,
                    anchor='w',
                    command=
                        lambda item = item: self.set_entry_text(item),
                    hover_color=self._hover
                )
            )
            self._list_butoes[idx].grid_propagate(False)
            self._list_butoes[idx].grid(row=idx + 1, column=0, sticky='nsew')

    def my_callback(self, var, index, mode):
        """Callback do entry que cria os botões quando algo é digitado"""
        if(self._entry_set_state):
            self._entry_var.set('')
            self._entry_set_state = False
            self._entry.delete(0, 'end')
        self.create_list_buttons()

    def destroy_list(self):
        """Remove a lista de botões"""
        for item in self._list_butoes:
            item.destroy()
        self.configure(height=40)

    def change_list(self, new: list[str]):
        """Altera a lista de opções"""
        self._values = new[:]

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

    frame = SearchBar(root, width=300, height=40, values=funcionarios)
    frame.place(relx=0.5,rely=0.5, anchor='n')
    root.mainloop()