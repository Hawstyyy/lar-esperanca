import customtkinter as ctk
from util import imagemCTK, FontsUI

class Hotbar(ctk.CTkFrame):
    """Cria um instância do frame Hotbar. A hotbar se coloca no topo do frame passado no primeiro argumento. É necessário dar bind no label l_exit para tela do login"""
    def __init__(self, master: ctk.CTkFrame, username = None):
        super().__init__(master)

        self.configure(height=98, fg_color='#8ED6D0', corner_radius=0)

        #Logo
        self.l_logo = ctk.CTkLabel(self, text='', image=imagemCTK('imagens/logo.png', 98, 98))
        self.l_logo.place(relx=.5, rely=.5, anchor='center')

        #Place User
        self.l_icon = ctk.CTkLabel(self, text='', image=imagemCTK('imagens/hotbar/user_icon.png', 29, 34))
        self.l_icon.place(relx=.145, rely=.5, anchor='e')

        self.l_username = ctk.CTkLabel(self, text=f'{username}', font=FontsUI.simples, text_color='#1C3942') #supondo que x já é a varíavel tratada com o nome do usuário retirado do banco
        self.l_username.place(relx=.15, rely=.5, anchor='w')

        #Label Exit
        self.l_exit = ctk.CTkLabel(self, text='', image=imagemCTK('imagens/hotbar/loggout.png', 34, 34))
        self.l_exit.place(relx=.87, rely=.5, anchor='center')
        self.l_exit.bind("<Button-1>", lambda event: print('>Aqui chama a tela de login<')) #Alterar para o comando correto

        #saindo da criação
        self.place(rely=0, relx=0.5, anchor="n", relwidth=1)
        #self.l_exit.unbind("<Button-1>") #não sei se ao alterar de páginas vai acumular funções bind, então melhor prevenir

        #Button Exit
        self.b_exit = ctk.CTkButton(self, text='', width=34, height=34, fg_color='transparent', hover_color='#8ED6D0',image=imagemCTK('imagens/hotbar/loggout.png', 34, 34), command=lambda: print('opppps'))
        self.b_exit.place(relx=.87, rely=.5, anchor='center')


    def user_forget(self):
        self.l_icon.place_forget()
        self.l_username.place_forget()
        self.l_exit.place_forget()

    def config_name(self, username:str):
        self.l_username.configure(text=username)

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
    logo_label = ctk.CTkLabel(hotbar_frame, text='', image=imagemCTK('imagens/logo.png', 98, 98))
    logo_label.place(relx=.5, rely=.5, anchor='center')

    b_exit = ctk.CTkButton(hotbar_frame, text='', width=34, height=34, fg_color='transparent', hover_color='#8ED6D0',image=imagemCTK('imagens/hotbar/loggout.png', 34, 34), command=lambda: print('opppps'))
    b_exit.place(relx=.87, rely=.5, anchor='center')


    user_icon = ctk.CTkLabel(hotbar_frame, text='', image=imagemCTK('imagens/hotbar/user_icon.png', 29, 34))
    user_icon.place(relx=.145, rely=.5, anchor='e')

    x = 'João Silva'

    user_name = ctk.CTkLabel(hotbar_frame, text=f'{x}', font=FontsUI.simples, text_color='#1C3942', anchor='w') #supondo que x já é a varíavel tratada com o nome do usuário retirado do banco
    user_name.place(relx=.15, rely=.5, anchor='w')

    def back_button():
        back_icon = ctk.CTkLabel(janela, text='', image=imagemCTK('imagens/hotbar/back_icon.png', 40, 40))
        back_icon.place(relx=.02, rely=.12, anchor='center')

        back_label = ctk.CTkLabel(janela, text='Voltar', font=FontsUI.subtitulo, text_color='#1C3942')
        back_label.place(relx=.055, rely=.117, anchor='center')

        back_icon.bind("<Button-1>", lambda event: print('>Aqui chama a tela anterior<')) #Alterar para o comando correto
        back_label.bind("<Button-1>", lambda event: print('>Aqui chama a tela anterior<'))

    back_button()

    janela.mainloop()