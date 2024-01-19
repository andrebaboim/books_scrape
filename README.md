# Web Scraping com livros

## Deploy

Para executar o projeto, no terminal executar o seguinte comando na raiz do projeto:
```
make init
```

Após executar verificar se com o seguinte comando se o container do banco de dados está de pé:

```
docker ps -a
```

O container tem que estar funcionando sem problemas:

- books-scrape

Acompanhado o terminando, todas as informações sobre o processo será mostrada no terminal para acompanhamento.

## Extração de dados

Para a realização da extração e armazenamento dos dados as seguintes tecnologias foram utilizadas:

- Ubuntu WSL
- Docker Desktop com WSL 2
- Python 3.10 - Com as seguintes bibliotecas:  pandas-2.1.4-cp310, SQLAlchemy-2.0, mysql_connector_python-8.3
- Container MySQL latest realease

## Modelagem de dados

Todas as tabelas e o banco de dados é criado no processo de init, então não é necessário nenhuma intervenção manual para a execução dos SQL.

Foram criadas 3 tabelas para a solução do problema:

- categorias
- livros
- resultados_livros

O desenho se encontra no diretório: modelagem_bd no projeto.

## Agregação de dados

A tabela de agregação de dados é a seguinte: books_scrape.

## Destroy project

Para derrubar o container de banco de dados, executar:

```
make drop
```