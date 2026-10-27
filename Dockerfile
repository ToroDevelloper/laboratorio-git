# syntax=docker/dockerfile:1

FROM python:3.12-slim AS builder
WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY src/ .

RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]
