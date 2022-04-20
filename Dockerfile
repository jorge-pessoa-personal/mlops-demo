FROM python:3.8

ENV HOST=0.0.0.0

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./main.py /app/main.py
COPY ./influx.py /app/influx.py
COPY ./models /app/models

WORKDIR /app

CMD ["gunicorn", "main:app"]
