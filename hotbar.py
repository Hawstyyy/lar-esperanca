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

class Hotbar(ctk.CTkFrame):
    def __init__(self, master: ctk.CTkFrame, width: int = 200, height: int = 98, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Image.Tuple[str] = "transparent", fg_color: str | Image.Tuple[str] | None = '#8ED6D0', border_color: str | Image.Tuple[str] | None = None, background_corner_colors: Image.Tuple[str | Image.Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

        self.l_logo = ctk.CTkLabel(self, text='', image=imagem('imagens/logo.png', 98, 98))
        self.l_logo.place(relx=.5, rely=.5, anchor='center')

        self.place(relx=0.5, rely=0, anchor='n', relwidth=1)

