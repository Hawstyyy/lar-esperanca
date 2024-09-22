try:
    import pymysql.cursors
    from config import DB_CONFIG
except ImportError as e:
    print(f'Você não possui os arquivos necessários!\nErro:{e}')

class DB:
    def __init__(self) -> None:
        self.database = pymysql.connect(**DB_CONFIG)
        self.cursor: pymysql.cursors.Cursor = self.database.cursor()

    def close(self):
        """Fecha a conexão com o banco. Importante para não empedir novas conexões"""
        self.cursor.close()
        self.database.close()

    def f_one(self):
        """Retorna apenas uma linha por vez"""
        return self.cursor.fetchone()
    
    def f_all(self):
        """Retorna todas as linhas"""
        return self.cursor.fetchall()
    
    def f_many(self, quantidade = None):
        """Retorna a quantidade selecionada de linhas por vez"""
        return self.cursor.fetchmany(quantidade)
    
    def exec(self, query:str, args = None):
        """Executa a query"""
        self.cursor.execute(query=query, args=args)
    def commit(self):
        """Aplica mudanças ao Banco de dados, como insert, update, etc"""
        self.database.commit()
