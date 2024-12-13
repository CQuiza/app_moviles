# pull official base image
FROM python:3.12-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#pango es una dependencia de weasyprint ## a partir de gdal son todas para geodjango
RUN apk update && apk add postgresql-dev g++ gcc musl-dev libpq-dev wget pango gdal-dev geos-dev proj-dev gcc musl-dev \
     libffi-dev python3-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
     libc-dev linux-headers 

 

# install dependencies // la linea 22 es nueva
RUN pip install --upgrade pip
#RUN pip install --upgrade pip setuptools wheel


COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x initdb.sh
RUN pip install --upgrade pip