# Pull base image
FROM python:3.12-slim

# Установка netcat-openbsd
RUN apt-get update \
    && apt-get install -y netcat-openbsd \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy project files
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh
