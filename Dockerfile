ARG PYTHON_VERSION=3.8-alpine3.11
ARG ALPINE_VERSION=3.11

FROM python:${PYTHON_VERSION} as install-env

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /tmp/install

COPY [ "./requirements.txt", "." ]

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

FROM alpine:${ALPINE_VERSION}

LABEL maintainer="Lucca Pessoa da Silva Matos - luccapsm@gmail.com" \
      org.label-schema.url="https://github.com/lpmatos" \
      org.label-schema.alpine="https://alpinelinux.org/" \
      org.label-schema.python="https://www.python.org/" \
      org.label-schema.name="Sentimental Analysis" 

ENV HOME=/usr/src/code

RUN set -ex && apk update && \
    addgroup -g 1000 python && adduser -u 999 -G python -h ${HOME} -s /bin/sh -D python && \
    mkdir -p ${HOME} && chown -hR python:python ${HOME}

RUN apk update && apk add --update --no-cache expat=2.2.9-r1 'su-exec>=0.2'

WORKDIR ${HOME}

COPY --chown=python:python --from=install-env [ "/usr/local", "/usr/local/" ]
COPY --chown=python:python [ "./code", "." ]
COPY [ "./docker-entrypoint.sh", "/usr/local/bin/" ]

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;

ENTRYPOINT [ "docker-entrypoint.sh" ]

CMD [ "sh" ]
