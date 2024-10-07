#from telalogin import TelaLogin
from cadastro import cadastro
from hotbar import Hotbar
import customtkinter as ctk
from listadb import lista_padrao

from telalogin import tela_login

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Teste")
    root.resizable(False, False)


    hotbar = Hotbar(root)
    hotbar.user_forget()
    tela = tela_login(root, lambda var: lista_padrao(root, var), hotbar)
    hotbar.tkraise()

    root.mainloop()
