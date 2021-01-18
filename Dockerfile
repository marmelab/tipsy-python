FROM python:3

WORKDIR /usr/src/app

COPY ./src/ ./

RUN ls
RUN pip install -r requirements.txt