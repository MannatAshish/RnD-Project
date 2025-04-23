FROM python:3.11-slim

WORKDIR /app

COPY honeypot.py .

RUN mkdir /logs

CMD ["python", "honeypot.py"]