import customtkinter as ctk
from util import FontsUI as f
from util import imagemCTK as img
from db_handler import DB

janela = ctk.CTk()
janela.state('zoomed')
janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
janela.configure(fg_color='#FAFEFC')
janela.title("Lista")
janela.resizable(False, False)

db = DB()

# Apenas para ter noção de espaço
hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
hotbar_frame.place(relx=.5, rely=.045, anchor="center")
back_icon = ctk.CTkLabel(janela, text='', image=img('imagens/hotbar/back_icon.png', 40, 40))
back_icon.place(relx=.02, rely=.12, anchor='center')

dic_teste = {}

try:
    query = """
SELECT 
    p.id_paciente, 
    p.nome_paciente, 
    s.temperatura, 
    s.pressao_cardiaca, 
    CONCAT(s.pressao_sistolica, '/', s.pressao_diastolica) AS pressao_arterial, 
    s.saturacao, 
    er.estado AS estado_risco,  -- Aqui estamos selecionando o estado
    p.status_paciente
FROM 
    paciente p
JOIN 
    sinal_vital s ON p.id_paciente = s.id_paciente
JOIN 
    estado_risco er ON s.id_estado_risco = er.id_estado_risco  -- Certifique-se de que esta junção está correta
ORDER BY 
    p.id_paciente;
    """
    db.exec(query)
    resultados = db.f_all()
    
    for row in resultados:
        id_paciente = row[0]
        nome_paciente = row[1]
        dados_vitais = [row[2], row[3], row[4], row[5], row[6]]  # Temperatura, Pressão, Saturação, Status
        dic_teste[id_paciente] = {'nome': nome_paciente, 'dados': dados_vitais}

    print(dic_teste)

finally:
    db.close()

headers = ["Paciente", "Temperatura", "Cardíaca", "Arterial", "Saturação", "Status"]

search_frm = ctk.CTkFrame(janela, width=200, height=70)
search_frm.place(relx=.05, rely=0.25)

tt_lbl = ctk.CTkLabel(janela, text='Registros', font=(f.titulo_negrito), text_color='#48818D')
tt_lbl.place(relx=.5, rely=0.18, anchor='center')

# Frame principal
reg_frm = ctk.CTkFrame(janela, width=1450, height=640, fg_color='transparent', corner_radius=10)
reg_frm.place(relx=.2, rely=.23)

reg_frm.grid_rowconfigure(0, weight=1)
reg_frm.grid_rowconfigure(1, weight=99)
reg_frm.columnconfigure(0, weight=1)
reg_frm.grid_propagate(False)

header_frm = ctk.CTkFrame(reg_frm, fg_color='#48818D', height=80, corner_radius=10)
header_frm.grid(row=0, column=0, sticky='nsew', pady=(0, 20))
header_frm.grid_propagate(False)

for col in range(len(headers)):
    header_frm.grid_columnconfigure(col, weight=1)
header_frm.rowconfigure(0, weight=1)

for col, header in enumerate(headers):
    header_label = ctk.CTkLabel(header_frm, text=header, font=f.titulo, text_color='#FFFFFF')
    header_label.grid(row=0, column=col, pady=10, padx=5, sticky='nsew')
    header_label.grid_propagate(False)

# Lines frames >> Aqui entram as linhas (frames) com cores intercaladas
line_frame = ctk.CTkFrame(reg_frm, fg_color='transparent', corner_radius=10)
line_frame.grid(column=0, row=1, sticky='new')
line_frame.columnconfigure(0, weight=1)
line_frame.rowconfigure(0, weight=1)
line_frame.rowconfigure(9, weight=1)

# Index das páginas
x = 0
linhas = []  # Lista para armazenar as linhas

def hover_fake_enter(event, label):
    label.configure(fg_color="light blue")
    label.configure(cursor="hand2")

def hover_fake_leave(event, label):
    label.configure(fg_color="transparent")
    label.configure(cursor='')

# ID do label
def search_id(event, nome_paciente, id_paciente, label):
    print(f'O id do paciente {nome_paciente} é {id_paciente}!')
    
    label.configure(fg_color="#2D5E6C", text_color = 'white')

    label.after(150, lambda: label.configure(fg_color="transparent", text_color='#1C3942'))
    
# Função para gerar as linhas na tabela
def gerar_linhas(frame, headers, pacientes, start_index):
    max_char = 15
    for idx, (id_paciente, info) in enumerate(list(pacientes.items())[start_index:start_index + 10]):
        linha_frame = ctk.CTkFrame(frame, fg_color='#DBF0EE' if idx % 2 == 0 else '#F5F5F5', height=45, corner_radius=10)
        linha_frame.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        linha_frame.grid_propagate(False)

        paciente_truncado = info['nome'] if len(info['nome']) <= max_char else info['nome'][:max_char] + "..."

        linha_labels = []
        for idy, valor in enumerate([paciente_truncado] + info['dados']):
            label = ctk.CTkLabel(linha_frame, text=valor, font=(f.simples), text_color='#1C3942', corner_radius=10)
            if idy == 2:  # Add BPM no label
                label.configure(text=f'{valor} BPM')
            elif idy == 5:  # Coluna 6 (status)
                if info['dados'][-1] == 'Normal':  # 0 sendo OK e 1 sendo RISCO
                    label.configure(text='', image=img('imagens/check_icon.png', 30, 30))
                else:
                    label.configure(text='', image=img('imagens/alert_icon_red.png', 30, 30))

            # Bind do search id
            if idy == 0:
                if idy == 0:
                    label.bind("<Button-1>", lambda event, nome=info['nome'], id_paciente=id_paciente, lbl=label: search_id(event, nome, id_paciente, lbl))

                # Hover fake
                label.bind("<Enter>", lambda e, label=label: hover_fake_enter(e, label))
                label.bind("<Leave>", lambda e, label=label: hover_fake_leave(e, label))

            label.grid(column=idy, row=0, sticky='news', ipady=3, padx=5, pady=5)
            label.grid_propagate(False)
            linha_labels.append(label)

        linha_frame.grid(row=idx, column=0, sticky='news', pady=0)
        linhas.append((linha_frame, linha_labels, id_paciente))

gerar_linhas(line_frame, headers, dic_teste, x)

# Funções para mudar de página
def next_pag():
    global x
    if (x)*10 < len(dic_teste) - 10:
        x += 1
        atualizar_linhas()
        pag_label.configure(text=f'{x+1}')
    else: 
        x = x

def back_pag():
    global x
    if x > 0:
        x -= 1
    else: 
        x = 0
    atualizar_linhas()
    pag_label.configure(text=f'{x+1}')

def atualizar_linhas():
    for idx, (linha_frame, linha_labels, id_paciente) in enumerate(linhas):
        # Remove binds de clique e hover para não acumular 
        linha_labels[0].unbind("<Button-1>")
        linha_labels[0].unbind("<Enter>")
        linha_labels[0].unbind("<Leave>") 

        if idx < 10:  # Limita até 10 linhas
            if (x * 10 + idx) < len(dic_teste):  # Verifica se existe paciente para essa linha
                id_paciente = list(dic_teste.keys())[x * 10 + idx]
                info = dic_teste[id_paciente]
                
                # Atualiza as labels com os novos dados
                linha_labels[0].configure(text=info['nome'] if len(info['nome']) <= 15 else info['nome'][:15] + "...")
                linha_labels[1].configure(text=info['dados'][0])  # Temperatura
                linha_labels[2].configure(text=f"{info['dados'][1]} BPM")  # Cardíaca
                linha_labels[3].configure(text=info['dados'][2])  # Arterial
                linha_labels[4].configure(text=info['dados'][3])  # Saturação
                linha_labels[5].configure(
                    text='',
                    image=img('imagens/check_icon.png', 30, 30) if info['dados'][-1] == 'Normal' else img('imagens/alert_icon_red.png', 30, 30)
                )

                # Adiciona novamente os binds
                linha_labels[0].bind("<Button-1>", lambda event, nome=info['nome'], id_paciente=id_paciente, lbl=linha_labels[0]: search_id(event, nome, id_paciente, lbl))
                linha_labels[0].bind("<Enter>", lambda event, lbl=linha_labels[0]: hover_fake_enter(event, lbl))
                linha_labels[0].bind("<Leave>", lambda event, lbl=linha_labels[0]: hover_fake_leave(event, lbl))
            else:
                # Limpa as labels se não houver paciente
                for label in linha_labels:
                    label.configure(text='')
                    label.configure(image='')

# Linhas verticais
def linhas_coluna(px):
    linha = ctk.CTkLabel(line_frame, text='', width=4, height=450, bg_color='transparent', image=img('imagens/linha_tabelas.png', 4, 450))
    linha.place(relx=px, rely=0, anchor='nw')

linhas_coluna(.165)
linhas_coluna(.34)
linhas_coluna(.5)
linhas_coluna(.66)
linhas_coluna(.845)

# --------- Botões para avançar ou retroceder a página da lista ---------
frame_but = ctk.CTkFrame(janela, fg_color='transparent')
frame_but.place(relx=.576, rely=0.8, anchor='center')
frame_but.columnconfigure(0, weight=1)
frame_but.columnconfigure(1, weight=1)
frame_but.columnconfigure(2, weight=1)


back_but = ctk.CTkButton(frame_but, text='', fg_color='#48818D', hover_color='#72B4B0', image=img('imagens/arrow_esquerda.png', 24, 24), width=80, height=40, corner_radius=10, command=back_pag)
back_but.grid(row=0, column=0, sticky='ens', padx=10)

pag_frame = ctk.CTkFrame(frame_but, fg_color='#48818D', width=80, height=40, corner_radius=8)
pag_frame.grid(row=0, column=1, sticky='wens')

pag_label = ctk.CTkLabel(pag_frame, text=f'{x + 1}', font=f.subtitulo_negrito, text_color='#FFFFFF')
pag_label.place(relx=0.5, rely=0.5, anchor='center')

next_but = ctk.CTkButton(frame_but, text='', fg_color='#48818D', hover_color='#72B4B0', image=img('imagens/arrow_direita.png', 24, 24), width=80, height=40, corner_radius=10, command=next_pag)
next_but.grid(row=0, column=2, sticky='nse', padx=10)

janela.mainloop()
