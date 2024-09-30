import customtkinter as ctk
from util import FontsUI as f
from util import imagemCTK as img

janela = ctk.CTk()
janela.state('zoomed')
janela.geometry(f'{janela.winfo_width()}x{janela.winfo_height()}')
janela.configure(fg_color='#FAFEFC')
janela.title("Lista")
janela.resizable(False, False)

# Apenas para ter noção de espaço
hotbar_frame = ctk.CTkFrame(janela, width=janela.winfo_width(), height=98, fg_color='#8ED6D0', corner_radius=0)
hotbar_frame.place(relx=.5, rely=.045, anchor="center")
back_icon = ctk.CTkLabel(janela, text='', image=img('imagens/hotbar/back_icon.png', 40, 40))
back_icon.place(relx=.02, rely=.12, anchor='center')

dic_teste = {
    'Lucas Oliveira Silva': ['33º', '72', '120/80', '98%', 0],
    'Maria Fernanda dos Santos': ['34º', '68', '115/75', '96%', 0],
    'João Pedro Almeida Costa': ['32º', '75', '118/78', '99%', 1],
    'Ana Paula de Souza Lima': ['33º', '70', '122/80', '97%', 0],
    'Carlos Eduardo Ribeiro': ['34º', '65', '110/70', '95%', 1],
    'Sofia Alice Pereira Gomes': ['33º', '80', '125/82', '100%', 1],
    'Fernando Henrique Mendes': ['35º', '74', '119/77', '97%', 1],
    'Juliana Cristina da Rocha': ['33º', '78', '117/79', '98%', 0],
    'Gabriel Augusto Martins': ['32º', '69', '116/76', '96%', 0],
    'Larissa Fernanda Nascimento': ['34º', '73', '121/81', '97%', 1],
    'Rafael Lima e Silva': ['33º', '67', '113/72', '95%', 0],
    'Beatriz Gomes da Silva': ['32º', '76', '120/80', '98%', 0],
    'Pedro Henrique Alves': ['33º', '70', '118/79', '97%', 1],
    'Isabella de Andrade Lima': ['34º', '68', '117/77', '96%', 0],
    'Felipe Augusto de Souza': ['33º', '71', '116/78', '98%', 1],
    'Clara Maria de Oliveira': ['32º', '74', '115/76', '99%', 0],
    'Vinícius da Silva Costa': ['35º', '72', '119/80', '97%', 1],
    'Mariana Gabriela Santos': ['34º', '67', '118/78', '96%', 0],
    'Luiz Carlos Ferreira': ['33º', '69', '117/75', '98%', 1],
    'Julia Alves de Lima': ['32º', '73', '116/77', '95%', 0],
    'Thiago Costa Ferreira': ['34º', '72', '120/78', '98%', 0],
    'Fernanda Martins e Silva': ['33º', '70', '118/79', '97%', 1],
    'Cecília Maria de Souza': ['32º', '68', '115/76', '96%', 1],
    'Henrique de Oliveira Lima': ['35º', '69', '119/80', '98%', 1],
    'Camila Souza Ferreira': ['33º', '75', '120/81', '96%', 0],
    'Eduardo Nascimento da Silva': ['34º', '65', '118/77', '97%', 1],
    'Ana Clara da Rocha': ['33º', '71', '116/78', '98%', 1],
    'Gabriel Martins de Souza': ['32º', '74', '115/76', '99%', 0],
    'Roberta Lima de Oliveira': ['35º', '72', '119/80', '97%', 1],
    'Bruno Henrique Gomes': ['34º', '68', '117/79', '96%', 0],
    'Lívia Maria Santos': ['33º', '69', '116/77', '95%', 0],
    'Thiago da Silva Costa': ['34º', '74', '115/76', '98%', 1],
    'Alessandra de Souza Lima': ['32º', '73', '120/80', '99%', 1],
    'Matheus Oliveira da Rocha': ['35º', '70', '119/81', '96%', 0],
    'Nathalia Costa e Silva': ['33º', '72', '120/79', '98%', 1],
    'Igor Santos de Almeida': ['34º', '68', '118/78', '96%', 1],
    'Karina Alves de Oliveira': ['32º', '75', '116/76', '99%', 0],
    'André Gomes da Silva': ['35º', '71', '115/77', '97%', 1],
    'Robson da Silva Costa': ['33º', '69', '117/78', '95%', 0],
    'Ana Paula de Souza': ['34º', '73', '120/81', '98%', 0],
    'Samuel Henrique Ferreira': ['32º', '68', '115/75', '96%', 1],
    'Rafaela Costa de Almeida': ['33º', '76', '120/80', '98%', 0],
    'Vitor Martins de Oliveira': ['34º', '72', '117/79', '97%', 1],
    'Juliana Ribeiro da Silva': ['32º', '74', '119/80', '96%', 0],
    'Gustavo Alves de Lima': ['35º', '75', '120/82', '97%', 0],
    'Marcel de Souza e Silva': ['34º', '68', '118/76', '96%', 0],
    'Sérgio Almeida Costa': ['33º', '67', '113/72', '95%', 0],
    'Cynthia Maria Santos': ['32º', '69', '116/78', '98%', 1],
    'Eduarda de Oliveira Lima': ['34º', '73', '120/80', '97%', 1],
    'Renato Ferreira e Silva': ['32º', '74', '119/81', '95%', 0],
    'Tânia Maria da Rocha': ['33º', '70', '122/80', '97%', 0],
    'Alexandre de Souza': ['34º', '68', '117/75', '96%', 1],
    'Karla Cristina da Silva': ['33º', '71', '116/78', '98%', 1],
    'Valentina Costa Ferreira': ['32º', '72', '119/77', '98%', 0],
    'Felipe dos Santos Nascimento': ['34º', '67', '115/76', '95%', 0],
}

headers = ["Paciente", "Temperatura", "Cardíaca", "Arterial", "Saturação", "Status"]

search_frm = ctk.CTkFrame(janela, width=200, height=70)
search_frm.place(relx=.05, rely=0.25)

tt_lbl = ctk.CTkLabel(janela, text='Registros', font=(f.titulo_negrito), text_color='#1C3942')
tt_lbl.place(relx=.5, rely=0.18, anchor='center')

# Frame principal
reg_frm = ctk.CTkFrame(janela, width=1450, height=640, fg_color='transparent', corner_radius=10)
reg_frm.place(relx=.2, rely=.23)

# Configuração do grid para o cabeçalho
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

# Função para gerar as linhas na tabela
def gerar_linhas(frame, headers, pacientes, start_index):
    max_char = 15
    for idx, (paciente, dados) in enumerate(list(pacientes.items())[start_index:start_index + 10]):
        linha_frame = ctk.CTkFrame(frame, fg_color='#DBF0EE' if idx % 2 == 0 else '#F5F5F5', height=45, corner_radius=10)
        linha_frame.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        linha_frame.grid_propagate(False)

        paciente_truncado = paciente if len(paciente) <= max_char else paciente[:max_char] + "..."

        # Dados paciente
        linha_labels = []  # Lista para armazenar as labels da linha
        for idy, valor in enumerate([paciente_truncado] + dados):
            label = ctk.CTkLabel(linha_frame, text=valor, font=(f.simples), text_color='#1C3942')
            if idy == 2:  # Add BPM no label
                label.configure(text=f'{valor} BPM')
            elif idy == 5:  # Coluna 6 (status)
                if dados[-1] == 0:  # 0 sendo OK e 1 sendo RISCO
                    label.configure(text='', image=img('imagens/check_icon.png', 30, 30))
                else:
                    label.configure(text='', image=img('imagens/alert_icon.png', 30, 26))
            label.grid(column=idy, row=0, sticky='news', ipady=3, padx=5, pady=5)
            label.grid_propagate(False)
            linha_labels.append(label)  # Adiciona a label à lista

        linha_frame.grid(row=idx, column=0, sticky='news', pady=0)
        linhas.append((linha_frame, linha_labels))  # Adiciona o frame e as labels à lista

gerar_linhas(line_frame, headers, dic_teste, x)

# Funções para mudar de página
def next_pag():
    global x
    if (x)*10 < len(dic_teste) - 10:  # Limita o avanço de páginas
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
    for idx, (linha_frame, linha_labels) in enumerate(linhas):
        if idx < 10:  # Limita até 10 linhas
            if (x * 10 + idx) < len(dic_teste):  # Verifica se existe paciente para essa linha
                paciente = list(dic_teste.keys())[x * 10 + idx]
                dados = dic_teste[paciente]
                # Atualiza as labels com os novos dados
                linha_labels[0].configure(text=paciente if len(paciente) <= 15 else paciente[:15] + "...")
                linha_labels[1].configure(text=dados[0])  # Temperatura
                linha_labels[2].configure(text=f'{dados[1]} BPM')  # Cardíaca
                linha_labels[3].configure(text=dados[2])  # Arterial
                linha_labels[4].configure(text=dados[3])  # Saturação
                # Atualiza status
                linha_labels[5].configure(text='', image=img('imagens/check_icon.png', 30, 30) if dados[-1] == 0 else img('imagens/alert_icon.png', 30, 26))
            else:
                # Limpa as labels se não houver paciente
                for label in linha_labels:
                    label.configure(text='')
                    label.configure(image='')

# Linhas verticais
def linhas_coluna(px):
    linha = ctk.CTkLabel(line_frame, text='', width=4, height=450, bg_color='transparent', image=img('imagens/linha_tabelas.png', 4, 450))
    linha.place(relx=px, rely=0.5, anchor='center')

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