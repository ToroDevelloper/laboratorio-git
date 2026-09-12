# syntax=docker/dockerfile:1

# ---------- Builder stage ----------
FROM python:3.12-slim AS builder
WORKDIR /app

# Install build dependencies (if any) and project requirements
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Runtime stage ----------
FROM python:3.12-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy application source code
COPY src/ .

# Create a non‑root user for security
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser

# Default command runs the test suite; adjust as needed
CMD ["python", "-m", "pytest"]