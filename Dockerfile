FROM python:3.9-slim-buster
LABEL maintainer="pawel.benkowski@xdsa.pl"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    postgresql-client
RUN pip install --upgrade pip setuptools poetry
RUN poetry --version
COPY ./poetry.lock .
COPY ./pyproject.toml .
RUN poetry config virtualenvs.create false
RUN poetry install

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser --disabled-login user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

COPY . /app