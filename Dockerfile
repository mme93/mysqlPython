FROM python:3.9.5

WORKDIR /test-app

RUN pip install mysql-connector-python

COPY ./app ./app

CMD ["python","./app/main.py"]