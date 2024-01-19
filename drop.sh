#!/bin/bash

python3 drop_database_books_scrape.py
docker stop book-scrape
docker rm book-scrape