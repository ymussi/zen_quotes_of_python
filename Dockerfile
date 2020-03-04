# FROM python:3.6
# LABEL mantainer="ymussi@gmail.com"
# LABEL fileversion=v0.1

# ARG RUN_ENVIRONMENT
# ENV DBENV=${RUN_ENVIRONMENT}
# ENV DD_LOGS_STDOUT=yes
# ENV PYTHONUNBUFFERED=TRUE
# ENV TZ=America/Sao_Paulo

# WORKDIR /app/zen

# COPY . .

# RUN apt-get update -y && \
#     apt-get install -y python3-pip python3-dev && \
#     apt-get install -y uwsgi uwsgi-plugin-python3 git && \
#     ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# RUN python setup.py develop

# ENTRYPOINT ["/bin/sh","/app/zen/entrypoint.sh"]

FROM python:3.6-stretch
LABEL fileversion=v0.1

ARG RUN_ENVIRONMENT
ENV DBENV=${RUN_ENVIRONMENT}

# Para que os logs apareçam no datadog
ENV PYTHONUNBUFFERED=TRUE
EXPOSE 5000

WORKDIR /app/zen/

COPY . .

RUN apt-get update -y && apt install -y uwsgi uwsgi-src uuid-dev libcap-dev

RUN export PYTHON=python3.6 && \
    uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36" && \
    mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so && \
    chmod 644 /usr/lib/uwsgi/plugins/python36_plugin.so

RUN pip install -r requirements.txt --quiet

RUN cd /app/zen

ENTRYPOINT ["/bin/sh","/app/zen/entrypoint.sh"]
