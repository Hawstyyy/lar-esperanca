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

search_frm = ctk.CTkFrame(janela, width=200, height=70)
search_frm.place(relx=.05, rely= 0.25) # Isso provávelmente ta torto mas não é que vou fazer então lero lero lero

tt_lbl = ctk.CTkLabel(janela, text='Registros', font=(U.f_titulo), text_color='#1C3942')
tt_lbl.place(relx=.5, rely=0.18, anchor='center')

reg_frm = ctk.CTkFrame(janela, width=1450, height=660, fg_color='#FAFEFC', corner_radius=10)
reg_frm.place(relx=.2, rely=.23)

# Eu me arrependo profundamente de não ter usado pack ou grid desde o inicio

reg_frm.columnconfigure(0, weight=1)
reg_frm.columnconfigure(4,  weight=1)
reg_frm.pack_propagate(False)
reg_frm.grid_propagate(False)

def inserir_registros_com_grid(frame, dic_pacientes):
    # Cabeçalho
    headers = ["Paciente", "Temperatura", "Cardíaca", "Arterial", "Saturação"]
    
    # Frame de fundo para o cabeçalho
    header_bg_frame = ctk.CTkFrame(frame, fg_color='#48818D', corner_radius=10)
    header_bg_frame.grid(row=0, column=0, columnspan=len(headers), padx=10, pady=(20, 10), sticky='ew')
    
    # Os títulos de cada info da tabela
    for col, header in enumerate(headers):
        header_label = ctk.CTkLabel(header_bg_frame, text=header, font=U.f_titulo, text_color='#FFFFFF')
        header_label.grid(row=0, column=col, padx=20, pady=(10, 10), sticky='ew')

    # Isso é pra ajustar o bg do header
    for col in range(len(headers)):
        header_bg_frame.columnconfigure(col, weight=1)  # Para expansão de colunas

    # Distância vertical entre as linhas
    ypad = 10

    # Esse for é mt confuso 
    for i, (paciente, dados) in enumerate(dic_pacientes.items()):
        if i >= 10:  # 10 pacientes por tabela
            break

        # Frame que simula a linha
        linha_frame = ctk.CTkFrame(frame, fg_color='#DBF0EE' if i % 2 == 0 else '#FAFEFC', corner_radius=10)
        linha_frame.grid(row=i + 1, column=0, columnspan=len(headers), padx=10, pady=0, sticky='ew')

        for col in range(len(headers)):
            linha_frame.columnconfigure(col, weight=1)

        # Nome
        paciente_label = ctk.CTkLabel(linha_frame, text=paciente, font=U.f_simples, text_color='#1C3942')
        paciente_label.grid(row=0, column=0, padx=10, pady=ypad, sticky='ew')

        # Temperatura
        temp_label = ctk.CTkLabel(linha_frame, text=dados[0], font=U.f_simples, text_color='#1C3942')
        temp_label.grid(row=0, column=1, padx=10, pady=ypad, sticky='ew')

        # BPM
        bpm_label = ctk.CTkLabel(linha_frame, text=f"{dados[1]} BPM", font=U.f_simples, text_color='#1C3942')
        bpm_label.grid(row=0, column=2, padx=10, pady=ypad, sticky='ew')

        # Pressão arterial
        arterial_label = ctk.CTkLabel(linha_frame, text=dados[2], font=U.f_simples, text_color='#1C3942')
        arterial_label.grid(row=0, column=3, padx=10, pady=ypad, sticky='ew')

        # Saturação
        saturation_label = ctk.CTkLabel(linha_frame, text=dados[3], font=U.f_simples, text_color='#1C3942')
        saturation_label.grid(row=0, column=4, padx=10, pady=ypad, sticky='ew')

    for col in range(len(headers)):
        frame.columnconfigure(col, weight=1)  # Expansão de colunas

inserir_registros_com_grid(reg_frm, dic_teste)

# Agora que vi que esqueci de fazer as linhas separando os valores da tabela (sinto que to esquecendo mais alguma coisa)
# Tenho que fazer a função de alterar a página da tabela mas vou usar como desculpa que não sei como vamos retirar as info do db então lero lero lero

janela.mainloop()
