FROM python:3.11-slim

WORKDIR /switchs

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app/
COPY data data/
COPY templates templates/
COPY static static/
COPY nginx nginx/


CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app.main:app"]
