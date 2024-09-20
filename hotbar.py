import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

# TELA --------------------------------------------------------

janela = ctk.CTk()
janela.after(0, janela.state('zoomed'))
janela.configure(fg_color='#F0F8FF')
janela.title("Login")
janela.resizable(False, False)

def imagem(path, largura, altura):
    img = Image.open(path).convert("RGBA")
    return ctk.CTkImage(
        light_image=img,
        dark_image=img,
        size=(largura, altura)
    )

hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0')
hotbar_frame.place(relx=.5, rely=.045, anchor="center")

logo_label = ctk.CTkLabel(hotbar_frame, text='', image=imagem('imagens/logo.png', 98, 98))
logo_label.place(relx=.5, rely=.5, anchor='center')


janela.mainloop()
