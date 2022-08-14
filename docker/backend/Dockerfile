FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code/backend/

RUN apt update && apt -qy upgrade

ADD ./docker /code/docker
COPY . /code/

RUN pip install --upgrade pip

ADD ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

ENTRYPOINT ['python', 'manage.py', 'migrate']
