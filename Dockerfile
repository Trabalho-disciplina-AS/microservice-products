FROM python:3-alpine
RUN apk add rrdtool
RUN apk add --virtual .build-dependencies \
    --no-cache \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev
RUN apk add --no-cache pcre
WORKDIR /data_extraction
COPY . /data_extraction
RUN pip install -r /data_extraction/requirements.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5000
CMD ["uwsgi", "--ini", "/data_extraction/wsgi.ini"]