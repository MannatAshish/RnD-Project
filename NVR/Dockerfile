FROM python:3.11-slim

WORKDIR /app

COPY flaskapp.py .
COPY feed.py .
COPY onvif.py .

RUN pip install flask

EXPOSE 8000
EXPOSE 554
EXPOSE 80

CMD ["sh", "-c", "python feed.py & python flaskapp.py & python onvif.py"]