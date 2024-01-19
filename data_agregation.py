import mysql.connector
import pandas as pd
from sqlalchemy import create_engine


connection = mysql.connector.connect(
    host='localhost', 
    port=3306,
    user='root',
    password='mysql',
    database='books_scrape'
)

query = "SELECT * FROM livros"
df = pd.read_sql(query, connection)

connection.close()


preco_minimo = df['preco'].min()
preco_mediano = df['preco'].median()
preco_maximo = df['preco'].max()

avaliacao_minima = df['avaliacao'].min()
avaliacao_mediana = df['avaliacao'].median()
avaliacao_maxima = df['avaliacao'].max()

titulo_mais_caro = df.sort_values(by=['preco', 'titulo_livro'], ascending=[False, True]).iloc[0]['titulo_livro']
titulo_maior_avaliacao = df.sort_values(by=['avaliacao', 'titulo_livro'], ascending=[False, True]).iloc[0]['titulo_livro']

resultados = {
    'Estatística': ['preco_minimo', 'preco_mediano', 'preco_maximo', 
                    'avaliacao_minima', 'avaliacao_mediana', 'avaliacao_maxima', 
                    'titulo_mais_caro', 'titulo_maior_avaliacao'],
    'Valor': [preco_minimo, preco_mediano, preco_maximo, 
              avaliacao_minima, avaliacao_mediana, avaliacao_maxima, 
              titulo_mais_caro, titulo_maior_avaliacao]
}

# Convertendo o dicionário em um DataFrame
df_resultados = pd.DataFrame(resultados)

engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/books_scrape')
df_resultados.to_sql('resultados_livros', con=engine, if_exists='append', index=False)