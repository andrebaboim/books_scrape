import pandas as pd
from sqlalchemy import create_engine
from tables import generateTables


def database_writer():
    df = pd.read_json('books_toscrape.json')

    columns_rename_dict = {
        'Title': 'titulo_livro',
        'UPC': 'codigo_barra',
        'Category': 'nome_categoria',
        'Price (GBP)': 'preco',
        'Stock': 'quantidade_estoque',
        'Rating': 'avaliacao'
    }

    # Renomeando as colunas
    df = df.rename(columns=columns_rename_dict)

    processor = generateTables.DataFrameProcessor(df)
    df_categorias = processor.dataframe_categorias()
    df_titulos = processor.dataframe_titulos(df_categorias)

    engine = create_engine('mysql+pymysql://root:mysql@localhost:3306/books_scrape')
    df_categorias.to_sql('categorias', con=engine, if_exists='append', index=False)
    df_titulos.to_sql('livros', con=engine, if_exists='append', index=False)
    
