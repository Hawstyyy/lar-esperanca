#from telalogin import TelaLogin
from cadastro import cadastro
from hotbar import Hotbar
import customtkinter as ctk

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Teste")
    root.resizable(False, False)


    tela = cadastro(root)
    hotbar = Hotbar(tela)
    #hotbar.user_forget()

    root.mainloop()
