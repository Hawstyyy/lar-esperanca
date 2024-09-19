import customtkinter as ctk
from customtkinter import CTkFrame
from tkinter import messagebox
from PIL import Image

FONT = ('Segoe', 40)

# TELA --------------------------------------------------------
class Receita(CTkFrame):
    def __init__(self, master: Image.Any, width: int = 200, height: int = 200, corner_radius: int | str | None = None, border_width: int | str | None = None, bg_color: str | Image.Tuple[str] = "transparent", fg_color: str | Image.Tuple[str] | None = None, border_color: str | Image.Tuple[str] | None = None, background_corner_colors: Image.Tuple[str | Image.Tuple[str]] | None = None, overwrite_preferred_drawing_method: str | None = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.place(relheigh=1, relwidth=1)

        self.p_holder = CTkFrame(self, width=440, height=600, fg_color='gray')
        self.p_holder.place(relx=0.5, rely=0.5, anchor='center')

        self.l_titulo = ctk.CTkLabel(self.p_holder, text='Nova Receita', fg_color='gray').place(relx=0.5, rely=0, anchor='n')



if __name__ == "__main__":
    root = ctk.CTk()
    root.after(0, root.state('zoomed'))
    root.configure(fg_color='white')
    root.title("Nova Receita")
    root.resizable(False, False)
    frame = Receita(root, fg_color='white')
    root.mainloop()