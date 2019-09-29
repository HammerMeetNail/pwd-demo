FROM python:3.7-alpine

COPY app.py /app/app.py

WORKDIR /app

ENTRYPOINT ["python3", "app.py"]