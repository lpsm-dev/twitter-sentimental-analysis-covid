ARG PYTHON_VERSION=3.8-alpine3.11
ARG ALPINE_VERSION=3.11

FROM python:${PYTHON_VERSION} as install-env

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /tmp/install

COPY [ "./requirements.txt", "." ]

RUN apk add --update --no-cache --virtual=build-dependencies linux-headers build-base && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    apk del --purge build-dependencies

FROM alpine:${ALPINE_VERSION}

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
      org.label-schema.url="https://github.com/lpmatos" \
      org.label-schema.alpine="https://alpinelinux.org/" \
      org.label-schema.python="https://www.python.org/" \
      org.label-schema.name="Twitter Sentimental Analysis API" 

ENV HOME=/app \
    LOG_PATH=/var/log/sentiment-analysis \
    LOG_FILE=file.log \
    LOG_LEVEL=DEBUG \
    LOGGER="Sentiment Analysis" \
    TWITTER_CONSUMER_KEY= \
    TWITTER_CONSUMER_SECRET= \
    TWITTER_ACCESS_TOKEN= \
    TWITTER_ACCESS_TOKEN_SECRET=

RUN set -ex && apk update && \
    addgroup -g 1000 python && adduser -u 999 -G python -h ${HOME} -s /bin/sh -D python && \
    mkdir -p ${HOME} && chown -hR python:python ${HOME} /var

RUN apk update && apk add --update --no-cache expat=2.2.9-r1 sqlite-dev=3.30.1-r1 libffi=3.2.1-r6 'su-exec>=0.2'

WORKDIR ${HOME}

COPY --chown=python:python --from=install-env [ "/usr/local", "/usr/local/" ]

RUN python -m nltk.downloader punkt

COPY --chown=python:python [ "./code", "/app" ]
COPY [ "./docker-entrypoint.sh", "/usr/local/bin/" ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

EXPOSE 5000

ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD [ "uwsgi", "--ini", "/app/uwsgi.ini" ]
