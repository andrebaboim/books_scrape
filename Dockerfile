FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install requests bs4 sqlalchemy