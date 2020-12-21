FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
    --no-cache \
    python3-dev \
    build-base \
    linux-headers \
    pcre-dev
RUN apk add --no-cache pcre
WORKDIR /products
COPY . /products
RUN pip install -r /products/requirements.txt
RUN pip install uwsgi
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5000
CMD ["uwsgi", "--ini", "/products/wsgi.ini"]