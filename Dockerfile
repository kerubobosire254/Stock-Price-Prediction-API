# ---- Base Image ----
FROM python:3.10-slim

# ---- Environment Variables ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System Dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# ---- Work Directory ----
WORKDIR /app

# ---- Install Python Dependencies ----
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---- Create Non-Root User ----
RUN useradd -m appuser
USER appuser

# ---- Copy Application Code ----
COPY --chown=appuser:appuser . .

# ---- Expose Port ----
EXPOSE 5000

# ---- Environment ----
ENV FLASK_ENV=production

# ---- Run App ----
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "60", "app:app"]
