FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN -r requirements.txt

ADD scraper.py .

ADD cleaning.py .

ADD geocoder.py .

ENTRYPOINT ["python3"]

