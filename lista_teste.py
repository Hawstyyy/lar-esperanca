import customtkinter as ctk
from util import Utils as U

janela = ctk.CTk()
janela.state('zoomed')
janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
janela.configure(fg_color='#FAFEFC')
janela.title("Lista")
janela.resizable(False, False)

# Só pra ter noção de espaço
hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
hotbar_frame.place(relx=.5, rely=.045, anchor="center")
back_icon = ctk.CTkLabel(janela, text='', image=U.imagemCTK('imagens/hotbar/back_icon.png', 40, 40))
back_icon.place(relx=.02, rely=.12, anchor='center')

dic_teste = {
    'Paciente 1': ['33º', '72', '120/80', '98%'],
    'Paciente 2': ['34º', '68', '115/75', '96%'],
    'Paciente 3': ['32º', '75', '118/78', '99%'],
    'Paciente 4': ['33º', '70', '122/80', '97%'],
    'Paciente 5': ['34º', '65', '110/70', '95%'],
    'Paciente 6': ['33º', '80', '125/82', '100%'],
    'Paciente 7': ['35º', '74', '119/77', '97%'],
    'Paciente 8': ['33º', '78', '117/79', '98%'],
    'Paciente 9': ['32º', '69', '116/76', '96%'],
    'Paciente 10': ['34º', '73', '121/81', '97%'],
    'Paciente 11': ['33º', '67', '113/72', '95%']
}

headers = ["Paciente", "Temperatura", "Cardíaca", "Arterial", "Saturação", "Status"]

search_frm = ctk.CTkFrame(janela, width=200, height=70)
search_frm.place(relx=.05, rely=0.25)

tt_lbl = ctk.CTkLabel(janela, text='Registros', font=(U.f_titulo), text_color='#1C3942')
tt_lbl.place(relx=.5, rely=0.18, anchor='center')

# Frame principal
reg_frm = ctk.CTkFrame(janela, width=1450, height=660, fg_color='black', corner_radius=10)
reg_frm.place(relx=.2, rely=.23)

# Configuração do grid para o cabeçalho
reg_frm.grid_rowconfigure(0, weight=0)  
reg_frm.grid_rowconfigure(1, weight=0) 
reg_frm.grid_rowconfigure(2, weight=0)  
for col in range(len(headers)):
    reg_frm.grid_columnconfigure(col, weight=1)

header_frm = ctk.CTkFrame(reg_frm, fg_color='blue')
header_frm.grid(columnspan=len(headers), row=0, sticky='new')

for col in range(len(headers)):
    header_frm.grid_columnconfigure(col, weight=1)

for col, header in enumerate(headers):
    header_label = ctk.CTkLabel(header_frm, text=header, font=U.f_titulo, text_color='#FFFFFF')
    header_label.grid(row=0, column=col, padx=(15, 15), pady=(10, 10), sticky='nsew')

def gerar_linhas_vazias(reg_frm, headers):
    for idx in range(10):
        linha_frame = ctk.CTkFrame(reg_frm, fg_color='green' if idx % 2 == 0 else 'pink', height=55)
        linha_frame.grid(row=idx + 1, columnspan=len(headers), sticky='nsew')

        for col in range(len(headers)):
            linha_frame.grid_columnconfigure(col, weight=1)

gerar_linhas_vazias(reg_frm, headers)

reg_frm.pack_propagate(False)
reg_frm.grid_propagate(False)

janela.mainloop()
