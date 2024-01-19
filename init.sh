#!/bin/bash

VENV_NAME="books_scrape"

if [ ! -d "$VENV_NAME" ]; then
    virtualenv $VENV_NAME
fi

# Ativa o ambiente virtual
source "$VENV_NAME/bin/activate"

pip3 install -r requirements.txt

docker run --name book-scrape -e MYSQL_ROOT_PASSWORD=mysql -p 3306:3306 -d mysql

sleep 10

python3 create_datatabase_books_scrape.py

python3 app/app.py

sleep 5

python3 data_agregation.py