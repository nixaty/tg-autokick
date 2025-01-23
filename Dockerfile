FROM python:3.12-slim

WORKDIR /autokickbot
COPY requirements.txt /autokickbot/

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Копировать код
COPY . /autokickbot

CMD python main.py
