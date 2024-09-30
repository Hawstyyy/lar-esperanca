from typing import Tuple
import customtkinter as ctk
from customtkinter import CTkFrame
from util import FontsUI as F
from db_handler import DB

class SearchBar(CTkFrame):
    """Uma SearchBar que permite selecionar um valor da lista. Selecionar um valor aplica o valor ao Entry e remover a lista da tela"""
    def __init__(self, master: CTkFrame, primary: str, table: str, column: str, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Tuple[str, str] = "transparent", fg_color: str | Tuple[str, str] | None = None, border_color: str | Tuple[str, str] | None = None, background_corner_colors: Tuple[str | Tuple[str, str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self._WT = '#ffffff'
        self._BT = '#000000'
        self._COR = '#8ED6D0'
        self._values = {}
        self._primary = primary
        self._table = table
        self._column = column
        self._hover = '#BBF4F0'
        self._selected_id = None

        #Variaveis do entry
        self._entry_var = ctk.StringVar()
        self._entry_set_state = False
        self.set_callback_var()

        # Configure grid to make the entry expand
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

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

        #Configuração para permitir entry propagar para o tamanho do frame
        self._entry.grid(row=0, column=0, sticky='nsew')

        #Faz frame respeitar o tamanho dado no input
        self.grid_propagate(False)

### Métodos da Classe
    def set_callback_var(self):
        """Adiciona o callback na variavel presente no entry e salva o nome do callback. É necessário salvar o nome gerado por trace_add quando o callback é adicionado, para remoção  posterior..."""
        self._callback_name = self._entry_var.trace_add('write', self.entry_callback)

    def set_entry_text(self, id: str):
        """Adiciona o texto selecionado no entry e remove a lista de opções. Lida com a interação com o trace para evitar erros"""
        self._entry_var.trace_remove('write', self._callback_name)
        self._entry_set_state = True
        self._entry_var.set(self._values[id])
        self._selected_id = id
        self.destroy_list()
        self.set_callback_var()
        self.focus()

    def create_list_buttons(self):
        """Cria a lista de botões abaixo do entry"""
        #Deleta todos os itens da tela caso ja existam
        if(hasattr(self, '_list_butoes')):
            self.destroy_list()

        #Pega os valores do banco
        self.get_data(self._primary, self._table, self._column)

        #Configuração do grid
        self.configure(height=40*(len(self._values) + 1))
        self.columnconfigure(0,weight=1)
        rows = [i for i in range( len(self._values) + 1 ) ]
        self.rowconfigure(rows, weight=1)

        self._list_butoes:list[ctk.CTkButton] = []

        for idx, id in enumerate(self._values):

            self._list_butoes.append(

                ctk.CTkButton(self,
                    text=self._values[id],
                    corner_radius=0,
                    fg_color=self._COR,
                    bg_color=self._WT,
                    font=F.simples,
                    text_color='#ffffff',
                    border_width=0,
                    height=40,
                    anchor='w',
                    command=
                        lambda item = id: self.set_entry_text(item),
                    hover_color=self._hover
                )
            )

            self._list_butoes[idx].grid_propagate(False)
            self._list_butoes[idx].grid(row=idx + 1, column=0, sticky='nsew')

    def entry_callback(self, var, index, mode):
        """Callback do entry que cria os botões quando algo é digitado"""
        if(self._entry_set_state):
            self._entry_var.set('')
            self._entry_set_state = False
            self._entry.delete(0, 'end')

        # Cancela o after caso exista, pois um novo digito foi inserido no entry
        if hasattr(self, '_after_id'):
            self.after_cancel(self._after_id)

        #Agenda um novo after para execução após de 500ms
        self._after_id = self.after(500, self.create_list_buttons)

    def destroy_list(self):
        """Remove a lista de botões"""
        for item in self._list_butoes:
            item.destroy()
        self.configure(height=40)

    def get_data(self, primary: str, table: str, column: str):
        query = f"select {primary},{column} from {table} where {column} like %s"

        db = DB()
        #Pega as primeiras 10 linhas caso existam, que começam com o valor digitado
        like_value = f'{self._entry_var.get()}%'
        db.exec(query, (like_value,))
        print(like_value)

        #Remove anteriores
        self._values.clear()

        for linha in db.f_many(10):
            self._values[linha[0]] = linha[1]
        print(self._values)
        db.close()
        len_dic = len(self._values)
        print(f'len:{len_dic}')
        #Adiciona elementos com nome parecido até no maximo 10 elementos
        if(len_dic < 10 and len_dic != 0):
            print('second')
            db = DB()
            like_value = f'%{self._entry_var.get()}%'
            db.exec(query, (like_value,))
            print(like_value)

            for row in db.f_many(len_dic):
                print(f'linha: {row}')
                self._values[row[0]] = row[1]

            db.close()
        print(self._values)

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)

    frame = SearchBar(root, width=300, height=40, primary='id_paciente', table='paciente', column='nome_paciente')
    frame.place(relx=0.5,rely=0.5, anchor='n')
    root.mainloop()