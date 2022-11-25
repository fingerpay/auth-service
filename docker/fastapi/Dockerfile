FROM python:3.9-buster
USER root
MAINTAINER ITO Manaki <colk@fingerpay.app>

ENV LC_ALL=en_US.UTF-8 \
    TZ=JST-9 \
    TERM=xtermdocker-attachingdocker-attaching

ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    # 激重なので upgrade はしない
    # && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends locales postgresql-client

RUN localedef -f UTF-8 -i en_US en_US.UTF-8

# 激重なので cleanup はしない
# RUN apt-get autoremove -y \
#    && apt-get clean -y \
#    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install poetry

RUN mkdir -p /deploy/auth-service

WORKDIR /deploy/auth-service

COPY ./Pipfile* ./
COPY ./pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi
