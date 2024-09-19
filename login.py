
import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import pymysql.cursors # pip install PyMySQL para adquirir essa blibioteca
# Tkinter é utilizado para criação da interface e janela.
from tabela_pacientes import TabelaPaciente



# Root
## È a base de todas as janelas, para mudar todas ao mesmo tempo. Mude o root.
root = ctk.CTk()

root.geometry("1440x900") # Define o tamanho em pixels da janela
root.title("Lar Esperança") # Define o nome da janela, visto no canto esquerdo superior.

# Paginas
# Todos os frames começam com p_

## Todas as páginas não variáveis que tem no programa
### Login
p_login = ctk.CTkFrame(root, fg_color= 'gray', corner_radius= 0)
p_login.place(relheight=1,relwidth=1)
### Tela Principal
p_principal = ctk.CTkFrame(root,bg_color='gray', corner_radius= 0)
p_principal.place(relheight=1,relwidth=1)
### Tabela Pacientes
p_pacientes = ctk.CTkFrame(root,bg_color='gray', corner_radius= 0)
p_pacientes.place(relheight=1,relwidth=1)
### Nova Receita
p_receita = ctk.CTkFrame(root,bg_color='gray', corner_radius= 0)
p_receita.place(relheight=1,relwidth=1)
### Sinal Vital
p_sinal_vital = ctk.CTkFrame(root,bg_color='gray', corner_radius= 0)
p_sinal_vital.place(relheight=1,relwidth=1)
### Intercorrência
p_intercorrencia = ctk.CTkFrame(root,bg_color='gray', corner_radius= 0)
p_intercorrencia.place(relheight=1,relwidth=1)
### Registro de Funcionário
p_registro = ctk.CTkFrame(root, fg_color= 'gray', corner_radius= 0)
p_registro.place(relheight=1,relwidth=1)


# Coloca a Pagina de login como pagina inicial
p_login.tkraise()

root.mainloop() # Faz com que o programa rode.