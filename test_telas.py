from telalogin import TelaLogin
from hotbar import Hotbar
import customtkinter as ctk

if __name__ == '__main__':
    root = ctk.CTk()
    root.geometry(f'{root.winfo_width()}x{root.winfo_height()}')
    root.state('zoomed')
    root.configure(fg_color='white')
    root.title("Teste")
    root.resizable(False, False)


    login = TelaLogin(root)
    hotbar = Hotbar(login, 'Jão')

    root.mainloop()
