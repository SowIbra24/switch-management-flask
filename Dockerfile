FROM python:3.11-slim

WORKDIR /switchs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app/
COPY data data/
COPY templates templates/
COPY static static/


CMD ["python", "app/main.py"]
