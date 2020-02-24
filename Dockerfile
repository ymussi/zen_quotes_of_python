FROM python:3.6
LABEL mantainer="ymussi@gmail.com"
LABEL fileversion=v0.1

ARG RUN_ENVIRONMENT
ENV DBENV=${RUN_ENVIRONMENT}
ENV DD_LOGS_STDOUT=yes
ENV PYTHONUNBUFFERED=TRUE
ENV TZ=America/Sao_Paulo

WORKDIR /app/zen

COPY . .

RUN apt-get update && pip install --upgrade pip && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

RUN python setup.py develop

ENTRYPOINT ["/bin/sh","/app/zen/entrypoint.sh"]