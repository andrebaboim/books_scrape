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
        CREATE DATABASE IF NOT EXISTS books_scrape;
        CREATE TABLE IF NOT EXISTS books_scrape.categorias (
            id_categoria integer NOT NULL,
            nome_categoria character varying(100) NOT NULL
        );
        CREATE TABLE IF NOT EXISTS books_scrape.livros (
            id_livro integer NOT NULL,
            titulo_livro character varying(255) NOT NULL,
            codigo_barra character varying(100) NOT NULL,
            id_categoria integer NOT NULL,
            preco real NOT NULL,
            quantidade_estoque integer,
            avaliacao integer
        );
        """
        cursor.execute(script_sql, multi=True)
        print("Tabelas criadas com sucesso")

except Error as e:
    print("Erro ao conectar ao MySQL", e)

finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão ao MySQL foi encerrada")
