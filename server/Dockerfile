# syntax=docker/dockerfile:1

# I did a similar thing for myself a bit earlier, so I just took it from
# https://github.com/yuriymironov96/python-flask-docker

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind" , "0.0.0.0:5000", "wsgi:app", "--workers", "3"]