FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./ugc_etl .

CMD python main.py