
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql.cursors # pip install PyMySQL para adquirir essa blibioteca
# Tkinter é utilizado para criação da interface e janela.



# Root
## È a base de todas as janelas, para mudar todas ao mesmo tempo. Mude o root.
root = tk.Tk()

root.geometry("1440x900") # Define o tamanho em pixels da janela
root.title("Lar Esperança") # Define o nome da janela, visto no canto esquerdo superior.

# Paginas
# Todos os frames começam com p_

## Todas as páginas não variáveis que tem no programa
### Login
p_login = tk.Frame(root,bg='gray')
p_login.place(relheight=1,relwidth=1)
### Tela Principal
p_principal = tk.Frame(root,bg='gray')
p_principal.place(relheight=1,relwidth=1)
### Tabela Pacientes
p_pacientes = tk.Frame(root,bg='gray')
p_pacientes.place(relheight=1,relwidth=1)
### Nova Receita
p_receita = tk.Frame(root,bg='gray')
p_receita.place(relheight=1,relwidth=1)
### Sinal Vital
p_sinal_vital = tk.Frame(root,bg='gray')
p_sinal_vital.place(relheight=1,relwidth=1)
### Intercorrência
p_intercorrencia = tk.Frame(root,bg='gray')
p_intercorrencia.place(relheight=1,relwidth=1)
### Registro de Funcionário
p_registro = tk.Frame(root,bg='gray')
p_registro.place(relheight=1,relwidth=1)

root.mainloop() # Faz com que o programa rode.