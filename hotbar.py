import customtkinter as ctk
from util import Utils as U

class Hotbar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame):
        super().__init__(master)

        self.configure(height=98, fg_color='#8ED6D0', corner_radius=0)

        self.l_logo = ctk.CTkLabel(self, text='', image=U.imagemCTK('imagens/logo.png', 98, 98))
        self.l_logo.place(relx=.5, rely=.5, anchor='center')

        self.place(relx=0.5, rely=0, anchor='n', relwidth=1)

#-------------------------------TELA -------------------------
if __name__ == '__main__':
    janela = ctk.CTk()
    janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
    janela.state('zoomed')
    janela.configure(fg_color='#F0F8FF')
    janela.title("Login")
    janela.resizable(False, False)

    hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
    hotbar_frame.place(relx=.5, rely=.045, anchor="center")

    logo_label = ctk.CTkLabel(hotbar_frame, text='', image=U.imagemCTK('imagens/logo.png', 98, 98))
    logo_label.place(relx=.5, rely=.5, anchor='center')

    janela.mainloop()