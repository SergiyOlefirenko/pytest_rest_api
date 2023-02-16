FROM python:3.9-alpine3.16

ARG marker='not db_test'
ENV env $marker

WORKDIR /usr/project
ENV PYTHONPATH=/usr/project

VOLUME [ "/allureress" ]

RUN apk update && apk upgrade && apk add bash
RUN apk add postgresql-dev gcc musl-dev

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -s -v -m "$env" tests/* --alluredir=allureress
