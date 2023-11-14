FROM python:3

ADD data.yml
ADD app.yml
ADD main.py

RUN pip install pyyaml


