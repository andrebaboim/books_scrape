import pandas as pd

class DataFrameProcessor:
    """
    A class for processing dataframes.

    Args:
        df (pandas.DataFrame): The input dataframe.

    Attributes:
        df (pandas.DataFrame): The input dataframe.

    Methods:
        dataframe_categorias: Returns a dataframe with unique categories.
        dataframe_titulos: Returns a dataframe with titles and corresponding category IDs.
    """

    def __init__(self, df):
        self.df = df
        

    def dataframe_categorias(self):
        """
        Returns a dataframe with unique categories.

        Returns:
            pandas.DataFrame: A dataframe with unique categories.
        """
        categorias_unicas = self.df['nome_categoria'].unique()
        df_categorias = pd.DataFrame(categorias_unicas, columns=['nome_categoria'])
        df_categorias.insert(0, 'id_categoria', range(1, 1 + len(df_categorias)))
        return df_categorias


    def dataframe_titulos(self, df_categorias):
        """
        Returns a dataframe with titles and corresponding category IDs.

        Args:
            df_categorias (pandas.DataFrame): A dataframe with unique categories.

        Returns:
            pandas.DataFrame: A dataframe with titles and corresponding category IDs.
        """
        df_titulos = self.df.copy()
        categoria_para_id = dict(zip(df_categorias['nome_categoria'], df_categorias['id_categoria']))
        df_titulos['id_categoria'] = df_titulos['nome_categoria'].map(categoria_para_id)
        df_titulos.insert(0, 'id_livro', range(1, 1 + len(df_titulos)))
        colunas = ['id_livro', 'titulo_livro', 'codigo_barra', 'id_categoria', 'preco', 'quantidade_estoque', 'avaliacao']
        df_titulos = df_titulos[colunas]
        return df_titulos