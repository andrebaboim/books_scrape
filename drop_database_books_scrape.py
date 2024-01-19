import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost', 
        port=3306,
        user='root',
        password='mysql',
        database='mysql'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = connection.cursor()
        script_sql = """
        DROP TABLE IF EXISTS books_scrape.livros;
        DROP TABLE IF EXISTS books_scrape.categorias;
        DROP TABLE IF EXISTS books_scrape.resultados_livros;
        DROP DATABASE IF EXISTS books_scrape;
        """
        cursor.execute(script_sql, multi=True)
        print("Tabelas dropadas com sucesso")

except Error as e:
    print("Erro ao conectar ao MySQL", e)

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão ao MySQL foi encerrada")
