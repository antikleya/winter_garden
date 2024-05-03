FROM python:3.10

WORKDIR /srv

COPY ./requirements/base.txt /tmp

RUN pip install --no-cache-dir --upgrade -r /tmp/base.txt

COPY . .
