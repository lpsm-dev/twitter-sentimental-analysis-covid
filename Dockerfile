ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

FROM base as install-env

COPY [ "requirements.txt", "."]

RUN apk add --update --no-cache --virtual=build-dependencies linux-headers build-base && \
    pip install --upgrade pip && \
    pip install --user --no-warn-script-location -r ./requirements.txt && \
    apk del --purge build-dependencies

FROM base

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
        org.label-schema.version="1.0.0" \
        org.label-schema.release-data="07-06-2020" \
        org.label-schema.url="https://github.com/lpmatos" \
        org.label-schema.alpine="https://alpinelinux.org/" \
        org.label-schema.python="https://www.python.org/" \
        org.label-schema.name="IESB Project - Sentimental Analysis API"

ENV HOME=/usr/src/code

RUN set -ex && apk update && \
    addgroup -g 1000 python && adduser -u 999 -G python -h ${HOME} -s /bin/sh -D python && \
    mkdir -p ${HOME} && chown -hR python:python ${HOME} /var

RUN apk add --update --no-cache \
      bash=5.0.11-r1 \
      netcat-openbsd=1.130-r1 \
      expat=2.2.9-r1 \
      sqlite-dev=3.30.1-r2 \
      libffi=3.2.1-r6 \
      'su-exec>=0.2'

COPY --chown=python:python --from=install-env [ "/root/.local", "/usr/local" ]

RUN python -m nltk.downloader punkt

COPY [ "./scripts/docker-entrypoint", "/usr/local/bin" ]

WORKDIR ${HOME}

COPY --chown=python:python [ "./code", "." ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

EXPOSE 5000

CMD [ "uwsgi", "--ini", "/usr/src/code/uwsgi.ini" ]
