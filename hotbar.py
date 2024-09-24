import customtkinter as ctk
from util import Utils as U

class Hotbar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame):
        super().__init__(master)

        self.configure(height=98, fg_color='#8ED6D0', corner_radius=0)

        self.l_logo = ctk.CTkLabel(self, text='', image=U.imagemCTK('imagens/logo.png', 98, 98))
        self.l_logo.place(relx=.5, rely=.5, anchor='center')

        self.place(relx=0.5, rely=0, anchor='n', relwidth=1)
        exit_label.unbind("<Button-1>") #não sei se ao alterar de páginas vai acumular funções bind, então melhor prevenir

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

    exit_label = ctk.CTkLabel(hotbar_frame, text='', image=U.imagemCTK('imagens/hotbar/loggout.png', 34, 34))
    exit_label.place(relx=.87, rely=.5, anchor='center')
    exit_label.bind("<Button-1>", lambda event: print('>Aqui chama a tela de login<')) #Alterar para o comando correto

    user_icon = ctk.CTkLabel(hotbar_frame, text='', image=U.imagemCTK('imagens/hotbar/user_icon.png', 29, 34))
    user_icon.place(relx=.1, rely=.5, anchor='center')

    x = 'Funcionário 1'

    user_name = ctk.CTkLabel(hotbar_frame, text=f'{x}', font=U.f_simples, text_color='#1C3942') #supondo que x já é a varíavel tratada com o nome do usuário retirado do banco
    user_name.place(relx=.15, rely=.5, anchor='center')

    def back_button():
        back_icon = ctk.CTkLabel(janela, text='', image=U.imagemCTK('imagens/hotbar/back_icon.png', 40, 40))
        back_icon.place(relx=.02, rely=.12, anchor='center')

        back_label = ctk.CTkLabel(janela, text='Voltar', font=U.f_subtitulo, text_color='#1C3942')
        back_label.place(relx=.055, rely=.117, anchor='center')

        back_icon.bind("<Button-1>", lambda event: print('>Aqui chama a tela anterior<')) #Alterar para o comando correto
        back_label.bind("<Button-1>", lambda event: print('>Aqui chama a tela anterior<'))

    back_button()

    janela.mainloop()